# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/6/26 20:50 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    # strange function
    # def __init__(self, methodName):
    #     super(TestAnonymousSurvey, self).__init__(methodName)
    #     question = "What language did you first learn to speak?"
    #     self.my_survey = AnonymousSurvey(question)
    #     self.responses = ['English', 'Spanish', 'Mandarin']

    def setUp(self):
        """ 创建一个调查对象和一组答案，供使用的测试方法使用 """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    # normal function
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
