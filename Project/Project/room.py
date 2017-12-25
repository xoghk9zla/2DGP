from pico2d import *


class Room:
    def __init__(self):
        self.image = load_image('images/room/room.png')
        self.bgm = load_music('sounds/room/main_bgm.mp3')
        self.bgm.set_volume(128)
        self.bgm.repeat_play()

    def draw(self, frame_time):
        self.image.draw(400, 300)
