# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/6/21 13:50 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : practice
    @Description : practice
"""
import matplotlib.pyplot as plt
import numpy as np


def cg(x, *arr):
    arr[1]['b'] = 5
    print(x)
    print('------')
    print(arr)


if __name__ == "__main__":
    arr0 = [1, 2, 3]
    dict0 = {'a': 1, 'b': "str"}
    cg(1, arr0, dict0)
