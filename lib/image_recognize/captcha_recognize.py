#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 10:43 AM
# @Author  : Liwenbin
# @File    : captcha_recognize.py
# @Project: WebSimulateLogin
from lib.image_recognize.src import ocr


class CaptchaRecognizerError(Exception):

    def __init__(self, msg):
        super(CaptchaRecognizerError, self).__init__()
        self.message = "CaptchaRecognizer: " + msg

    def __str__(self):
        return self.message


class CaptchaRecognizer(object):

    def __init__(self):
        self._ocr_engine = ocr.DdddOcr()

    def image_to_string(self, image_path=None, image_bytes=None):
        if not image_path and not image_bytes:
            raise CaptchaRecognizerError("invalid parameter, image_path and image_bytes cant all be empty")

        if image_path:
            if not isinstance(image_path, str):
                raise CaptchaRecognizerError("invalid image_path type, expected <str>")
            with open(image_path, 'rb') as f:
                img_bytes = f.read()
            return self._ocr_engine.classification(img_bytes)

        if image_bytes:
            if not isinstance(image_bytes, str):
                raise CaptchaRecognizerError("invalid image_bytes type, expected <str>")
            return self._ocr_engine.classification(image_bytes)


if __name__ == "__main__":
    print(CaptchaRecognizer().image_to_string("/Users/wenbin/Desktop/validateCodeServlet.jpeg"))
