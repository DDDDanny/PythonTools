# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 17:04
# @Author  : DannyDong
# @File    : count_money.py
# @describe: 计算下午茶价格


class CountMoney(object):
    def __init__(self):
        self.num = int(input('请输入购买数量：'))
        self.price = []
        for i in range(self.num):
            self.price.append(float(input('请按顺序输入原价：')))
        self.actual_price = float(input('请输入实际支付总价：'))

    def calculation(self):
        sum_price = sum(self.price)
        for i in range(self.num):
            proportion = float(self.price[i] / sum_price)
            print('实际消费{:.2f}'.format(self.actual_price * proportion))


if __name__ == '__main__':
    demo = CountMoney()
    demo.calculation()
