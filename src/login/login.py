#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 4:35 PM
# @Author  : Liwenbin
# @File    : login.py.py
# @Project: WebSimulateLogin
import os
import uuid
import logging
import time
import traceback

from dto.browser import Browser
from src.login.form_filler.password_filler.password_filler import PasswordFiller
from src.login.form_filler.username_filler.username_filler import UsernameFiller
from src.login.form_filler.captcha_filler.captcha_filler import CaptchaFiller
from src.login.login_submitter.login_submitter import LoginSubmitter


class LoginController(object):

    def __init__(self):
        self._browser = Browser()
        self._username_filler = UsernameFiller(self._browser)
        self._password_filler = PasswordFiller(self._browser)
        self._captcha_filler = CaptchaFiller(self._browser)
        self._login_submitter = LoginSubmitter(self._browser)
        self._data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
        # 生成的截图放到data目录下
        if not os.path.exists(self._data_dir):
            os.mkdir(self._data_dir)

    def _close_page(self):
        time.sleep(1)
        self._browser.close()

    def _open_page(self, url):
        # 打开网址
        self._browser.open_page(url)

    def _fill_form(self, username, password):
        if self._username_filler.fill(username) is False:
            return False
        web_element = self._password_filler.fill(password)
        if web_element is False:
            return False

        # 无法获取验证码，可能该页面不需要验证码，尝试登录
        captcha_str = self._captcha_filler.recognize_captcha()
        if not captcha_str:
            return web_element

        captcha_element = self._captcha_filler.fill(captcha_str)

        return captcha_element if captcha_element else web_element

    def _submit_login(self, web_element):
        if self._login_submitter.login(web_element) is False:
            return False
        return True

    def _try_login(self, username, passwd):
        # 填写登录表单
        web_element = self._fill_form(username, passwd)
        if web_element is False:
            return False

        # 点击登录
        if self._submit_login(web_element) is False:
            return False

        # 如果还能找到用户名和密码的输入框，则认为登录失败
        username_input = self._username_filler.find_input_box()
        password_input = self._password_filler.find_input_box()
        if username_input or password_input:
            logging.info("debug 3")
            return False

        return True

    def pre_check(self, url):
        try:
            self._open_page(url)
            username_input = self._username_filler.find_input_box()
            password_input = self._password_filler.find_input_box()
            if not username_input and not password_input:
                return False
            return True
        except Exception:
            # logging.warning(traceback.format_exc())
            return False
        finally:
            self._close_page()

    def try_page_login(self, url, username, passwd):
        login_ret = False
        img_path = os.path.join(self._data_dir, str(uuid.uuid1()) + ".png")

        try:
            self._open_page(url)

            # 尝试登录
            if self._try_login(username, passwd) is True:
                login_ret = True
            else:
                # 可能有其他的登录方式，例如手机号登录、邮箱登录
                login_types_driver = self._browser.find_elements_by_link_text('登录')
                for one_driver in login_types_driver:
                    logging.debug("try login with method: {}".format(one_driver.accessible_name))
                    one_driver.click()
                    if self._try_login(username, passwd) is True:
                        login_ret = True
                        break

            self._browser.save_screenshot(img_path)
            logging.debug("save screenshot, url={} img_path={}".format(url, img_path))
        except Exception as e:
            logging.debug("login failed, url={} err={}".format(url, str(e)))
        finally:
            self._close_page()

        return login_ret, img_path


if __name__ == "__main__":
    pass
