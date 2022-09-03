#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 4:28 PM
# @Author  : Liwenbin
# @File    : login_submitter.py.py
# @Project: WebSimulateLogin
import logging
import traceback

from dto.web_element import WebElement
from dto.browser import Browser
from conf.config import CRACK_FORM_FIELD_DICT


class LoginSubmitterError(Exception):

    def __init__(self, msg):
        super(LoginSubmitterError, self).__init__()
        self.message = "SubmitLogin: " + msg

    def __str__(self):
        return self.message


class LoginSubmitter(object):

    def __init__(self, browser):
        if not isinstance(browser, Browser):
            raise LoginSubmitterError("invalid browser, expected <dto.browser.Browser>")
        self._browser = browser

    def _find_and_submit_button_by_form_id(self):
        id_try_list = CRACK_FORM_FIELD_DICT["login_button"]["general_keywords"]
        for try_id in id_try_list:
            try:
                search_str = "//button[@id='{}']".format(try_id)
                self._browser.find_element_by_xpath(search_str).click()
                return True
            except Exception:
                continue
        logging.debug("cant find useful login button by form.id")
        return False

    def _find_and_submit_button_by_form_name(self):
        name_try_list = CRACK_FORM_FIELD_DICT["login_button"]["general_keywords"]
        for try_name in name_try_list:
            try:
                search_str = "//button[@name='{}']".format(try_name)
                self._browser.find_element_by_xpath(search_str).click()
                return True
            except Exception:
                continue
        logging.debug("cant find useful login button by form.name")
        return False

    def _find_and_submit_button_by_form_placeholder(self):
        placeholder_try_list = CRACK_FORM_FIELD_DICT["login_button"]["button_placeholder"]
        for try_placeholder in placeholder_try_list:
            try:
                search_str = "//button[@placeholder='{}']".format(try_placeholder)
                self._browser.find_element_by_xpath(search_str).click()
                return True
            except Exception:
                continue
        logging.debug("cant find useful login button by form.placeholder")
        return False

    def _find_and_submit_button_by_form_class_name(self):
        submit_name_try_list = CRACK_FORM_FIELD_DICT["login_button"]["button_placeholder"]
        class_name_try_list = CRACK_FORM_FIELD_DICT["login_button"]["general_keywords"]
        for try_name in class_name_try_list:
            try:
                search_str = "//button[@class='{}']".format(try_name)
                cls_names = self._browser.find_elements_by_xpath(search_str)
                for idx, cls_name in enumerate(cls_names):
                    if cls_name.accessible_name in submit_name_try_list:
                        # todo 只有这样才能点击成功，也不知道为什么
                        self._browser.find_elements_by_xpath(search_str)[idx].click()
                        if self._browser.alert_is_present():
                            break
            except Exception:
                # logging.warning(traceback.format_exc())
                continue
        logging.debug("cant find useful login button by form.class_name")
        return False

    def _login_by_other_web_element(self):
        func_list = [
            self._find_and_submit_button_by_form_id,
            self._find_and_submit_button_by_form_name,
            self._find_and_submit_button_by_form_class_name,
            self._find_and_submit_button_by_form_placeholder
        ]

        before_url = self._browser.current_url
        for func in func_list:
            if func() is True:
                break
        after_url = self._browser.current_url
        # 通过判断url，判断跳转是否成功。如果url变了，认为登录成功了
        if before_url != after_url:
            return True
        return False

    def _login_by_submit_web_element(self, web_element):
        try:
            before_url = self._browser.current_url
            if isinstance(web_element, WebElement):
                web_element.submit()
            after_url = self._browser.current_url
            # 通过判断url，判断跳转是否成功。如果url变了，认为登录成功了
            if before_url != after_url:
                return True
            return False
        except Exception:
            return False

    def login(self, web_element):
        if self._login_by_other_web_element() is True:
            return True
        # 尝试其他登录方式
        return self._login_by_submit_web_element(web_element)
