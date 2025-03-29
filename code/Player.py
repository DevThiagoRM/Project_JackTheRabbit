import pygame
from code.Entity import Entity
from code.Const import PLAYER_KEY_UP, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_HEIGHT, \
    WIN_WIDTH


class Player(Entity):
    def __init__(self, name, position, sprites):
        super().__init__(name, position)
        self.sprites = sprites
        self.current_sprite = 0  # Índice do sprite
        self.surf = self.sprites[self.current_sprite].surf
        self.last_switch_time = pygame.time.get_ticks()  # Armazena o tempo da última troca

    def move(self):
        pressed_key = pygame.key.get_pressed()
        movement = [0, 0]  # [x, y]

        # Movimentação do jogador
        if pressed_key[PLAYER_KEY_UP] and self.rect.top > 0:
            movement[1] -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN] and self.rect.bottom < WIN_HEIGHT:
            movement[1] += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT] and self.rect.left > 0:
            movement[0] -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT] and self.rect.right < WIN_WIDTH:
            movement[0] += ENTITY_SPEED[self.name]

        # Move o retângulo do jogador
        self.rect.move_ip(movement)

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_switch_time >= 100:  # IF 100ms PAST
            self.last_switch_time = current_time
            self.current_sprite += 1  # GOES NEXT SPRITE
            if self.current_sprite >= len(self.sprites):  # RETURN FIRST SPRITE
                self.current_sprite = 0
            self.surf = self.sprites[self.current_sprite].surf  # UPDATE SURFACE WITH SPRITE
            self.image = self.surf
            self.rect = self.image.get_rect(center=self.rect.center)  # ADJUSTMENT RECT WITH NEW IMAGE
