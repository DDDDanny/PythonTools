# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 14:45
# @Author  : DannyDong
# @File    : txt_to_excel.py.py
# @describe: txt转Excel

import re
import xlwt


class TxtExcel(object):
    def __init__(self, filename, excel_path):
        self.data = []
        self.file = filename
        self.excel_path = excel_path
        self.excel_name = self.get_filename()
        self.read_txt()
        self.get_data()

    # 获取Excel文件名称（教材小节名称）
    def get_filename(self):
        with open(self.file, 'r', encoding='UTF-8') as f:
            name = f.readline()
            f.close()
            return name.split(']')[1].split('.')[0]

    # 读取并筛选txt
    def read_txt(self):
        with open(self.file, 'r', encoding='UTF-8') as f:
            file_data = f.read()
            # regular = r'(#\d\s[^#]+)'
            regular = r'(#[0-9]+\s[^#]+)'
            # 使用正则表达式匹配
            source_data = re.finditer(regular, file_data)
            f.close()
            return source_data

    # 拆分获取数据
    def get_data(self):
        source_data = self.read_txt()
        for data in source_data:
            self.data.append(data.group())
        return self.data

    # 写入Excel表
    def excel_write(self):
        book = xlwt.Workbook()
        sheet = book.add_sheet(self.excel_name)
        for row in range(len(self.data)):
            low = self.data[row].split('\n')
            i = 0
            for item in range(len(low)):
                if item != 0 and item != 2 and item != 3 and item != 4 and item != 5:
                    continue
                elif item == 3:
                    sheet.write(row, i, low[item].split('-')[0])
                    i += 1
                    sheet.write(row, i, low[item].split('-')[1])
                    i += 1
                else:
                    sheet.write(row, i, low[item])
                    i += 1
                print(low[item] + '----数据成功添加')
        book.save(self.excel_path+self.excel_name+'.xls')
        print('--------------------------\n 数据转换完成，已生成Excel表')
        print('文件地址为：'+self.excel_path + self.excel_name+'.xls')


if __name__ == '__main__':
    Txt_File = input('请输入TXT文件地址：')
    Excel_File = input('请输入存放Excel文件地址：')
    demo = TxtExcel(Txt_File, Excel_File)
    demo.excel_write()
