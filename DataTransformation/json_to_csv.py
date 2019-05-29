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
    # 获取键
    titles = data_list[0].keys()
    # 获取值
    data = [dic.values() for dic in data_list]
    # 关闭json文件的连接
    json_file.close()
    # 打开csv文件，没有则新建
    csv_file = open(csv_file, 'w', newline='', encoding='utf8')
    # 创建csv写入器
    csv_writer = csv.writer(csv_file)
    # 写入数据
    csv_writer.writerow(titles)
    csv_writer.writerows(data)
    # 关闭csv文件的连接
    csv_file.close()


if __name__ == '__main__':
    # transformation('D://测试/002.json', 'D://测试/001.csv')
    transformation('D://测试/001.json', 'D://测试/001.csv')
