# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/6/21 13:50 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    x = np.linspace(-1, 1, 50)
    y = 2 * x + 1
    plt.plot(x, y)
