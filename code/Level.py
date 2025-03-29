#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
import sys

from code.Const import TIMEOUT_LEVEL, EVENT_TIMEOUT, TIMEOUT_STEP, \
    C_WHITE, WIN_HEIGHT, WIN_WIDTH, EVENT_OBSTACLE, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font
from typing import List

from code.EntityMediator import EntityMediator
from code.Score import Score


class Level:
    def __init__(self, window: Surface, name: str):
        self.start_time = pygame.time.get_ticks()
        self.window = window
        self.name = name
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # LOAD BACKGROUNDS
        self.entity_list.extend(EntityFactory.get_entity('Player'))  # LOAD PLAYER
        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME, 0)

    def level_text(self, text_size: int, text_bold: bool, text: str, text_color: tuple, text_pos: tuple):
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

            player_dead = EntityMediator.verify_health(self.entity_list, self.window)
            if player_dead:
                score = Score(self.window)
                score_value = pygame.time.get_ticks() / 1000
                score.save("NEW GAME", [score_value])
                score.show()
                return

            self.timeout = (pygame.time.get_ticks() - self.start_time) / 1000

            # REFRESH DISPLAY
            for ent in self.entity_list:
                if isinstance(ent, list):
                    for sub_ent in ent:
                        if 'Player' in sub_ent.name:
                            self.level_text(20, False, f'Jack - Health {sub_ent.health} | Score: {self.timeout:.1f}',
                                            C_WHITE, (10, 30))
                        self.window.blit(source=sub_ent.surf, dest=sub_ent.rect)
                        sub_ent.move()

                elif isinstance(ent, Entity):
                    if 'Player' in ent.name:
                        self.level_text(20, False, f'Jack - Health {ent.health} | Score: {self.timeout:.1f}',
                                        C_WHITE, (10, 30))
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()

            for event in pygame.event.get():

                # QUIT GAME
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_OBSTACLE:
                    choice = random.choice(('Obstacle1', 'Obstacle2', 'Obstacle3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # PRINTED TEXT
            self.level_text(20, False, f'{self.name.upper()}', C_WHITE, (10, 5))
            self.level_text(20, False, f'FPS: {clock.get_fps():.0f}', C_WHITE, (WIN_WIDTH - 80, 5))
            self.level_text(20, False, f'Entities: {len(self.entity_list)}', C_WHITE,
                            (WIN_WIDTH - 112.5, WIN_HEIGHT - 30))

            pygame.display.flip()

            # COLLISIONS
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list, window=self.window)


