#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 4:51 PM
# @Author  : Liwenbin
# @File    : main.py
# @Project: WebSimulateLogin
import logging
from src.input_parser.excel_parser import ExcelParser
from src.login.login import LoginController
from src.output_saver.excel_saver import ExcelSaver
from dto.login_info import LoginStatus

if __name__ == "__main__":
    logging.info("====================START====================")

    input_parser = ExcelParser("input_parser/test/test_input_excel.xlsx")
    output_saver = ExcelSaver("output_saver/test/test_output_excel.xlsx")
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
        logging.info(
            "url: {} username: {} password: {} status: {}".format(valid_url, login_info.username, login_info.password,
                                                                  login_info.login_status))

    output_saver.close()

    logging.info("=====================END=====================")
