#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Const import TIMEOUT_LEVEL, EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_STEP, \
    C_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from pygame import Surface, Rect
from pygame.font import Font
from typing import List

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: int):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.player_score = player_score
        self.game_Mode = game_mode
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # Levels Background
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME, 0)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
        player = EntityFactory.get_entity('Player1')  # SCORE PLAYER 1
        # player.score = 0
        self.entity_list.append(player)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, ):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans TypeWriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self, player_score: int):
        # LEVEL MUSIC
        pygame.mixer.music.load(f'./assets/{self.name}.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Param to Loop music

        # REFRESH RATE
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)  # FPS

            # REFRESH DISPLAY
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                # if isinstance(ent, (Player, Enemy)):
                #     shoot = ent.shoot()
                #     if shoot is not None:
                #         self.entity_list.append(shoot)
                # if ent.name == 'Player':
                #     self.level_text(20, f'Player - Health {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # QUIT GAME
                    pygame.quit()
                    sys.exit()

                # if event.type == EVENT_ENEMY:
                #     choice = random.choice['Enemy1', 'Enemy2']
                #     self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score = ent.score
                        return True
                found_player = False

                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # PRINTED TEXT
            self.level_text(20, f'{self.name} Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(20, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'Entities: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # COLLISIONS
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
