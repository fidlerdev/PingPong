import pygame as pg
from settings import *
from player import Player
from background import Background
from ball import Ball
from audio import Audio

class Game:
    def __init__(self):
        # Запускаем движок PyGame
        pg.init()
        self.window = pg.display.set_mode((W_WIDTH, W_HEIGHT))
        self.clock = pg.time.Clock()

        self.audio = Audio()
        self.audio.play_theme()

        self.main_font = pg.font.Font("fonts/SYNNova-Bold.otf", size=FONT_SIZE_1)

        self.new_game()

    def new_game(self):
        """
        Метод отвечает за запуск новой игры
        """
        # Переменная игрового цикла
        self.run_game = True
        # Кто последний дотронулся до мяча
        self.who_touched_last = None
        self.score_left = 0
        self.score_right = 0

        self.bg = Background("pics/bg.jpg", self)
        self.playerL = Player(
            game=self,
            image_path="pics/left-block.png",
            pos=PSize(x=10, y=(W_WIDTH // 2 - PLAYER_HEIGHT // 2)),
            size=PSize(x=PLAYER_WIDTH, y=PLAYER_HEIGHT),
            speed=PLAYER_SPEED,
            btns=DirButtons(up=pg.K_w, down=pg.K_s),
        )
        self.playerR = Player(
            game=self,
            image_path="pics/right-block.png",
            pos=PSize(
                x=(W_WIDTH - PLAYER_WIDTH - 10), y=(W_WIDTH // 2 - PLAYER_HEIGHT // 2)
            ),
            size=PSize(x=PLAYER_WIDTH, y=PLAYER_HEIGHT),
            speed=PLAYER_SPEED,
            btns=DirButtons(
                up=pg.K_UP, down=pg.K_DOWN),
        )
        self.ball = Ball(
            game=self,
            image_path="pics/ball.png",
            pos=PSize(W_WIDTH // 2, W_HEIGHT // 2),
            size=PSize(BALL_WIDTH, BALL_HEIGHT),
            speed=BALL_SPEED,
        )
        self.players = pg.sprite.Group()
        self.players.add(self.playerL)
        self.players.add(self.playerR)

    def update(self):
        """
        Меняем положение спрайтов
        """
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run_game = False

        self.playerL.update()
        self.playerR.update()
        self.ball.update()
        self.bg.update()
        self.score_text = self.main_font.render(
            f"{self.score_left} : {self.score_right}", 1, BLACK
        ).convert_alpha()
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")
        pg.display.flip()

    def draw(self):
        """
        Отрисовываем спрайты в окне
        """
        self.bg.draw()
        self.playerL.draw()
        self.playerR.draw()
        self.ball.draw()
        # TODO: сделать текст классом с методом draw
        self.window.blit(
            self.score_text,
            (
                W_HALF_WIDTH - self.score_text.get_width() // 2,
                10,
            ),
        )

    def run(self):
        """
        Запуск игрового цикла
        """
        while self.run_game:
            self.delta_time = self.clock.tick(FPS) / 1000.0
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
