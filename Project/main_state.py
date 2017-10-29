import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

student = None
room = None
font = None

frame_time = 0.0


class Room:
    def __init__(self):
        self.image = load_image('room.png')

    def draw(self):
        self.image.draw(400, 300)


class Student:
    def __init__(self):
        self.hp_x, self.hp_y = 200, 525
        self.hp = 100
        self.stress = 0
        self.image = load_image('hp_e.png')

    def update(self):
        delay(0.5)
        self.stress += 1
        if self.stress == 100:
            self.stress = 0

    def draw(self):
        self.image.clip_draw(0, 0, 2200 , 100, self.hp_x, self.hp_y, 2.2 * self.stress, 25)


class Enemy:
    def __init__(self):
        self.x, self.y = 600, 400
        self.hp_x, self.hp_y = 600, 525
        self.hp = 100
        self.frame = 0
        self.image = load_image('Enemy_C.png')
        self.image_hp = load_image('hp_e.png')

    def update(self):
        global frame_time
        if frame_time > 1.0:
            frame_time = 0.0
            self.frame = (self.frame + 1) % 5
        delay(0.01)
        frame_time += 0.01


    def draw(self):
        self.image.clip_draw(self.frame * 440, 0, 440, 275, self.x, self.y, 200, 150)
        self.image_hp.clip_draw(0, 0, 2200, 100, self.hp_x, self.hp_y, 2.2 * self.hp, 25)

def enter():
    global student, enemy, room
    student = Student()
    enemy = Enemy()
    room = Room()


def exit():
    global student, enemy, room
    del(student)
    del(enemy)
    del(room)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            game_framework.change_state(title_state)


def update():
    student.update()
    enemy.update()


def draw():
    clear_canvas()
    room.draw()
    student.draw()
    enemy.draw()
    update_canvas()