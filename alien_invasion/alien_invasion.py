# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : data_science 
    @Product : PyCharm
    @createTime : 2023/6/26 22:40 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : main
"""

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))

    pygame.display.set_caption(ai_settings.name)

    bullets = Group()

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update(bullets)
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == "__main__":
    run_game()
