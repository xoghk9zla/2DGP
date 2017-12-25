import random

from pico2d import *

from student import Student

class Randombox:
    def __init__(self):
        self.x, self.y = 300, 300
        self.x_range, self.y_range = 50, 50
        self.image = load_image('images/randombox/randombox.png')
        Randombox.take_box_sound = load_music('sounds/randombox/bell.mp3')
        Randombox.take_box_sound.set_volume(128)

    def draw(self, frame_time):
        self.image.draw(self.x, self.y)

    def open_box(self, student):
        if random.randint(0, 99) < 30:
            student.gold += 50 * student.level
        else:
            if student.hp > 10 + student.level:
                student.hp -= 10 + student.level
            else:
                student.hp = 0
