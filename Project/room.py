from pico2d import *

class Room:
    def __init__(self):
        self.image = load_image('room.png')

    def draw(self, frame_time):
        self.image.draw(400, 300)