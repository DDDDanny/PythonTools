# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:23
# @Author  : DannyDong
# @File    : ProConModel.py
# @describe: 生成者消费者模式

import queue
import time
import threading

new_queue = queue.Queue()
count = 0


# 生产者线程 当队列中产品数量小于100时就每隔1秒向队列放5个产品
class Producer(threading.Thread):
    def run(self):
        global new_queue, count
        while True:
            if new_queue.qsize() < 100:
                producer_list = []
                for y in range(5):
                    count = count + 1
                    new_queue.put(count)
                    producer_list.append(count)
                print("生产者生产了5个产品:{0}".format(producer_list))
            else:
                print('生产者线程等待中。。。')
            time.sleep(1)


# 消费者线程 当队列中产品数量大于50时就每隔1秒从队列中消费20个产品
class Consumer(threading.Thread):
    def run(self):
        global new_queue

        while True:
            if new_queue.qsize() > 50:
                consumer_list = []
                for k in range(20):
                    msg = new_queue.get()
                    consumer_list.append(msg)
                print("消费者消费了：{0}".format(consumer_list))
            else:
                print('消费者线程{0}等待中。。。'.format(self.name))
            time.sleep(1)


if __name__ == '__main__':
    # 先在消息队列中放入200个初始产品
    print("主线程放入初始产品:")
    for i in range(1, 201):
        count = count + 1
        new_queue.put(i)
        print(i, end=' ')
        if i % 25 == 0:
            print('\n')

    # 启动生产者线程
    p1 = Producer()
    p1.start()
    # p2 = Producer()
    # p2.start()

    # 启动消费者线程
    c1 = Consumer()
    c1.start()

    # 在主线程中，每隔1秒打印队列中产品剩余情况
    while True:
        print('\n----------------队列中还有{0}个产品-----------\n'.format(new_queue.qsize()))
        time.sleep(1)
