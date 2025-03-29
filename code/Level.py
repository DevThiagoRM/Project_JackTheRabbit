#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Const import TIMEOUT_LEVEL, EVENT_TIMEOUT, TIMEOUT_STEP, \
    C_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font
from typing import List


class Level:
    def __init__(self, window: Surface, name: str):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # LOAD BACKGROUNDS
        self.entity_list.extend(EntityFactory.get_entity('Player'))  # LOAD PLAYER
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def level_text(self, text_size: int, text_bold: bool, text: str, text_color: tuple, text_pos: tuple, ):
        text_font: Font = pygame.font.SysFont(name="Comic Sans", size=text_size, bold=text_bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        # LEVEL MUSIC
        pygame.mixer.music.load(f'./assets/{self.name}.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # REFRESH RATE
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)  # FPS

            # REFRESH DISPLAY
            for ent in self.entity_list:
                if 'Player' in ent.name:
                    self.level_text(20, False, f'Jack - Health {ent.health} | Score: {ent.score}', C_WHITE, (10, 30))
                self.window.blit(source=ent.surf, dest=ent.rect)  # RENDER ALL ENTITIES
                ent.move()  # UPDATE ANIMATION AND MOVE

            for event in pygame.event.get():

                # QUIT GAME
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # EVENT_TIMEOUT
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        pass

            # PRINTED TEXT
            self.level_text(20, False, f'{self.name.upper()} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(20, False, f'FPS: {clock.get_fps():.0f}', C_WHITE, (WIN_WIDTH - 80, 5))
            self.level_text(20, False, f'Entities: {len(self.entity_list)}', C_WHITE,
                            (WIN_WIDTH - 112.5, WIN_HEIGHT - 30))

            pygame.display.flip()