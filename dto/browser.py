#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 5:09 PM
# @Author  : Liwenbin
# @File    : browser.py.py
# @Project: WebSimulateLogin
from selenium import webdriver
from selenium.webdriver.common.by import By
from dto.web_element import WebElement
from selenium.common.exceptions import NoAlertPresentException


class Browser(object):

    def __init__(self):
        self._browser = webdriver.Chrome()

    def open_page(self, url):
        self._browser.get(url)

    def close(self):
        self._browser.close()

    def find_element_by_name(self, value):
        element = self._browser.find_element(By.NAME, value)
        if element:
            return WebElement(element)
        return None

    def find_elements_by_name(self, value):
        elements = self._browser.find_elements(By.NAME, value)
        if elements:
            return [WebElement(element) for element in elements]
        return []

    def find_element_by_class_name(self, value):
        element = self._browser.find_element(By.CLASS_NAME, value)
        if element:
            return WebElement(element)
        return None

    def find_elements_by_class_name(self, value):
        elements = self._browser.find_elements(By.CLASS_NAME, value)
        if elements:
            return [WebElement(element) for element in elements]
        return []

    def find_element_by_placeholder(self, value):
        search_str = "//input[@placeholder='{}']".format(value)
        element = self._browser.find_element(By.XPATH, search_str)
        if element:
            return WebElement(element)
        return None

    def find_elements_by_placeholder(self, value):
        search_str = "//input[@placeholder='{}']".format(value)
        elements = self._browser.find_elements(By.XPATH, search_str)
        if elements:
            return [WebElement(element) for element in elements]
        return []

    def find_element_by_type(self, value):
        search_str = "//input[@type='{}']".format(value)
        element = self._browser.find_element(By.XPATH, search_str)
        if element:
            return WebElement(element)
        return None

    def find_elements_by_type(self, value):
        search_str = "//input[@type='{}']".format(value)
        elements = self._browser.find_elements(By.XPATH, search_str)
        if elements:
            return [WebElement(element) for element in elements]
        return []

    def find_element_by_link_text(self, value):
        element = self._browser.find_element(By.PARTIAL_LINK_TEXT, value)
        if element:
            return WebElement(element)
        return None

    def find_elements_by_link_text(self, value):
        elements = self._browser.find_elements(By.PARTIAL_LINK_TEXT, value)
        if elements:
            return [WebElement(element) for element in elements]
        return []

    def find_element_by_xpath(self, value):
        element = self._browser.find_element(By.XPATH, value)
        if element:
            return WebElement(element)
        return None

    def find_elements_by_xpath(self, value):
        elements = self._browser.find_elements(By.XPATH, value)
        if elements:
            return [WebElement(element) for element in elements]
        return []

    def save_screenshot(self, filename):
        # return self._browser.get_screenshot_as_file(filename)
        return self._browser.save_screenshot(filename)

    def alert_is_present(self):
        try:
            alert = self._browser.switch_to.alert.text
            if alert:
                return True
        except NoAlertPresentException:
            return False

    @property
    def current_url(self):
        return self._browser.current_url
