#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Background speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
