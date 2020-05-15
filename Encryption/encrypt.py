# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 0:07
# @Author  : DannyDong
# @File    : encrypt.py
# @describe: 加密

import hmac
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
        return self

    # MD5加密（message-digest algorithm 5 信息-摘要算法）
    def md5_encrypt(self):
        # md5_obj = hashlib.md5()
        md5_obj = hashlib.md5(bytes('DDDDanny', encoding='utf-8'))  # 加盐后会在原md5加密上再进行一次加密
        md5_obj.update(self.waiting_str.encode('utf-8'))  # 需要转成bytes字节符
        print(md5_obj.hexdigest())
        return self

    # hmac加密（hex-based message authentication code 哈希消息认证码）
    def hmac_encrypt(self):
        salt = b'DDDDanny'
        hmac_obj = hmac.new(salt, self.waiting_str.encode('utf-8')).hexdigest()
        print(hmac_obj)
        print(hmac.compare_digest(hmac_obj, hmac_obj))  # 比较两个加密后的字符串是否一致 --> Bool
        return self

    # sha1加密（Secure Hash Algorithm 安全哈希算法）
    def sha1_encrypt(self):
        """
        sha1加密是基于MD5，加密后的数据会更长，相对于MD5会更加安全，但是运算速度会更慢
        """
        # sha1_obj = hashlib.sha1()
        sha1_obj = hashlib.sha1(bytes('DDDDanny', encoding='utf-8'))  # 加盐后会在原sha1加密上再进行一次加密
        sha1_obj.update(self.waiting_str.encode('utf-8'))  # 需要转成bytes字节符
        print(sha1_obj.hexdigest())


if __name__ == '__main__':
    ws = 'Waiting String'
    Encrypt(ws).base64_code()
    Encrypt(ws).md5_encrypt()
    Encrypt(ws).hmac_encrypt()
    Encrypt(ws).sha1_encrypt()
