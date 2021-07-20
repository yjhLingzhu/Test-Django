# _*_ coding: utf-8 _*_
# @Time : 2021/5/20 10:34
# @File : test.py
# @Author : yjh
# @Software: PyCharm

import logging
from Test_Django.settings import BASE_DIR
import os
import base64
import random

# format = "[%(asctime)s][%(levelname)s]""[%(filename)s:%(lineno)d][%(message)s]"
# logger = logging.basicConfig(filename=os.path.join(BASE_DIR, "logs", "chacewang_info.log"), level=logging.INFO, format=format)
#
# a = {"a": 1}
# print(a["a"])
#
# b_list = "123456 "
# print(b_list)
# print(b_list[0:-1])
#
# logging.info("试一下..")
def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

# s = "年好呀"
# a = "1"
# a = a + "_" + generate_random_str()
# en = base64.b64encode(str(a).encode())
# print(en)
# print(base64.b64decode(en).decode())

a = "RegisterArea_HNDQ_Guangdong_GuangZhou_LW"
print(a.lower())