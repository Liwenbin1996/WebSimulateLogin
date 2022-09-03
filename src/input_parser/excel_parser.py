#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 10:59 AM
# @Author  : Liwenbin
# @File    : excel_parser.py.py
# @Project: WebSimulateLogin
import logging
import re
import xlrd
from typing import List
from urllib import request
from dto.login_info import LoginInfo
from src.input_parser.base_parser import BaseParser
from conf.config import URL_REGEX


class ExcelParser(BaseParser):

    http_header = "http://"
    https_header = "https://"

    def __init__(self, file_path):
        super(ExcelParser, self).__init__()
        self._file_path = file_path

    def _read_excel(self) -> list:
        excel_reader = xlrd.open_workbook(self._file_path)
        sheet = excel_reader.sheets()[0]
        raw_data = []

        row_count = sheet.nrows
        col_count = sheet.ncols
        for i in range(row_count):
            row_data = []
            for j in range(col_count):
                row_data.append(sheet.row_values(i)[j])
            raw_data.append(row_data)
        return raw_data

    @staticmethod
    def _get_domain_from_url(url):
        url = re.sub("^[A-Za-z]+://", '', url)
        domain, _, _ = url.partition("/")
        return domain

    @staticmethod
    def _try_request_url(url):
        try:
            request.urlopen(url)
            # # 4xx和5xx的状态码
            # if status_code // 100 in [4, 5]:
            #     return False
            return True
        except Exception as e:
            return False

    def _extract_urls(self, url, proof):
        urls_tmp = [url, self._get_domain_from_url(url)]

        if proof and isinstance(proof, str):
            url_re_context = re.search(URL_REGEX, proof)
            if url_re_context:
                urls_tmp.append(url_re_context.group())

        urls_tmp = list(set(urls_tmp))

        urls = []
        for url in urls_tmp:
            if not str(url).startswith("http://") and not str(url).startswith("https://"):
                if self._try_request_url(self.http_header + url):
                    urls.append(self.http_header + url)
                else:
                    urls.append(self.https_header + url)
            else:
                urls.append(url)

        return list(set(urls))

    def _parse_raw_data(self, data_list) -> List[LoginInfo]:
        title_list = data_list[0]
        login_info_title_idx = {"URL": -1, "账号": -1, "密码": -1, "举证信息": -1}
        for title in login_info_title_idx.keys():
            idx = title_list.index(title)
            login_info_title_idx[title] = idx

        login_info_lst = []
        for data in data_list[1:]:
            url = data[login_info_title_idx["URL"]]
            proof = data[login_info_title_idx["举证信息"]]
            username = data[login_info_title_idx["账号"]]
            password = data[login_info_title_idx["密码"]]

            login_info = LoginInfo(self._extract_urls(url, proof), username, password)

            extra_info = []
            for i, value in enumerate(data):
                extra_info.append((title_list[i], value))
            login_info.extra_info = extra_info

            login_info_lst.append(login_info)
            logging.info("input parse, url: {}".format(url))

        return login_info_lst

    def parse(self) -> List[LoginInfo]:
        """
        1. 读取excel文件、加载数据
        2. 解析url, username, password等信息，封装成LoginInfo列表返回
        :return:
        """
        raw_data = self._read_excel()
        return self._parse_raw_data(raw_data)


if __name__ == "__main__":
    test_parser = ExcelParser("test/test_input_excel.xlsx")
    test_ret = test_parser.parse()
    print(test_ret)
    for test_login_info in test_ret:
        print("{}-{}-{}-{}".format(test_login_info.urls, test_login_info.username, test_login_info.password,
                                   test_login_info.extra_info))
