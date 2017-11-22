import random

from pico2d import *


class Subject:
    font = None

    DAMAGE_PER_TIME = 3.0
    TIME_PER_DAMAGE = 1.0 / DAMAGE_PER_TIME

    TIME_PER_ACTION = 3.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    def __init__(self):
        self.name = 'C Language'
        self.x, self.y = 600, 400
        self.x_range, self.y_range = 100, 75
        self.hp_x, self.hp_y = 600, 525
        self.hp = 100
        self.hp_max = 100
        self.damage = 5
        self.frame = 0
        self.total_frames = 0.0

        self.image = load_image('subject.png')
        self.image_hp = load_image('hp_bar.png')
        if Subject.font == None:
            Subject.font = load_font('ENCR10B.TTF', 16)

    def update(self, frame_time):
        self.total_frames += Subject.FRAMES_PER_ACTION * Subject.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5

    def update_hp(self, student):
        if self.hp > student.damage:
            self.hp -= student.damage
        else:
            self.hp = self.hp_max

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 440, 0, 440, 275, self.x, self.y, self.x_range * 2, self.y_range * 2)
        self.image_hp.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)
        Subject.font.draw(self.hp_x - 65, self.hp_y + 25, 'Subject: %s' % self.name, (0, 0, 0))
        Subject.font.draw(self.hp_x - 65, self.hp_y, 'HP: %d / %d' % (self.hp, self.hp_max), (0, 0, 0))