import random

from pico2d import *

import game_framework
import main_state
import endding_state


class Subject:
    DAMAGE_PER_TIME = 3.0
    TIME_PER_DAMAGE = 1.0 / DAMAGE_PER_TIME

    TIME_PER_ACTION = 3.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    subject_list = [
        "C_Langugae", "C++", "2DGP", "3DGP", "Graduation_Work"
    ]

    def __init__(self):
        self.level = 0
        self.name = self.subject_list[self.level]
        self.x, self.y = 600, 400
        self.x_range, self.y_range = 100, 75
        self.hp_x, self.hp_y = 600, 525
        self.hp = 100
        self.hp_max = 100
        self.damage = 5
        self.progress = 0
        self.frame = 0
        self.total_frames = 0.0

        self.image = load_image('images/subject/subject.png')
        self.image_hp = load_image('images/subject/hp_bar.png')

    def update(self, frame_time):
        self.total_frames += Subject.FRAMES_PER_ACTION * Subject.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5

    def update_hp(self, student):
        if self.hp > student.damage:
            self.hp -= student.damage * 0.75
        else:
            self.hp = self.hp_max
            if self.progress + 10 - self.level < 100:
                self.progress += 10 - self.level
            else:
                self.finish()

    def finish(self):
        if self.level < 4:
            self.level += 1
            self.progress = 0
            self.hp_max += 10
            self.hp = self.hp_max
            self.damage += 5
            self.name = self.subject_list[self.level]
        else:
            game_framework.change_state(endding_state)

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 440, 0, 440, 275, self.x, self.y, self.x_range * 2, self.y_range * 2)
        self.image_hp.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)
        main_state.font.draw(self.hp_x - 65, self.hp_y + 50, 'Subject: %s' % self.name, (0, 0, 0))
        main_state.font.draw(self.hp_x - 65, self.hp_y + 25, 'progress: %d' % self.progress, (0, 0, 0))
        main_state.font.draw(self.hp_x - 65, self.hp_y, 'HP: %d / %d' % (self.hp, self.hp_max), (0, 0, 0))