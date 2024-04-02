from dataclasses import dataclass


FPS = 60
W_WIDTH = 1280
W_HEIGHT = 720


@dataclass
class PSize:
    x: int
    y: int

@dataclass
class DirButtons:
    up: int
    down: int