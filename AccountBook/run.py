# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 21:55
# @Author  : DannyDong
# @File    : run.py
# @describe: 脚本执行文件

from AccountBook.AccountBookCount.calculated_amount import CalculatedAmount as ca


file_path = input('请输入InI文件地址：')

print(ca(file_path).calc_data())
