from pico2d import *


class Room:
    def __init__(self):
        self.image = load_image('room.png')
        self.bgm = load_music('main_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self, frame_time):
        self.image.draw(400, 300)