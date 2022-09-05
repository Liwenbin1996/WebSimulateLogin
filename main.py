#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 4:51 PM
# @Author  : Liwenbin
# @File    : main.py
# @Project: WebSimulateLogin
import argparse
import logging
import os

from src.input_parser.excel_parser import ExcelParser
from src.input_parser.param_parser import ParamParser
from src.login.login import LoginController
from src.output_saver.excel_saver import ExcelSaver
from src.output_saver.empty_saver import EmptySaver
from dto.login_info import LoginStatus


def parse_args():
    parser = argparse.ArgumentParser(description="WebSimulateLogin")
    parser.add_argument('-t', '--type', choices=['excel', 'cmd'], default='cmd',
                        help='输入方式，支持EXCEL文件格式(excel)和命令行参数(cmd)，默认为cmd方式')
    group_1 = parser.add_argument_group(title="EXCEL输入方式")
    group_1.add_argument('-i', '--input', type=str, help='输入文件名，-t=excel时生效')
    group_1.add_argument('-o', '--output', type=str, default='result.xlsx', help='输出文件名，-t=excel时生效')

    group_2 = parser.add_argument_group(title="命令行输入方式")
    group_2.add_argument('-u', '--url', type=str, help='URL，-t=cmd时生效')
    group_2.add_argument('-a', '--account', type=str, help='账号名，-t=cmd时生效')
    group_2.add_argument('-p', '--password', type=str, help='密码，-t=cmd时生效')
    args = parser.parse_args()
    if args.type == "cmd" and (not args.url or not args.account or not args.password):
        print("ERROR: URL、账号和密码不能为空")
        exit(0)
    if args.type == "excel":
        if not args.input:
            print("ERROR: 输入文件名不能为空")
            exit(0)
        if args.output:
            dir_name = os.path.dirname(args.output)
            if dir_name and not os.path.exists(dir_name):
                try:
                    os.makedirs(dir_name)
                except Exception:
                    print("ERROR: 创建目录{}失败，请手动创建".format(dir_name))
                    exit(0)
    return args


if __name__ == "__main__":
    input_args = parse_args()

    if input_args.type == "cmd":
        input_parser = ParamParser(input_args.url, input_args.account, input_args.password)
        output_saver = EmptySaver()
    else:
        input_parser = ExcelParser(input_args.input)
        output_saver = ExcelSaver(input_args.output)

    logging.info("====================START====================")

    login_info_lst = input_parser.parse()
    logging.info("input parse end...")

    for login_info in login_info_lst:
        urls = login_info.urls
        if not urls or not isinstance(urls, list):
            logging.warning("invalid urls: {}".format(urls))
            continue

        # 找出登录界面的url，如果找不到就默认用第一个url
        valid_url = urls[0]
        logging.info("try login, urls={}".format(urls))
        for url in urls:
            if LoginController().pre_check(url) is True:
                valid_url = url
                login_info.urls = [url]
                break

        login_status, img_path = LoginController().try_page_login(valid_url, login_info.username, login_info.password)
        login_info.login_status = LoginStatus.success if login_status else LoginStatus.fail
        login_info.screenshot_path = img_path

        output_saver.save(login_info)

        logging.info("*" * 25)
        logging.info("url:          {}".format(valid_url))
        logging.info("username:     {}".format(login_info.username))
        logging.info("password:     {}".format(login_info.password))
        logging.info("login_status: {}".format(login_info.login_status))
        logging.info("img_path:     {}".format(login_info.screenshot_path))
        logging.info("*" * 25)

    output_saver.close()

    logging.info("=====================END=====================")
