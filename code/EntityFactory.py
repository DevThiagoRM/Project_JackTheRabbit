#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random

import pygame

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
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

            case 'Level2Bg':
                list_bg = []
                for i in range(8):  # Level2Bg IMAGES NUMBER
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level3Bg':
                list_bg = []
                for i in range(5):  # Level3Bg IMAGES NUMBER
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                list_sprite = []
                for i in range(1):  # Level3Bg IMAGES NUMBER
                    list_sprite.append(Background(f'Player{i}', (120, WIN_HEIGHT - 27)))
                return list_sprite

        pass
