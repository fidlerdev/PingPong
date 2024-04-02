import pygame as pg
from gamesprite import GameSprite
from settings import *
from random import random, seed
from math import tau, cos, sin, pi
from time import time
from player import Player

class Ball(GameSprite):
    def __init__(
                self,
                 game,
                 image_path: str,
                 pos: PSize,
                 size: PSize,
                 speed: float
                ) -> None:
        super().__init__(game, image_path, pos, size, speed)
        seed(time())
        self.angle = random() * tau
        self.last_angle_change = pg.time.get_ticks()
        self.angle_change_delay = 400
        
    def update(self) -> None:
        now = pg.time.get_ticks()
        self.rect.x += cos(self.angle) * self.speed * self.game.delta_time
        self.rect.y += sin(self.angle) * self.speed * self.game.delta_time
        
        # Коллизия с верхней и нижней стеной
        if (self.rect.y >= W_HEIGHT - self.rect.width or
            self.rect.y <= 0):
            
            if now - self.last_angle_change < self.angle_change_delay:
                return
            
            self.angle = pi - self.angle
            self.speed = -self.speed
            self.last_angle_change = now
        
        # Коллизия с игроком
        playerCol: list[Player] = pg.sprite.spritecollide(self, self.game.players, False)
        if playerCol:
            self.angle = random() * tau
            self.speed = -self.speed
            self.game.who_touched_last = playerCol[0]
            print(playerCol[0].rect.x)
            
        # Мяч улетает за экран (пока оба случая)
        if self.rect.x > W_WIDTH or self.rect.x + self.rect.width < 0:
            self.angle = random() * tau
            self.rect.x = W_WIDTH // 2 - self.rect.width // 2
            self.rect.y = W_HEIGHT // 2 - self.rect.height // 2
            
            