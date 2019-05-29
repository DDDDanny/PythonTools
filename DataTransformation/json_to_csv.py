# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 20:52
# @Author  : DannyDong
# @File    : json_to_csv.py
# @describe: json格式转csv

import csv
import json


def transformation(json_file, csv_file):
    # 打开json文件
    json_file = open(json_file, 'r', encoding='utf8')

    # 解析json文件
    data_list = json.load(json_file)
    # print(data_list)

    # 获取键
    titles = list(data_list.keys())
    print(titles)

    data = []

    # 获取值
    for item in data_list.values():
        data.append(item)
        # print(item)
    print(data)

    titles1 = list(data[0][0].keys())
    print(titles1)

    data1 = []
    for dic1 in data[0]:
        for i in dic1.values():
            data1.append(i)
    print(data1)

    # 关闭连接
    json_file.close()

    # csv_file = open(csv_file, 'w', newline='', encoding='utf8')


if __name__ == '__main__':
    # transformation('D://测试/002.json', 'D://测试/001.csv')
    transformation('D://测试/001.json', 'D://测试/001.csv')
