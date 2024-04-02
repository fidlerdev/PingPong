from dataclasses import dataclass

FPS = 30
W_WIDTH = 1000
W_HEIGHT = 720
W_HALF_WIDTH = W_WIDTH // 2
W_HALF_HEIGHT = W_HEIGHT // 2

PLAYER_SPEED = 500
BALL_SPEED = 400
BALL_MAX_SPEED = 1400

PLAYER_HIT_DELAY = 100

MAX_BG_RATIO = 1.2
MIN_BG_RATIO = 1.0

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