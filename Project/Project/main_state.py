import random
import json
import os

from pico2d import *

import game_framework
import title_state
import gameover_state

name = "MainState"

x, y = 0, 0
student = None
subject = None
room = None
boxs = None

class Room:
    def __init__(self):
        self.image = load_image('room.png')

    def draw(self):
        self.image.draw(400, 300)


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
        self.image = load_image('hp_e.png')
        if Student.font == None:
            Student.font = load_font('ENCR10B.TTF', 16)

    def update(self, frame_time):
        self.hp += subject.damage
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

    def draw(self):
        self.image.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)
        Student.font.draw(self.hp_x - 30, self.hp_y, 'Stress: %d / %d' %(self.hp, self.hp_max), (0, 0, 0))
        Student.font.draw(50, 550, 'GOLD: %d' % self.gold, (255, 228, 0))
        Student.font.draw(50, 575, 'LV. %d EXP: %d / %d' %(self.level, self.exp, self.exp_max), (0, 228, 0))


class Subject:
    font = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    def __init__(self):
        self.name = 'C Language'
        self.x, self.y = 600, 400
        self.hp_x, self.hp_y = 600, 525
        self.hp = 100
        self.hp_max = 100
        self.damage = 0.01
        self.frame = 0
        self.total_frame = 0.0

        self.image = load_image('Enemy_C.png')
        self.image_hp = load_image('hp_e.png')
        if Subject.font == None:
            Subject.font = load_font('ENCR10B.TTF', 16)

    def update(self, frame_time):
        #self.total_frame = Subject.FRAMES_PER_ACTION * Subject.ACTION_PER_TIME * frame_time
        #self.frame = (self.frame + 1) % 5
        self.frame = 4

    def update_hp(self):
        if self.hp > student.damage:
            self.hp -= student.damage
        else:
            self.hp = self.hp_max

    def draw(self):
        self.image.clip_draw(self.frame * 440, 0, 440, 275, self.x, self.y, 200, 150)
        self.image_hp.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)
        Subject.font.draw(self.hp_x - 65, self.hp_y + 25, 'Subject: %s' % self.name, (0, 0, 0))
        Subject.font.draw(self.hp_x - 65, self.hp_y, 'HP: %d / %d' % (self.hp, self.hp_max), (0, 0, 0))


class Randombox:
    def __init__(self):
        self.x, self.y = 300, 300
        self.image = load_image('randombox.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def open_box(self):
        if random.randint(0, 9) < 5:
            student.gold += 100
        else:
            student.hp -= 10


def enter():
    global student, subject, room, boxs
    student = Student()
    subject = Subject()
    room = Room()
    boxs = []


def exit():
    global student, subject, room, boxs
    del(student)
    del(subject)
    del(room)
    del(boxs)


def pause():
    pass


def resume():
    pass


current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time

    current_time += frame_time
    return frame_time


def collide(ob, x, y):
    if ob.x - 100 > x: return False
    if x > ob.x + 100: return False
    if ob.y - 75 > y: return False
    if y > ob.y + 75: return False

    return True


def handle_events(frame_time):
    global x, y, boxs

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if collide(subject, x, y):
                subject.update_hp()
                student.attack()
                if random.randint(0, 9) == 3:
                    boxs.append(Randombox())
            for box in boxs:
                if collide(box, x, y):
                    box.open_box()
                    boxs.remove(box)


def update(frame_time):
    frame_time = get_frame_time()
    subject.update(frame_time)

    if student.hp < student.hp_max:
        student.update(frame_time)
    else:
        game_framework.change_state(gameover_state)


def draw(frame_time):
    clear_canvas()

    room.draw()
    student.draw()
    subject.draw()
    for box in boxs:
        box.draw()

    update_canvas()