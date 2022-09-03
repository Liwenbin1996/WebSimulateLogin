#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 10:49 AM
# @Author  : Liwenbin
# @File    : base_parser.py.py
# @Project: WebSimulateLogin
from typing import List
from dto.login_info import LoginInfo


class BaseParser(object):

    def __init__(self):
        pass

    def parse(self) -> List[LoginInfo]:
        raise NotImplementedError
