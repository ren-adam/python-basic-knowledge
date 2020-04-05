#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time: 2020-03-22 00:11
# @Project: python-basic-knowledge
# @Version: 2020.03 builder 220011
# @Author: Adam Ren
# @Email: adam_ren@sina.com
# @Github: https://github.com/ren-adam/python-basic-knowledge
# @Site: http://renpeter.com
# @File : find_prime_number_in_range.py
# @Software: PyCharm
#


"""
一个做着测试的东西
"""
import sys


def find_prime_number_in_range(range_start, range_end):
    """
    计算在指定范围内的质数
    :param range_start:
    :param range_end:
    :return: 计算结果列表
    """

    # 检查数据的合法性
    if range_start < 2:
        range_start = 2
    if range_end < 2:
        range_end = 2

    start = min(range_start, range_end)
    end = max(range_start, range_end) + 1

    prime_number_list = []
    for i in range(start, end):
        prime_flag = True
        for j in prime_number_list:
            div, mode = divmod(i, j)
            if mode == 0 and i != j and j != 1:
                prime_flag = False
                break
        if prime_flag:
            prime_number_list.append(i)
    return prime_number_list


start = 1000
end = 1
print('wait to find prime number(s) between {} to {}'.format(start, end))
result = find_prime_number_in_range(start, end)
print()
print('from {} to {}, there are {} prime numbers'.format(start, end, len(result)))
print(result)
