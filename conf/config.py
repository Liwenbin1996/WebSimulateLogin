#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 7:55 PM
# @Author  : Liwenbin
# @File    : config.py.py
# @Project: WebSimulateLogin

CRACK_FORM_FIELD_DICT = {
    "username": {
        "general_keywords": [
            "username", "userName", "UserName", "USERNAME", "user_name",
            "login", "Login", "LOGIN",
            "textuname", "TEXTUNAME", "textUname", "text_uname", "TextUname",
            "login_username", "loginUsername", "LoginUsername", "loginusername", "LOGINUSERNAME",
            "loginName", "LoginName", "loginname", "LOGINNAME",
            "input_username", "inputUsername", "InputUsername", "INPUTUSERNAME",
            "user", "User", "USER",
            "name", "Name", "NAME",
            "zhanghao", "ZhangHao", "ZHANGHAO", "zhang_hao",
            "yonghu", "YongHu", "YONGHU", "yong_hu", "yongHu",
            "email", "Email", "EMAIL",
            "account", "Account", "ACCOUNT",
            "telephone", "Telephone", "TELEPHONE",
            "shou_ji", "shouji", "ShouJi", "shouJi", "SHOUJI",
            "shou_ji_hao", "shoujihao", "shouJiHao", "ShouJiHao", "SHOUJIHAO",
            "zhang_hu", "zhanghu", "ZhangHu", "zhangHu", "ZHANGHU",
            "uname", "UNAME", "uName",
            "phone", "Phone", "PHONE"
        ],
        # "text_class_name": ["username", "login", "login_username", "loginName", "user", "name", "zhanghao", "yonghu",
        #                     "email", "account", "telephone", "shouji", "shoujihao", "zhanghu"],
        "text_placeholder": [
            "账户", "请输入账户", "请输入您的账户", "请输入你的账户",
            "账号", "请输入账号", "请输入您的账号", "请输入你的账号",
            "用户", "请输入用户", "请输入您的用户", "请输入你的用户",
            "用户名", "请输入用户名", "请输入您的用户名", "请输入你的用户名",
            "手机", "请输入手机", "请输入您的手机", "请输入你的手机",
            "手机号", "请输入手机号", "请输入您的手机号", "请输入你的手机号",
            "身份证", "请输入身份证", "请输入您的身份证", "请输入你的身份证",
            "身份证号", "请输入身份证号" "请输入您的身份证号", "请输入你的身份证号",
        ]
    },
    "password": {
        "general_keywords": [
            "password", "PASSWORD", "Password",
            "login_password", "loginPassword", "LoginPassword", "LOGINPASSWORD",
            "mima", "MiMa" "miMa", "MIMA", "mi_ma",
            "PASSWD", "passwd", "Passwd",
        ],
        # "text_class_name": ["password", "login_password", "loginPassword", "mima", "miMa", "mi_ma"],
        "text_placeholder": [
            "密码", "密 码", "请输入密码", "请输入您的密码", "请输入你的密码",
        ]
    },
    "login_button": {
        "general_keywords": [
            "登录", "登 录",
            "确定", "确 定",
            "login", "Login", "LOGIN",
            "login_submit", "loginSubmit", "LoginSubmit",
            "btnLogin", "btn_login", "BtnLogin",
            "login-btn", "login_btn", "loginBtn", "LoginBtn",
            "login-button", "login_button", "loginButton", "LoginButton",
            "sub_btn", "subBtn", "SubBtn", "SUBBTN",
            "submit", "Submit", "SUBMIT",
            "submit_button", "submitButton", "SubmitButton", "SUBMIT_BUTTON", "SUBMITBUTTON",
            "sureMit", "SureMit", "sureMit", "sure_mit", "SUREMIT",
        ],
        # "button_class_name": ["sub_btn", "submit", "submit_button"],
        "button_placeholder": [
            "登录", "登 录",
            "确定", "确 定",
            "login", "Login", "LOGIN",
        ]
    },
    "captcha": {
        "general_keywords": [
            "yzm", "YZM",
            "yanzhengma" "yan_zheng_ma" "yanZhengMa" "YANZHENGMA",
            "verifycode", "verifyCode", "verify_code", "VerifyCode", "VERIFYCODE",
            "login.VerifyCode", "login.verify_code", "login.verifyCode",
            "validateCode", "validate_code", "ValidateCode", "VALIDATE_CODE",
            "code", "Code", "CODE",
            "login_code", "loginCode", "LoginCode", "LOGINCODE", "LOGIN_CODE",
            "seccode", "secCode", "SecCode", "SEC_CODE",
            "checkCode", "CheckCode", "CHECK_CODE", "check_code",
            "authcode", "auth_code", "authCode", "AuthCode",
        ],
        # "text_class_name": ["yzm", "verifyCode", "VerifyCode", "login.VerifyCode"],
        "text_placeholder": [
            "验证码", "请输入验证码",
        ]
    },
    "captcha_img": {
        "general_keywords": [
            "yzm", "YZM",
            "yanzhengma" "yan_zheng_ma" "yanZhengMa" "YANZHENGMA",
            "verifycode", "verifyCode", "verify_code", "VerifyCode", "VERIFYCODE",
            "login.VerifyCode", "login.verify_code", "login.verifyCode",
            "validateCode", "validate_code", "ValidateCode", "VALIDATE_CODE",
            "code", "Code", "CODE",
            "login_code", "loginCode", "LoginCode", "LOGINCODE", "LOGIN_CODE",
            "seccode", "secCode", "SecCode", "SEC_CODE",
            "VerifyCodeImg", "verifyCodeImg", "VERIFY_CODE_IMG", "verify_code_img",
            "mid validateCode",
            "code_img", "codeImg", "CodeImg", "CODE_IMG", "codeimg",
            "seccodesrc", "secCodeSrc", "SecCodeSrc", "SEC_CODE_SRC",
            "imgLoginCheckCode", "ImgLoginCheckCode", "img_login_check_code",
            "checkCode", "CheckCode", "CHECK_CODE", "check_code",
            "authcode", "auth_code", "authCode", "AuthCode",
        ]
    }
}

URL_REGEX = "((ht|f)tps?):\/\/[\w\-]+(\.[\w\-]+)+([\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?"
