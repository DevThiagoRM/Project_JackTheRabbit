#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import pygame

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Obstacle import Obstacle
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name=str, position=(0, 0)):
        match entity_name:
            case'MenuBg':
                list_bg = []
                for i in range(7):  # MenuBg IMAGES NUMBER
                    list_bg.append(Background(f'MenuBg{i}', (0, 0)))
                    list_bg.append(Background(f'MenuBg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level1Bg':
                list_bg = []
                for i in range(8):  # Level1Bg IMAGES NUMBER
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                player_sprites = []
                for i in range(4):  # Player0, Player1, Player2, Player3
                    player_sprites.append(Player(f'Player{i}', (120, WIN_HEIGHT - 56)))
                return player_sprites  # RETURN ALL SPRITES

            case 'Obstacle1':
                return Obstacle('Obstacle1', (WIN_WIDTH + 10, WIN_HEIGHT - 32))

            case 'Obstacle2':
                return Obstacle('Obstacle2', (WIN_WIDTH + 10, WIN_HEIGHT - 63))

            case _:
                return []

