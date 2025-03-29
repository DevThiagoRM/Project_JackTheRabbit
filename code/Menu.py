#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Const import WIN_WIDTH, MENU_OPTION, C_YELLOW, C_WHITE, C_BLACK
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font
from typing import List

class Menu:

    def __init__(self, window: Surface):
        self.window = window
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('MenuBg'))  # Menu Background

    def menu_text(self, text_size: int, text_bold: bool, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans", size=text_size, bold=text_bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        menu_option = 0  # INITIAL POSITION

        # MENU MUSIC
        pygame.mixer.music.load('./assets/Menu.mp3') # PATH MENU MUSIC
        pygame.mixer.music.play(-1)  # LOOP MUSIC

        # REFRESH RATE
        clock = pygame.time.Clock()

        while True:
            # FPS
            clock.tick(60)

            # DISPLAY

            # UPDATE BACKGROUND
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # SHOW TITLE MENU
            self.menu_text(50, True, "Jack", C_BLACK, (((WIN_WIDTH / 2) - 2), 72))
            self.menu_text(50, True, "Jack", C_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, True, "The Rabbit", C_BLACK, (((WIN_WIDTH / 2) - 2), 122))
            self.menu_text(50, True, "The Rabbit", C_WHITE, ((WIN_WIDTH / 2), 120))

            # SHOW MENU OPTIONS
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, False, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(25, False, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip() # REFRESH DISPLAY

            # CHECK FOR ALL EVENTS
            for event in pygame.event.get():
                match event.type:

                    case pygame.QUIT: # QUIT GAME
                        pygame.quit()
                        sys.exit()

                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_DOWN:  # KEY DOWN
                                menu_option = (menu_option + 1) % len(MENU_OPTION)

                            case pygame.K_UP:  # KEY UP
                                menu_option = (menu_option - 1) % len(MENU_OPTION)

                            case pygame.K_RETURN:  # KEY ENTER
                                return MENU_OPTION[menu_option]
