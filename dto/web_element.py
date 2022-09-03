#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 4:24 PM
# @Author  : Liwenbin
# @File    : web_element.py.py
# @Project: WebSimulateLogin
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement


class WebElementError(Exception):

    def __init__(self, msg):
        super(WebElementError, self).__init__()
        self.message = "WebElement: " + msg

    def __str__(self):
        return self.message


class WebElement(object):

    def __init__(self, selenium_web_elem):
        if not isinstance(selenium_web_elem, SeleniumWebElement):
            raise WebElementError("invalid web element, expected type: <SeleniumWebElement>")
        self._element = selenium_web_elem

    def send_key(self, value) -> None:
        """

        :param value:
        :return:
        """
        try:
            self._element.clear()
            self._element.send_keys(value)
        except Exception as e:
            raise WebElementError("send key error: {}".format(str(e)))

    def submit(self) -> None:
        try:
            self._element.submit()
        except Exception as e:
            raise WebElementError("submit error: {}".format(str(e)))

    def click(self) -> None:
        try:
            self._element.click()
        except Exception as e:
            raise WebElementError("click error: {}".format(str(e)))

    def get_attribute(self, name):
        return self._element.get_attribute(name)

    def screenshot(self, filename):
        return self._element.screenshot(filename)

    def is_display(self):
        return self._element.is_displayed()

    @property
    def accessible_name(self):
        return self._element.accessible_name
