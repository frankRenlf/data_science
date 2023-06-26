# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/6/26 22:49 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : ship
"""

import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen  # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/img.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
