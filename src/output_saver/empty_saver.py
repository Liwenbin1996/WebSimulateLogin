#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 10:51 AM
# @Author  : Liwenbin
# @File    : empty_saver.py
# @Project: WebSimulateLogin
from src.output_saver.base_saver import BaseSaver


class EmptySaver(BaseSaver):

    def __init__(self):
        super(EmptySaver, self).__init__()

    def save(self, login_info):
        pass

    def close(self):
        pass
