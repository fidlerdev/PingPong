import pygame as pg
from game_sprite import GameSprite
from settings import *
from random import random, seed, choice
from math import tau, cos, sin, pi, radians
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
        self.game = game

        # Рандомно выбираем сторону угол в одной из 4 четвертей
        seed(time())
        self.angle = choice(
            [
                random() * pi / 2 - 1 - .5,
                pi / 2 + random() * pi / 2 + .5,
                pi + random() * pi / 2 + .5,
                3 * pi / 2 + random() * pi / 2 - .5,
            ]
        )

        self.spawn_time = pg.time.get_ticks()
        self.player_hit_time = pg.time.get_ticks()

    def update(self,  *args, **kwargs) -> None:
        self.rect.x += cos(self.angle) * self.speed * self.game.delta_time
        self.rect.y += sin(self.angle) * self.speed * self.game.delta_time

        # Чем дольше мяч живет, тем быстрее он становится
        now: int = pg.time.get_ticks()
        multiplier: float = (now - self.spawn_time) / 10000000
        # Если скорость не больше максимальной
        if abs(self.speed) <= BALL_MAX_SPEED:
            self.speed *= (1 + multiplier)

        # Коллизия с верхней и нижней стеной
        if (self.rect.y >= W_HEIGHT - self.rect.width or
            self.rect.y <= 0):
            self.last_angle_change = now

            self.angle = pi - self.angle
            self.speed = -self.speed

        # Коллизия с игроком
        playerCol: list[Player] = pg.sprite.spritecollide(self, self.game.players, False)

        if playerCol and (now - self.player_hit_time) > PLAYER_HIT_DELAY:
            self.angle = tau - self.angle
            # self.angle = radians(playerCol[0].arrow_angle)
            self.speed = -self.speed
            self.game.who_touched_last = playerCol[0]
            self.player_hit_time = now
            choice(self.game.audio.hit_sounds).play()

        # Мяч улетает за экран (пока оба случая)
        if self.rect.x > W_WIDTH or self.rect.x + self.rect.width < 0:

            # Выигрыш левого
            if self.rect.x > W_WIDTH:
                self.game.score_left += 1
            # Выигрыш правого
            if self.rect.x + self.rect.width < 0:
                self.game.score_right += 1

            self.angle = random() * tau
            self.rect.x = W_WIDTH // 2 - self.rect.width // 2
            self.rect.y = W_HEIGHT // 2 - self.rect.height // 2
            # Восстанавливаем скорость при выходе за игровое поле
            self.spawn_time = now
            self.speed = BALL_SPEED
