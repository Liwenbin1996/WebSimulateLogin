#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 7:30 PM
# @Author  : Liwenbin
# @File    : username_filler.py.py
# @Project: WebSimulateLogin
import logging
from typing import Optional

from dto.web_element import WebElement
from conf.config import CRACK_FORM_FIELD_DICT
from src.login.form_filler.base_filler import BaseFiller


class UsernameFiller(BaseFiller):

    def __init__(self, browser):
        super(UsernameFiller, self).__init__(browser)

    def _find_input_box_by_form_placeholder(self):
        placeholder_try_list = CRACK_FORM_FIELD_DICT["username"]["text_placeholder"]
        for try_placeholder in placeholder_try_list:
            try:
                web_elements = self._browser.find_elements_by_placeholder(try_placeholder)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find username input element by form.placeholder: {}".format(try_placeholder))
                        return web_element
            except Exception:
                continue
        logging.debug("cant find useful username input element by form.placeholder")
        return None

    def _find_input_box_by_form_id(self):
        id_try_list = CRACK_FORM_FIELD_DICT["username"]["general_keywords"]
        for try_id in id_try_list:
            try:
                search_str = "//input[@id='{}']".format(try_id)
                web_elements = self._browser.find_elements_by_xpath(search_str)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find username input element by form.id: {}".format(try_id))
                        return web_element
            except Exception:
                continue
        logging.debug("cant find useful username input element by form.id")
        return None

    def _find_input_box_by_form_name(self):
        name_try_list = CRACK_FORM_FIELD_DICT["username"]["general_keywords"]
        for try_name in name_try_list:
            try:
                search_str = "//input[@name='{}']".format(try_name)
                web_elements = self._browser.find_elements_by_xpath(search_str)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find username input element by form.name: {}".format(try_name))
                        return web_element
            except Exception:
                continue
        logging.debug("cant find useful username input element by form.name")
        return None

    def _find_input_box_by_form_class_name(self):
        class_name_try_list = CRACK_FORM_FIELD_DICT["username"]["general_keywords"]
        for try_class_name in class_name_try_list:
            try:
                search_str = "//input[@class='{}']".format(try_class_name)
                web_elements = self._browser.find_elements_by_xpath(search_str)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find username input element by form.class_name: {}".format(try_class_name))
                        return web_element
            except Exception:
                continue
        logging.debug("cant find useful username input element by form.class_name")
        return None

    def find_input_box(self) -> Optional[WebElement]:
        func_list = [
            self._find_input_box_by_form_id,
            self._find_input_box_by_form_name,
            self._find_input_box_by_form_placeholder,
            self._find_input_box_by_form_class_name
        ]
        for func in func_list:
            web_element = func()
            if web_element is None:
                continue
            return web_element
        return None

    def fill_input_box(self, web_element, value=None) -> bool:
        if web_element is None:
            return False

        try:
            web_element.send_key(value)
            return True
        except Exception as e:
            logging.debug("fill input box failed, err={}".format(str(e)))
            return False
