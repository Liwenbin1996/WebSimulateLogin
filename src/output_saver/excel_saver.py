#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 6:13 PM
# @Author  : Liwenbin
# @File    : excel_saver.py.py
# @Project: WebSimulateLogin
import xlsxwriter
from dto.login_info import LoginInfo
from src.output_saver.base_saver import BaseSaver


class ExcelSaver(BaseSaver):

    def __init__(self, file_path):
        super(ExcelSaver, self).__init__()
        self._workbook = xlsxwriter.Workbook(file_path)
        self._sheet_writer = self._workbook.add_worksheet()
        self._write_row_idx = 0

    def save(self, login_info):
        if not isinstance(login_info, LoginInfo):
            raise TypeError("invalid login_info type, expected <LoginInfo>")

        extra_info = login_info.extra_info
        if self._write_row_idx == 0:
            col_n = 0
            for data_tuple in extra_info:
                self._sheet_writer.write(0, col_n, data_tuple[0])
                col_n += 1
            self._sheet_writer.write(0, col_n, "登录URL")
            col_n += 1
            self._sheet_writer.write(0, col_n, "登录是否成功")
            col_n += 1
            self._sheet_writer.write(0, col_n, "登录举证截图")
            self._write_row_idx += 1

        self._sheet_writer.set_row(self._write_row_idx, 200)
        self._sheet_writer.set_column(0, len(login_info.extra_info) + 2, 15)
        self._sheet_writer.set_column(len(login_info.extra_info) + 2, len(login_info.extra_info) + 3, 50)
        col_n = 0
        for data_tuple in extra_info:
            self._sheet_writer.write(self._write_row_idx, col_n, data_tuple[1])
            col_n += 1
        self._sheet_writer.write(self._write_row_idx, col_n, "\n".join(login_info.urls))
        col_n += 1
        self._sheet_writer.write(self._write_row_idx, col_n, login_info.login_status)
        col_n += 1
        img_option = {'x_scale': 0.13, 'y_scale': 0.13}
        self._sheet_writer.insert_image(self._write_row_idx, col_n, login_info.screenshot_path, img_option)
        self._write_row_idx += 1

    def close(self):
        self._workbook.close()


if __name__ == "__main__":
    from src.input_parser.excel_parser import ExcelParser

    test_parser = ExcelParser("../input_parser/test/test_input_excel.xlsx")
    test_ret = test_parser.parse()
    test_saver = ExcelSaver("test/test_output_excel.xlsx")
    for test_login_info in test_ret:
        test_saver.save(test_login_info)
    test_saver.close()
