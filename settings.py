from dataclasses import dataclass

FPS = 30
W_WIDTH = 800
W_HEIGHT = 720

PLAYER_SPEED = 0.4
BALL_SPEED = 0.5

BALL_HEIGHT = 50
BALL_WIDTH = 50

PLAYER_HEIGHT = 100
PLAYER_WIDTH = 30

@dataclass
class PSize:
    x: int
    y: int

@dataclass
class DirButtons:
    up: int
    down: int