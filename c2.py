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

if __name__ == "__main__":
    arr = np.array([1, 2, 3])
    print(type(arr))
    print(True == 1)
    x0 = {'a': 0, 'b': 1}
    for k, v in x0.items():
        print(k, v)
    x1 = [(k, v) for k, v in x0.items()]
    print(type(x1[0]))
