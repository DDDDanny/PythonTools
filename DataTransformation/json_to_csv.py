# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 20:52
# @Author  : DannyDong
# @File    : json_to_csv.py
# @describe: json格式转csv

import csv
import json


def transformation(json_file, csv_file):
    json_file = open(json_file, 'r', encoding='utf8')
    csv_file = open(csv_file, 'w', newline='', encoding='utf8')
    keys = []
    writer = csv.writer(csv_file)

    json_data = json_file.read()
    dic_data = json.loads(json_data, encoding='utf8')

    for dic in dic_data:
        keys = dic.keys()
        writer.writerow(keys)
        break

    for dic in dic_data:
        for key in keys:
            if key not in dic:
                dic[key] = ''
        writer.writerow(dic.values())
    json_file.close()
    csv_file.close()


if __name__ == '__main__':
    transformation('D://测试/001.json', 'D://测试/001.csv')
