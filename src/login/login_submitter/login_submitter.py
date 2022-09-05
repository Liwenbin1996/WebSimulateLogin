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

    def _find_button_by_form_id(self):
        return self._find_and_submit_button_by_form_id(submit=False)

    def _find_and_submit_button_by_form_id(self, submit=True):
        id_try_list = CRACK_FORM_FIELD_DICT["login_button"]["general_keywords"]
        for try_id in id_try_list:
            try:
                search_str = "//button[@id='{}']".format(try_id)
                if submit:
                    self._browser.find_element_by_xpath(search_str).click()
                    return True
                else:
                    button_element = self._browser.find_element_by_xpath(search_str)
                    if button_element:
                        return button_element
            except Exception:
                continue
        logging.debug("cant find useful login button by form.id")
        return False

    def _find_button_by_form_name(self):
        return self._find_and_submit_button_by_form_name(submit=False)

    def _find_and_submit_button_by_form_name(self, submit=True):
        name_try_list = CRACK_FORM_FIELD_DICT["login_button"]["general_keywords"]
        for try_name in name_try_list:
            try:
                search_str = "//button[@name='{}']".format(try_name)
                if submit:
                    self._browser.find_element_by_xpath(search_str).click()
                    return True
                else:
                    button_element = self._browser.find_element_by_xpath(search_str)
                    if button_element:
                        return button_element
            except Exception:
                continue
        logging.debug("cant find useful login button by form.name")
        return False

    def _find_button_by_form_placeholder(self):
        return self._find_and_submit_button_by_form_placeholder(submit=False)

    def _find_and_submit_button_by_form_placeholder(self, submit=True):
        placeholder_try_list = CRACK_FORM_FIELD_DICT["login_button"]["button_placeholder"]
        for try_placeholder in placeholder_try_list:
            try:
                search_str = "//button[@placeholder='{}']".format(try_placeholder)
                if submit:
                    self._browser.find_element_by_xpath(search_str).click()
                    return True
                else:
                    button_element = self._browser.find_element_by_xpath(search_str)
                    if button_element:
                        return button_element
            except Exception:
                continue
        logging.debug("cant find useful login button by form.placeholder")
        return False

    def _find_button_by_form_class_name(self):
        return self._find_and_submit_button_by_form_class_name(submit=False)

    def _find_and_submit_button_by_form_class_name(self, submit=True):
        submit_name_try_list = CRACK_FORM_FIELD_DICT["login_button"]["button_placeholder"]
        class_name_try_list = CRACK_FORM_FIELD_DICT["login_button"]["general_keywords"]
        for try_name in class_name_try_list:
            try:
                search_str = "//button[@class='{}']".format(try_name)
                cls_names = self._browser.find_elements_by_xpath(search_str)
                for idx, cls_name in enumerate(cls_names):
                    if cls_name.accessible_name in submit_name_try_list:
                        # todo 只有这样才能点击成功，也不知道为什么
                        if submit:
                            self._browser.find_elements_by_xpath(search_str)[idx].click()
                            if self._browser.alert_is_present():
                                return True
                            # return True
                        else:
                            button_element = self._browser.find_elements_by_xpath(search_str)[idx].click()
                            if button_element:
                                return button_element
            except Exception:
                # logging.warning(traceback.format_exc())
                continue
        logging.debug("cant find useful login button by form.class_name")
        return False

    def _judge_login_status(self, before_url, after_url):
        # 如果登录前后url都一样，则认为登录失败
        if before_url == after_url:
            logging.info("debug 1")
            return False

        # 如果登录后url仍然存在login字样，则认为登录失败
        if "login" in str(after_url).lower():
            logging.info("debug 2")
            return False

        # func_list = [
        #     self._find_button_by_form_id,
        #     self._find_button_by_form_name,
        #     self._find_button_by_form_class_name,
        #     self._find_button_by_form_placeholder
        # ]
        #
        # # 如果登录后url仍然可以找到登录按钮，则认为登录失败
        # for func in func_list:
        #     if func():
        #         return False

        return True

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

        return self._judge_login_status(before_url, after_url)

    def _login_by_submit_web_element(self, web_element):
        try:
            before_url = self._browser.current_url
            if isinstance(web_element, WebElement):
                web_element.submit()
            after_url = self._browser.current_url
            return self._judge_login_status(before_url, after_url)
        except Exception:
            return False

    def login(self, web_element):
        if self._login_by_other_web_element() is True:
            return True
        # 尝试其他登录方式
        return self._login_by_submit_web_element(web_element)
