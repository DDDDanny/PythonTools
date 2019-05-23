# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 0:12
# @Author  : DannyDong
# @File    : csv_to_excel.py
# @describe: csv转excel

import pandas


def transformation():
    csv = pandas.read_csv('D://测试/001.csv', encoding='utf-8')
    csv.to_excel('D://测试/001.xlsx', sheet_name='data')


if __name__ == '__main__':
    transformation()
