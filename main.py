import pygame as pg
from settings import *
from player import Player

class Game:

    def __init__(self):
        # Запускаем движок PyGame
        pg.init()
        self.window = pg.display.set_mode((W_WIDTH, W_HEIGHT))
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        '''
        Метод отвечает за запуск новой игры
        '''
        # Переменная игрового цикла
        self.run_game = True
        self.bg = pg.transform.scale(
            pg.image.load('pics/bg.jpg'),
            (W_WIDTH, W_HEIGHT)
        )
        self.playerL = Player(
            window=self.window,
            image_path='pics/left-block.png',
            pos=PSize(
                x=10, y=(W_WIDTH // 2 - 100) 
            ),
            size=PSize(x=40, y=200),
            speed=5
        )
        self.playerR = Player(
            window=self.window,
            image_path='pics/right-block.png',
            pos=PSize(
                x=(W_WIDTH-40-10), y=(W_WIDTH // 2 - 100) 
            ),
            size=PSize(x=40, y=200),
            speed=5
        )
      
      

    def update(self):
        '''
        Меняем положение спрайтов
        '''
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run_game = False

        self.playerL.update(
            btns=DirButtons(
                up=pg.K_w,
                down=pg.K_s
            )
        )

        self.playerR.update(
            btns=DirButtons(
                up=pg.K_UP,
                down=pg.K_DOWN
            )
        )

        pg.display.flip()

    
    def draw(self):
        '''
        Отрисовываем спрайты в окне
        '''
        self.window.blit(self.bg, (0, 0))
        self.playerL.draw()
        self.playerR.draw()

    def run(self):
        '''
        Запуск игрового цикла
        '''
        while self.run_game:
            self.update()
            self.draw()
            self.clock.tick(FPS)
    

if __name__ == '__main__':
    game = Game()
    game.run()

