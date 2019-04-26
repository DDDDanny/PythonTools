# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 1:42
# @Author  : DannyDong
# @File    : excel_save.py
# @describe: 保存Excel实现类

import xlrd
import openpyxl
from xlutils.copy import copy

from AutoCreateData.base_data_create import BaseDataCreate


class ExcelSave(object):
    def __init__(self):
        pass

    # 删除工作表（暂时不用）
    @staticmethod
    def clear_data(excel):
        work_book = openpyxl.load_workbook(excel)
        work_book.remove_sheet(work_book.get_sheet_by_name('Sheet1'))
        work_book.create_sheet('Sheet1', 0)
        work_book.save(excel)

    @staticmethod
    def write_excel(data_list, excel, col):
        # self.clear_data(excel)
        rb = xlrd.open_workbook(excel)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for x, v in enumerate(data_list, 1):
            y = col
            ws.write(x, y, v)
        wb.save(excel)


class DataInput(object):
    def __init__(self, cnt=1, excel=None, user_type=0):
        self.cnt = cnt
        self.Excel = excel
        self.type = user_type

    def data_save(self):
        """
            添加新字段写在这里：
                样例：ExcelSave().write_excel(数据, Excel文件地址, 列数)
        """
        if self.Excel is None or self.Excel == '':
            raise Exception('Excel文件地址错误！')
        data = BaseDataCreate(self.cnt)
        ExcelSave().write_excel(data.create_name(), self.Excel, 1)
        ExcelSave().write_excel(data.create_sex(), self.Excel, 2)
        ExcelSave().write_excel(data.create_phone(self.type), self.Excel, 3)
        ExcelSave().write_excel(data.create_course(), self.Excel, 4)
