# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/6/26 20:08 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""


def name_combine(first, last, middle='a'):
    return first + ((' ' + middle + ' ') if middle else ' ') + last
