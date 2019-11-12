# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 22:27
# @Author  : DannyDong
# @File    : calculated_amount.py
# @describe: 计算账本金额


from AccountBook.AccountBookCount.read_ini import ReadIni


class CalculatedAmount(object):
    def __init__(self, file_path):
        self.data = ReadIni(file_path)

    # 计算数据
    def calc_data(self):
        # 获取所有selections
        selections = self.data.get_sections()
        for i in range(len(selections)):
            print(selections[i])
            sum_data = 0
            # 获取selection下所有的keys
            keys = self.data.get_items(selections[i])
            for j in range(len(keys)):
                # 获取value
                value = self.data.get_value(selections[i], keys[j])
                sum_data = sum_data + float(value)
            print('本月消费总和：', sum_data)
            print('-----------------------------------------------')


if __name__ == '__main__':
    test = CalculatedAmount(r'D:\test.ini')
    test.calc_data()
