import pygame as pg
from settings import *


class TextArrow:
    def __init__(self, game, player, _arrow: str, angle: float) -> None:
        self.game = game
        self.player = player
        self.arrow = _arrow
        self.angle = angle

    def draw(self) -> None:
        rotated_arrow = pg.transform.rotozoom(
            self.game.main_font.render(f"{self.arrow}", 1, WHITE), -self.angle, 1
        )  # Rotate the image.
        pivot = self.player.rect.left, self.player.rect.centery
        rotated_offset = pg.math.Vector2(40, 0).rotate(self.angle)
        rect = rotated_arrow.get_rect(center=pivot+rotated_offset)

        # arrow_surface = pg.transform.rotate(
        #     self.game.main_font.render(f"{self.arrow}", 1, WHITE),
        #     self.angle,
        # ).convert_alpha()

        # if self.player.btns.side == Side.LEFT:
        #     self.game.window.blit(
        #         arrow_surface,
        #         (
        #             self.player.rect.right,
        #             self.player.rect.centery - arrow_surface.get_height() / 2,
        #         ),
        #     )

        self.game.window.blit(rotated_arrow, rect)
