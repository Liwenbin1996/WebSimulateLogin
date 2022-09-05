#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 10:39 AM
# @Author  : Liwenbin
# @File    : param_parser.py.py
# @Project: WebSimulateLogin
import re
from typing import List
from urllib import request
from dto.login_info import LoginInfo
from src.input_parser.base_parser import BaseParser


class ParamParser(BaseParser):

    http_header = "http://"
    https_header = "https://"

    def __init__(self, url, username, password):
        super(ParamParser, self).__init__()
        self._url = url
        self._username = username
        self._password = password

    @staticmethod
    def _try_request_url(url):
        try:
            request.urlopen(url)
            return True
        except Exception as e:
            return False

    def parse(self) -> List[LoginInfo]:
        if not str(self._url).startswith(self.http_header) and not str(self._url).startswith(self.https_header):
            if self._try_request_url(self.http_header + self._url):
                self._url = self.http_header + self._url
            else:
                self._url = self.https_header + self._url

        login_info = LoginInfo([self._url], self._username, self._password)
        return [login_info]


if __name__ == "__main__":
    test_parser = ParamParser("www.github.com", "xxx", "yyy")
    test_ret = test_parser.parse()
    print(test_ret)
    for test_login_info in test_ret:
        print("{}-{}-{}-{}".format(test_login_info.urls, test_login_info.username, test_login_info.password,
                                   test_login_info.extra_info))
