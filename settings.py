from dataclasses import dataclass
from enum import Enum

FPS = 30
W_WIDTH = 1000
W_HEIGHT = 720
W_HALF_WIDTH = W_WIDTH // 2
W_HALF_HEIGHT = W_HEIGHT // 2

BALL_SPEED = 400
BALL_MAX_SPEED = 1400

PLAYER_SPEED = 500
PLAYER_HIT_DELAY = 500
DANGLE = 1

MAX_BG_RATIO = 1.2
MIN_BG_RATIO = 1.0

BALL_HEIGHT = 50
BALL_WIDTH = 50

PLAYER_HEIGHT = 100
PLAYER_WIDTH = 30

FONT_SIZE_1 = 60

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

@dataclass
class PSize:
    x: int
    y: int


class Side(Enum):
    LEFT = 'left'
    RIGHT = 'right'

@dataclass
class DirButtons:
    up: int
    down: int
    left: int
    right: int
    side: Side


class ArrowSign(Enum):
    RIGHT = '→'
    LEFT  = '←'
