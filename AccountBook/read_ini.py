# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 21:57
# @Author  : DannyDong
# @File    : read_ini.py
# @describe: 读取配置文件

import os
import configparser


class ReadIni(object):
    # 构造函数
    def __init__(self, file_name=None):
        # 获取当前目录的绝对路径
        cur_path = os.path.abspath(__file__)
        # 获取配置文件的绝对路径
        if file_name is None:
            file_name = os.path.join(
                os.path.abspath(os.path.dirname(cur_path) + os.path.sep + '../Config'), 'Ele_config.ini'
            )
        else:
            file_name = os.path.join(
                os.path.abspath(os.path.dirname(cur_path) + os.path.sep + '../Config'), file_name
            )

        # if node is None:
        #     self.node = 'SearchInfo'
        # else:
        #     self.node = node

        self.conf = self.load_ini(file_name)

    # 加载文件
    @staticmethod
    def load_ini(file_name):
        conf = configparser.ConfigParser()
        conf.read(file_name, encoding='utf-8')
        return conf

    # 获取节点名称
    def get_sections(self):
        data = self.conf.sections()
        return data

    # 获取节点下所有的key
    def get_items(self, selection):
        data = self.conf.options(selection)
        return data

    # 获取Value值
    def get_value(self, node, key):
        data = self.conf.get(node, key)
        return data


if __name__ == '__main__':
    read = ReadIni(r'D:\test.ini')
    # read = ReadIni('Sys_config.ini', 'Base')
    print(read.get_sections())
    print(read.get_items('node1'))
