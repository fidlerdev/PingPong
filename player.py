import pygame as pg
from gamesprite import GameSprite
from settings import *


class Player(GameSprite):

    def update(self, btns: DirButtons):
        key_pressed = pg.key.get_pressed()

        if key_pressed[btns.up] and self.pos.y > 0:
            self.pos.y -= self.speed

        if (key_pressed[btns.down] and
            self.pos.y < W_HEIGHT - self.rect.height):
            self.pos.y += self.speed

