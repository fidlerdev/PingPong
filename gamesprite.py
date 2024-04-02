import pygame as pg
from settings import *

class GameSprite(pg.sprite.Sprite):

    def __init__(
            self,
            window: pg.Surface,
            image_path: str,
            pos: PSize,
            size: PSize,
            speed: int    
            ) -> None:
        self.window = window
        self.image = pg.transform.scale(pg.image.load(image_path), size=(size.x, size.y))
        self.pos = pos
        self.speed = speed
        self.rect = self.image.get_rect()

    
    def draw(self):
        self.window.blit(self.image, (self.pos.x, self.pos.y))
        