import random

from pico2d import *

from student import Student


class Randombox:
    def __init__(self):
        self.x, self.y = 300, 300
        self.x_range, self.y_range = 50, 50
        self.image = load_image('randombox.png')

    def draw(self, frame_time):
        self.image.draw(self.x, self.y)

    def open_box(self, student):
        if random.randint(0, 9) < 3:
            student.gold += 100
        else:
            if student.hp > 10:
                student.hp -= 10
            else:
                student.hp = 0
