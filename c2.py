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
import collections

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import json


def cg(x, **arr):
    arr['dict0']['b'] = 5


class Animal:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return str(self.age)


def json_add(arr):
    with open('dataset/json_data.txt', 'w') as jd:
        json.dump(arr, jd)


def json_load(dataset: str):
    with open('dataset/json_data.txt', 'r+') as jd:
        s = json.load(jd)
    try:
        data = s[dataset]
        print(data)
    except KeyError:
        print('No such dataset')
        s[dataset] = input('please enter data')
        json_add(s)


if __name__ == "__main__":
    dog1 = Dog('111', 11)
    dog1.print()
