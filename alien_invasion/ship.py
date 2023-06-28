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
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.ai_settings = ai_settings
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        # left
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center_x -= self.ai_settings.ship_speed_factor
        # forward
        if self.moving_forward and self.rect.top > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor
        # backward
        if self.moving_backward and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center_x
        self.rect.bottom = self.center_y
