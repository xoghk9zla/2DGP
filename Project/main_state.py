import random
import json
import os

from pico2d import *

import game_framework
import title_state
import gameover_state

name = "MainState"


frame_time = 0.0
x, y = 0, 0


class Room:
    def __init__(self):
        self.image = load_image('room.png')

    def draw(self):
        self.image.draw(400, 300)


class Student:
    def __init__(self):
        self.hp_x, self.hp_y = 200, 525
        self.hp = 0
        self.damage = 10
        self.gold = 0
        self.image = load_image('hp_e.png')

    def update(self):
        delay(0.5)
        self.hp += subject.damage

    def draw(self):
        self.image.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)


class Subject:
    def __init__(self):
        self.x, self.y = 600, 400
        self.hp_x, self.hp_y = 600, 525
        self.hp = 100
        self.max_hp = 100
        self.damage = 1
        self.hit = False
        self.frame = 0
        self.image = load_image('Enemy_C.png')
        self.image_hp = load_image('hp_e.png')

    def update(self):
        global frame_time
        if frame_time > 1.0:
            frame_time = 0.0
            self.frame = (self.frame + 1) % 5
        delay(0.5)
        frame_time += 0.5

    def update_hp(self):
        if self.hp > student.damage:
            self.hp -= student.damage
        else:
            self.hp = self.max_hp

    def draw(self):
        self.image.clip_draw(self.frame * 440, 0, 440, 275, self.x, self.y, 200, 150)
        self.image_hp.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)

def enter():
    global student, subject, room
    student = Student()
    subject = Subject()
    room = Room()


def exit():
    global student, subject, room
    del(student)
    del(subject)
    del(room)


def pause():
    pass


def resume():
    pass


def handle_events():
    global x, y, hit
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and (subject.x - 100 < x and x < subject.x + 100) and (subject.y - 75 < y and y < subject.y + 75):
            subject.hit = True
            student.gold += 10


def update():
    global hit
    subject.update()
    if subject.hit == True:
        subject.update_hp()
        subject.hit = False
    if student.hp < 100:
        student.update()
    else:
        game_framework.change_state(gameover_state)

def draw():
    clear_canvas()
    room.draw()
    student.draw()
    subject.draw()
    update_canvas()