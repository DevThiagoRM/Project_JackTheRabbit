#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            player_score = 0  # PLAYER SCORE
            # score = Score(self.window)

            # SHOW MENU
            menu = Menu(self.window)
            menu_option = menu.run()

            # MENU OPTIONS

            # NEW GAME
            if menu_option == MENU_OPTION[0]:

                # LEVELS

                # LEVEL 1
                level = Level(self.window, 'Level1', menu_option, player_score)
                level_return = level.run(player_score)

                # LEVEL 2
                if level_return:
                    level = Level(self.window, 'Level2', menu_option, player_score)
                    level_return = level.run(player_score)

                    if level_return:
                        # score.save(menu_return, player_score)
                        pass

            elif menu_option == MENU_OPTION[1]:  # SCORE
                # score.show()
                pass

            elif menu_option == MENU_OPTION[2]:  # QUIT
                pygame.quit()
                sys.exit()

            else:
                print("Invalid option")