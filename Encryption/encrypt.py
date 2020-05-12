# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 0:07
# @Author  : DannyDong
# @File    : encrypt.py
# @describe: 加密

import base64
import hashlib


class Encrypt(object):
    def __init__(self, wait_str):
        self.waiting_str = wait_str

    # Base64编码
    def base64_code(self):
        new_str = self.waiting_str.encode('utf-8')  # 需要转成bytes字节符
        new_str = base64.b64encode(new_str)
        print(new_str)

    # MD5加密（message-digest algorithm 5（信息-摘要算法））
    def md5_encrypt(self):
        # md5_obj = hashlib.md5()
        md5_obj = hashlib.md5(bytes('DDDDanny', encoding='utf-8'))  # 加盐后会在原md5加密上再进行一次加密
        md5_obj.update(self.waiting_str.encode('utf-8'))  # 需要转成bytes字节符
        print(md5_obj.hexdigest())


if __name__ == '__main__':
    ws = 'Waiting String'
    Encrypt(ws).base64_code()
    Encrypt(ws).md5_encrypt()
