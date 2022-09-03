#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 7:31 PM
# @Author  : Liwenbin
# @File    : captcha_filler.py.py
# @Project: WebSimulateLogin

import logging

from typing import Optional
from dto.web_element import WebElement
from conf.config import CRACK_FORM_FIELD_DICT
from src.login.form_filler.base_filler import BaseFiller
from lib.image_recognize.captcha_recognize import CaptchaRecognizer


class CaptchaFiller(BaseFiller):

    def __init__(self, browser):
        super(CaptchaFiller, self).__init__(browser)

    def _find_input_box_by_form_placeholder(self):
        placeholder_try_list = CRACK_FORM_FIELD_DICT["captcha"]["text_placeholder"]
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

    def _find_input_box_by_form_name(self):
        name_try_list = CRACK_FORM_FIELD_DICT["captcha"]["general_keywords"]
        for try_name in name_try_list:
            try:
                search_str = "//input[@name='{}']".format(try_name)
                web_elements = self._browser.find_elements_by_xpath(search_str)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find captcha input element by form.name: {}".format(try_name))
                        return web_element
            except Exception:
                continue
        logging.debug("cant find useful captcha input element by form.name")
        return None

    def _find_input_box_by_form_class_name(self):
        class_name_try_list = CRACK_FORM_FIELD_DICT["captcha"]["general_keywords"]
        for try_class_name in class_name_try_list:
            try:
                search_str = "//input[@class='{}']".format(try_class_name)
                web_elements = self._browser.find_elements_by_xpath(search_str)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find captcha input element by form.class_name: {}".format(try_class_name))
                        return web_element
            except Exception:
                continue
        logging.debug("cant find useful captcha input element by form.class_name")
        return None

    def _find_captcha_by_form_id(self):
        id_try_list = CRACK_FORM_FIELD_DICT["captcha_img"]["general_keywords"]
        for try_id in id_try_list:
            try:
                search_str = "//img[@id='{}']".format(try_id)
                web_elements = self._browser.find_elements_by_xpath(search_str)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find captcha img element by form.id: {}".format(try_id))
                        return web_element
            except Exception:
                continue
        logging.debug("cant find useful captcha img element by form.id")
        return None

    def _find_captcha_by_form_class_name(self):
        class_try_list = CRACK_FORM_FIELD_DICT["captcha_img"]["general_keywords"]
        for try_class in class_try_list:
            try:
                search_str = "//img[@class='{}']".format(try_class)
                web_elements = self._browser.find_elements_by_xpath(search_str)
                for web_element in web_elements:
                    if web_element and web_element.is_display() is True:
                        logging.debug("find captcha img element by form.class: {}".format(try_class))
                        return web_element
            except Exception:
                # logging.warning(traceback.format_exc())
                continue
        logging.debug("cant find useful captcha img element by form.class")
        return None

    def recognize_captcha(self) -> str:
        func_list = [
            self._find_captcha_by_form_id,
            self._find_captcha_by_form_class_name
        ]

        img_element = None
        for func in func_list:
            web_element = func()
            if web_element:
                img_element = web_element
                break

        if not img_element:
            return ""

        img_element.screenshot("codeImg.png")

        try:
            img_str = CaptchaRecognizer().image_to_string("codeImg.png")
            logging.debug("recognizer captcha: {}".format(img_str))
            return img_str
        except Exception as e:
            logging.debug("recognizer captcha failed, err={}".format(str(e)))
            return ""

    def find_input_box(self) -> Optional[WebElement]:
        func_list = [
            self._find_input_box_by_form_name,
            self._find_input_box_by_form_class_name,
            self._find_input_box_by_form_placeholder
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


if __name__ == "__main__":
    from dto.browser import Browser
    test_browser = Browser()
    test_browser.open_page("https://oa.cdtu.edu.cn/seeyon/index.jsp")
    test_captcha_filler = CaptchaFiller(test_browser)
    print(test_captcha_filler.recognize_captcha())
