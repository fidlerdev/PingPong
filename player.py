import pygame as pg
from gamesprite import GameSprite
from settings import *


class Player(GameSprite):

    def update(self, btns: DirButtons):
        key_pressed = pg.key.get_pressed()

        if key_pressed[btns.up] and self.rect.y > 0:
            self.rect.y -= self.speed * self.game.delta_time

        if (key_pressed[btns.down] and
                self.rect.y < W_HEIGHT - self.rect.height):
            self.rect.y += self.speed * self.game.delta_time

