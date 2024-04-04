import pygame as pg
from game_sprite import GameSprite
from settings import *
from settings import PSize
from math import pi, tau, radians


class Player(GameSprite):
    def __init__(
        self,
        game,
        image_path: str,
        pos: PSize,
        size: PSize,
        speed: float,
        btns: DirButtons,
    ) -> None:
        super().__init__(game, image_path, pos, size, speed)
        self.btns = btns

    def update(self, *args, **kwargs) -> None:
        self.key_pressed = pg.key.get_pressed()

        if self.key_pressed[self.btns.up] and self.rect.y > 0:
            self.rect.y -= self.speed * self.game.delta_time

        if (
            self.key_pressed[self.btns.down]
            and self.rect.y < W_HEIGHT - self.rect.height
        ):
            self.rect.y += self.speed * self.game.delta_time
