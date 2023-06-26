# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/6/26 20:07 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from NameCombine import name_combine


class NameTest(unittest.TestCase):
    def test_name(self):
        formatted_name = name_combine('janis', 'joplin', 'a')
        self.assertEqual(formatted_name, 'janis joplin a')


# if __name__ == "__main__":
unittest.main()
