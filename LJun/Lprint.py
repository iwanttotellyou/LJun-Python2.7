# coding:utf-8
import chardet
import codecs
import time
import sys

"""
格式：\033[显示方式;前景色;背景色m

说明：
前景色            背景色           颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              紫红色
36                46              青蓝色
37                47              白色
显示方式           意义
-------------------------
0                终端默认设置
1                高亮显示
4                使用下划线
5                闪烁
7                反白显示
8                不可见
"""


class MustDict(Exception):
    pass


def invincible_decode(decode_content):
    """
    依赖 chardet codecs 将任意编码转换成unicode
    :param decode_content:
    :return:
    """
    if isinstance(decode_content, str) and decode_content != '':
        charset = chardet.detect(decode_content)['encoding']
        decode_content = codecs.decode(decode_content, charset)
    return decode_content


def print_time(*kwargs):
    """
    带时间,自定义输出内容
    :param kwargs:
    :return:
    """
    content = ''
    for i in kwargs:
        i = invincible_decode(i)
        content = u'{content} {i}'.format(content=content, i=i)
    print u'\033[1;36;0m[{time}]\033[0m {content}'.format(time=time.ctime(), content=content)


def print_error(*kwargs):
    """
    带时间,输出错误信息
    :param kwargs:
    :return:
    """
    if kwargs == ():
        if sys.exc_info()[1] is None:
            print_error("no error")
            return "awesome"
        print_error(sys.exc_info()[1])
        return "aweful"
    content = ''
    for i in kwargs:
        i = invincible_decode(i)
        content = u'{content} {i}'.format(content=content, i=i)
    print u'\033[1;33;0m[{time}]\033[0m {content}'.format(time=time.ctime(), content=content)


def has_keys(detect_dict, *keys):
    """
    判断dict是否完全存在key
    :param detect_dict:
    :param keys:
    :return:
    """
    if isinstance(detect_dict, dict):
        for i in keys:
            if i not in detect_dict:
                print_error("wrong key " + i)
                return False
        return True
    raise MustDict
