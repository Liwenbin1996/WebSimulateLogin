#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 6:11 PM
# @Author  : Liwenbin
# @File    : base_saver.py.py
# @Project: WebSimulateLogin


class BaseSaver(object):

    def save(self, login_info):
        raise NotImplementedError
