from pico2d import *

from subject import Subject


class Student:
    font = None

    def __init__(self):
        self.hp_x, self.hp_y = 200, 525
        self.hp = 0
        self.hp_max = 100
        self.damage = 10
        self.gold = 0
        self.exp = 0
        self.exp_max = 100
        self.level = 1
        self.image = load_image('hp_bar.png')
        if Student.font == None:
            Student.font = load_font('ENCR10B.TTF', 16)

    def update(self, frame_time):
        pass

    def update_hp(self, subject, frame_time):
        self.hp += subject.TIME_PER_DAMAGE * subject.damage * frame_time
        pass

    def attack(self):
        self.gold += 10
        self.exp += 10
        if self.exp >= self.exp_max:
            self.level_up()

    def level_up(self):
        self.exp = 0
        self.damage += 5
        self.hp_max += 10
        self.exp_max += 50
        self.level += 1

    def draw(self, frame_time):
        self.image.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)
        Student.font.draw(self.hp_x - 30, self.hp_y, 'Stress: %d / %d' %(self.hp, self.hp_max), (0, 0, 0))
        Student.font.draw(50, 550, 'GOLD: %d' % self.gold, (255, 228, 0))
        Student.font.draw(50, 575, 'LV. %d EXP: %d / %d' %(self.level, self.exp, self.exp_max), (0, 0, 0))

