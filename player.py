import pygame as pg
from game_sprite import GameSprite
from text_arrow import TextArrow
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
        self.arrow_angle = 0 if btns.side == Side.LEFT else 180
        self.arrow = TextArrow(
            self.game,
            self,
            (
                ArrowSign.LEFT.value
                if btns.side == Side.RIGHT
                else ArrowSign.RIGHT.value
            ),
            angle=self.arrow_angle,
        )

    def update(self, *args, **kwargs) -> None:
        self.key_pressed = pg.key.get_pressed()

        if self.key_pressed[self.btns.up] and self.rect.y > 0:
            self.rect.y -= self.speed * self.game.delta_time

        if (
            self.key_pressed[self.btns.down]
            and self.rect.y < W_HEIGHT - self.rect.height
        ):
            self.rect.y += self.speed * self.game.delta_time

        # ПОТОМ...
        # if self.key_pressed[self.btns.left]:
        #     if (
        #         self.btns.side == Side.LEFT
        #         # and self.arrow_angle < tau + pi
        #         or self.btns.side == Side.RIGHT
        #         # and self.arrow_angle < pi + pi
        #     ):
        #         self.arrow_angle += DANGLE

        # if self.key_pressed[self.btns.right]:
        #     if (
        #         self.btns.side == Side.LEFT
        #         # and self.arrow_angle > tau - pi
        #         or self.btns.side == Side.RIGHT
        #         # and self.arrow_angle > pi - pi / 3
        #     ):
        #         self.arrow_angle -= DANGLE

        # self.arrow.angle = self.arrow_angle
        # self.arrow.draw()
