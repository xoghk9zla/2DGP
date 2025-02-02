from pico2d import *

from subject import Subject

import main_state


class Student:
    def __init__(self):
        self.hp_x, self.hp_y = 200, 525
        self.hp = 0
        self.hp_max = 100
        self.damage = 10
        self.gold = 1000
        self.exp = 0
        self.exp_max = 100
        self.level = 1
        self.image = load_image('images/student/hp_bar.png')
        self.skill_self_cancel_a_class_image = load_image('images/student/skill1.png')
        self.skill_drink_image = load_image('images/student/skill2.png')

    def update(self, frame_time):
        pass

    def update_hp(self, subject, frame_time):
        self.hp += subject.TIME_PER_DAMAGE * subject.damage * frame_time
        pass

    def attack(self, subject):
        self.gold += 10 + (10 * subject.level)
        self.exp += 10
        if self.exp >= self.exp_max:
            self.level_up()

    def level_up(self):
        self.exp = 0
        self.damage += 5
        self.hp_max += 10
        self.exp_max += 50
        self.level += 1

    def skill_self_cancel_a_class(self, subject):
        if self.hp > 5:
            self.hp -= 5
        else:
            self.hp = 0

        if subject.progress > 5:
            subject.progress -= 5
        else:
            subject.progress = 0

    def skill_drink(self):
        if self.hp > 10:
            self.hp -= 10
        else:
            self.hp = 0
        self.gold -= 300 * self.level / 3

    def draw(self, frame_time):
        self.image.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y - 25, 2.2 * self.hp, 25)
        self.skill_self_cancel_a_class_image.draw(75, 75)
        self.skill_drink_image.draw(175, 75)
        main_state.font.draw(self.hp_x - 30, self.hp_y - 25, 'Stress: %d / %d' %(self.hp, self.hp_max), (0, 0, 0))
        main_state.font.draw(50, self.hp_y, 'GOLD: %d' % self.gold, (255, 228, 0))
        main_state.font.draw(50, self.hp_y + 25, 'DAMAGE: %d' % self.damage, (255, 50, 50))
        main_state.font.draw(50, self.hp_y + 50, 'LV. %d EXP: %d / %d' %(self.level, self.exp, self.exp_max), (0, 0, 0))

