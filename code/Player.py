import pygame
from code.Entity import Entity
from code.Const import PLAYER_KEY_UP, ENTITY_SPEED, PLAYER_KEY_DOWN, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_SPACE


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.current_sprite = 0  # CONTROL SPRITE SHOWED (0 a 3)
        self.animation_speed = 0.2  # ANIMATION SPEED (+ Bigger, + Slow)
        self.last_update = pygame.time.get_ticks()  # LAST FRAME TIME
        self.damage = 1
        self.invincible = False
        self.invincible_timer = 0
        self.invincible_duration = 500
        self.last_dmg_from = None

        # JUMP CONTROL VARs
        self.jumping = False  # JUMP STATE
        self.jump_velocity = 0  # JUMP SPEED
        self.gravity = 1  # GRAVITY
        self.jump_power = -10  # POWER INITIAL JUMP

    def move(self):
        if self.invincible and pygame.time.get_ticks() - self.invincible_timer > self.invincible_duration:
            self.invincible = False
            self.last_dmg_from = None

        super().move()

        pressed_key = pygame.key.get_pressed()
        movement = [0, 0]  # [x, y]

        # PLAYER MOVES

        # JUMP
        if pressed_key[PLAYER_KEY_SPACE] and not self.jumping:
            self.jumping = True
            self.jump_velocity = self.jump_power

        if self.jumping:
            movement[1] += self.jump_velocity
            self.jump_velocity += self.gravity

            if self.rect.bottom >= WIN_HEIGHT - 10:
                self.rect.bottom = WIN_HEIGHT - 10
                self.jumping = False  #
                self.jump_velocity = 0

        # MOVE DOWN
        if pressed_key[PLAYER_KEY_DOWN] and self.rect.bottom < WIN_HEIGHT - 5:
            movement[1] += ENTITY_SPEED[self.name]

        # UPDATE POSITION
        self.rect.move_ip(movement)

        # ANIMATION (SPRITE CHANGE)
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 500:  # SPRITE CHANGES IN x ms
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % 4  # SPRITES LOOP 0, 1, 2, 3
            self.name = f'Player{self.current_sprite}'  # UPDATE SPRITE NAME
            self.surf = pygame.image.load(f'./assets/{self.name}.png').convert_alpha()  # UPDATE SPRITE