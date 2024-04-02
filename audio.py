import pygame as pg

class Audio:
    
    def __init__(self):
        # Подключаем фоновую музыку
        pg.mixer.music.load('audio/theme.mp3')
        self.hit_sounds: list[pg.mixer.Sound] = [
            pg.mixer.Sound('audio/hit1.wav'),
            pg.mixer.Sound('audio/hit2.wav'),
            pg.mixer.Sound('audio/hit3.wav'),
            pg.mixer.Sound('audio/hit4.wav'),
        ]
        for sound in self.hit_sounds:
            sound.set_volume(1.5)
        self.collect_sound = pg.mixer.Sound('audio/collect.wav')
        self.timer_sound = pg.mixer.Sound('audio/timer.wav')
        
    def play_theme(self):
        pg.mixer.music.play()