import pygame as pg
from settings import *
from enum import Enum

class BGAnimation(Enum):
    MINIMIZE = 'MINIMIZE'
    MAXIMIZE = 'MAXIMIZE'

class Background:

    def __init__(self, image_path: str, game):
        self.game = game
        self.image = pg.transform.scale(
            pg.image.load(image_path),
            (W_WIDTH, W_HEIGHT)
        ).convert()
        self.rect = self.image.get_rect()
        # Сначала увеличиваем задний фон
        self.animation = BGAnimation.MAXIMIZE

    # Анимация заднего фона
    def update(self):

        if self.rect.height >= W_HEIGHT * MAX_BG_RATIO:
            self.animation = BGAnimation.MINIMIZE
        if self.rect.height <= W_HEIGHT * MIN_BG_RATIO:
            self.animation = BGAnimation.MAXIMIZE

        dsize = 1.004

        if self.animation == BGAnimation.MAXIMIZE:
            self.rect.height *= dsize
            self.rect.width *= dsize

        if self.animation == BGAnimation.MINIMIZE:
            self.rect.height /= dsize
            self.rect.width  /= dsize

        self.rect.centerx = W_HALF_WIDTH
        self.rect.centery = W_HALF_HEIGHT

    def draw(self):
        self.game.window.blit(
            pg.transform.scale(
                self.image,
                (self.rect.width, self.rect.height)
            ),
            (self.rect.x, self.rect.y)
        )
