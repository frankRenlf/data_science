# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/7/9 10:47 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : csv
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt


def read_csv_attribute(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # for k, v in enumerate(header_row):
        #     print(k, v.strip())
        highs = []
        dates = []
        for row in reader:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            dates.append(current_date)
            highs.append(int(row[1]))
        # 根据数据绘制图形
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(dates, highs, c='red')
        # 设置图形的格式
        plt.title("Daily high temperatures, July 2014", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()


if __name__ == '__main__':
    file = '../dataset/sitka_weather_07-2014.csv'
    read_csv_attribute(file)
