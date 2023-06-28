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


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.name)

    ship = Ship(ai_settings, screen)
    while True:
        gf.check_events(ship)

        ship.update()

        gf.update_screen(ai_settings, screen, ship)


if __name__ == "__main__":
    run_game()
