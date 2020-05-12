# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 0:07
# @Author  : DannyDong
# @File    : decrypt.py
# @describe: 解密

import base64


class Decrypt(object):
    def __init__(self, wait_str):
        self.waiting_str = wait_str

    # Base64编码
    def base64_code(self):
        new_str = self.waiting_str.encode('utf-8')  # 需要转成bytes字节符
        new_str = base64.b64decode(new_str)
        print(new_str)

    # MD5解密（message-digest algorithm 5（信息-摘要算法））
    def md5_decrypt(self):
        # MD5加密后，不可逆
        pass


if __name__ == '__main__':
    ws = 'V2FpdGluZyBTdHJpbmc='
    Decrypt(ws).base64_code()
