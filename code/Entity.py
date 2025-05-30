#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from abc import ABC, abstractmethod
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)

        # ENTITY ATTRIBUTES
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]

    @abstractmethod
    def move(self):
        pass
