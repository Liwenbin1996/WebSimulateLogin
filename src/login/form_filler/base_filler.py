#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 7:18 PM
# @Author  : Liwenbin
# @File    : base_filler.py.py
# @Project: WebSimulateLogin
import logging
from typing import Optional
from dto.web_element import WebElement
from dto.browser import Browser


class FillerError(Exception):

    def __init__(self, msg):
        super(FillerError, self).__init__()
        self.message = "Filler: " + msg

    def __str__(self):
        return self.message


class BaseFiller(object):

    def __init__(self, browser):
        if not isinstance(browser, Browser):
            raise FillerError("invalid browser, expected type <dto.browser.Browser>")
        self._browser = browser

    def find_input_box(self) -> WebElement:
        raise NotImplementedError

    def fill_input_box(self, web_element, value=None) -> bool:
        raise NotImplementedError

    def fill(self, value=None) -> Optional[WebElement]:
        try:
            web_element = self.find_input_box()
            if web_element is None:
                return None
            fill_ret = self.fill_input_box(web_element, value)
            if fill_ret is True:
                return web_element
            return None
        except Exception as e:
            logging.debug("fill input box failed, err={}".format(str(e)))
            return None
