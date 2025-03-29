#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Obstacle import Obstacle
from code.Entity import Entity
from code.Player import Player
from code.Score import Score


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):

        if isinstance(ent, Obstacle):  # COLLISION Obstacle
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Obstacle):
            valid_interaction = True
        elif isinstance(ent1, Obstacle) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (
                    ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom >= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom
            ):
                player = ent1 if isinstance(ent1, Player) else ent2
                obstacle = ent2 if isinstance(ent2, Obstacle) else ent1
                last_dmg_from = getattr(player, 'last_dmg_from', None)
                invincible = getattr(player, 'invincible', False)

                if not invincible or last_dmg_from != obstacle.name:
                    player.health -= obstacle.damage
                    player.last_dmg = obstacle.name
                    player.last_dmg_from = obstacle.name
                    player.invincible = True
                    player.invincible_timer = pygame.time.get_ticks()
                    obstacle.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity], window):
        for ent in entity_list[:]:
            if isinstance(ent, Entity) and ent.health <= 0:
                if isinstance(ent, Player):
                    return True  # Player Dead
                elif isinstance(ent, Obstacle):
                    entity_list.remove(ent)
        return False

