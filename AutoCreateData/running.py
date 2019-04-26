# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 2:05
# @Author  : DannyDong
# @File    : running.py
# @describe: 程序入口

from AutoCreateData.excel_save import DataInput


user_type = int(input('请输入导入类型（若需要导入超级用户，输入666）：'))
cnt = int(input('请输入人数：'))
# Excel_File = 'E://004.xlsx'
Excel_File = input('请输入Excel文件地址：')
DataInput(cnt, Excel_File, user_type).data_save()
