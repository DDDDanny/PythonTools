# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 2:05
# @Author  : DannyDong
# @File    : running.py
# @describe: 程序入口

from AutoCreateData.excel_save import DataInput


num = int(input('请输入人数：'))
Excel_File = ''
DataInput(num, Excel_File).data_save()
