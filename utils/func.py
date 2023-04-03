# _*_ coding: utf-8 _*_
# @Time : 2021/8/13 10:32
# @File : utils.py
# @Software: PyCharm

import os
import time
import datetime
import shutil


def get_file_create_time(path):
    """
    获取文件创建时间
    """
    timestamp = os.path.getctime(path)          # 创建时间的获取
    print("time_create_timestamp: ", timestamp, type(timestamp))
    convert = time.localtime(timestamp)
    print("time_create_convert: ", convert, type(convert))
    return time.strftime('%Y-%m-%d %H:%M:%S', convert)


def get_file_modify_time(path):
    """
    获取文件修改时间
    """
    timestamp = os.path.getmtime(path)      # 修改时间的获取
    convert = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', convert)


def remove_files(path, now_time, day=3):
    """
    遍历文件夹及其子文件夹中的文件，并存删除里面过期的文件
    :param path: 输入文件夹路径
    :param now_time: 过期时间
    :return:
    """
    if os.path.isfile(path):
        file_modify_time = get_file_modify_time(path)
        struct_file_modify_time = datetime.datetime.strptime(file_modify_time, '%Y-%m-%d %H:%M:%S')
        three_day_time = struct_file_modify_time + datetime.timedelta(days=day)
        if three_day_time < now_time:  # 过期了，执行下面删除逻辑
            os.remove(path)
    elif os.path.isdir(path):
        folder = os.listdir(path)
        if len(folder) == 0:
            shutil.rmtree(path)
        else:
            for each in folder:
                new_path = os.path.join(path, each)
                remove_files(new_path, now_time, day=day)
