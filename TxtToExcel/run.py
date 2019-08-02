# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 16:49
# @Author  : DannyDong
# @File    : run.py
# @describe: 程序运行主入口

from TxtToExcel.txt_to_excel import TxtExcel

import_type = int(input('是否为批量导入（1是0否）：'))
# 非批量导入
if import_type == 0:

    Txt_File = input('请输入TXT文件地址：')
    Excel_File = input('请输入存放Excel文件地址：')
    TxtExcel(Txt_File, Excel_File).excel_write()
# 批量导入
elif import_type == 1:

    Txt_File = input('请输入批量导入TXT文件地址：')
    Excel_File = input('请输入存放Excel文件地址：')

    with open(Txt_File, 'r') as f:
        file_suite = f.readlines()

        for item in range(len(file_suite)):
            TxtExcel(file_suite[item].split('\n')[0], Excel_File).excel_write()
# 异常
else:
    raise ValueError('选择导入类型输入错误！！！')
