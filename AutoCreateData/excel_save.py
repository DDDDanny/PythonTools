# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 1:42
# @Author  : DannyDong
# @File    : excel_save.py
# @describe: 保存Excel实现类

import xlrd

from xlutils.copy import copy

from AutoCreateData.base_data_create import BaseDataCreate


class ExcelSave(object):
    def __init__(self):
        pass

    @staticmethod
    def write_excel(data_list, excel, col):
        rb = xlrd.open_workbook(excel)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for x, v in enumerate(data_list, 1):
            y = col
            ws.write(x, y, v)
        wb.save(excel)


class DataInput(object):
    def __init__(self, cnt=1, excel=None):
        self.cnt = cnt
        self.Excel = excel

    def data_save(self):
        if self.Excel is None or self.Excel == '':
            raise Exception('Excel地址错误！')
        data = BaseDataCreate(self.cnt)
        ExcelSave().write_excel(data.create_name(), self.Excel, 1)
        ExcelSave().write_excel(data.create_sex(), self.Excel, 2)
        ExcelSave().write_excel(data.create_phone(), self.Excel, 3)
        ExcelSave().write_excel(data.create_course(), self.Excel, 4)
