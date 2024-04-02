import pygame as pg
from settings import *

class GameSprite(pg.sprite.Sprite):
    def __init__(
            self,
            game,
            image_path: str,
            pos: PSize,
            size: PSize,
            speed: float
            ) -> None:
        super().__init__()
        self.game = game
        self.image = pg.transform.scale(pg.image.load(image_path), size=(size.x, size.y))
        self.size = size
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos.x
        self.rect.y = pos.y

    
    def draw(self):
        self.game.window.blit(self.image, (self.rect.x, self.rect.y))
        