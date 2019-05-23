# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 0:19
# @Author  : DannyDong
# @File    : excel_to_csv.py
# @describe: Excel转Csv

import pandas


def transformation():
    data_xls = pandas.read_excel('D://测试/001.xlsx', index_col=0)
    data_xls.to_csv('D://测试/001.csv', encoding='utf-8')


if __name__ == '__main__':
    transformation()
