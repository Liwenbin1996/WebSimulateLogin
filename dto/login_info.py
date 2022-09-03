#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 10:44 AM
# @Author  : Liwenbin
# @File    : login_info.py.py
# @Project: WebSimulateLogin

class LoginStatus:
    success = u"成功"
    fail = u"失败"


class LoginInfo(object):

    def __init__(self, urls, username, password, extra_info=None):
        self._urls = urls
        self._username = username
        self._password = password
        self._login_status = LoginStatus.fail
        self._screenshot_path = ""
        self._extra_info = extra_info

    @property
    def urls(self):
        return self._urls

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def extra_info(self):
        return self._extra_info

    @property
    def login_status(self):
        return self._login_status

    @property
    def screenshot_path(self):
        return self._screenshot_path

    @screenshot_path.setter
    def screenshot_path(self, path):
        if not isinstance(path, str):
            raise TypeError("invalid path type, expected <str>")
        self._screenshot_path = path

    @extra_info.setter
    def extra_info(self, extra_info):
        self._extra_info = extra_info

    @login_status.setter
    def login_status(self, status):
        if status not in [LoginStatus.success, LoginStatus.fail]:
            raise TypeError("invalid login status, expected <LoginStatus.success> or <LoginStatus.fail>")
        self._login_status = status

    @urls.setter
    def urls(self, urls):
        self._urls = urls
