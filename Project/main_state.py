import random
import json
import os

from pico2d import *

import game_framework
import title_state
import gameover_state

from room import Room
from student import Student
from subject import Subject
from randombox import Randombox

name = "MainState"

x, y = 0, 0

student = None
subject = None
room = None
randombox = None

def enter():
    global student, subject, room, randombox
    student = Student()
    subject = Subject()
    room = Room()
    randombox = []

def exit():
    global student, subject, room, randombox
    del(student)
    del(subject)
    del(room)
    del(randombox)


def pause():
    pass


def resume():
    pass


def collide(object, x, y):
    if object.x - object.x_range > x: return False
    if x > object.x + object.x_range: return False
    if object.y - object.y_range > y: return False
    if y > object.y + object.y_range: return False

    return True


def handle_events(frame_time):
    global x, y, randombox

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
                subject.update_hp(student)
                student.attack()
                if random.randint(0, 9) == 3 and len(randombox) == 0:
                    randombox.append(Randombox())
            for box in randombox:
                if collide(box, x, y):
                    box.open_box(student)
                    randombox.remove(box)


def update(frame_time):
    subject.update(frame_time)

    if student.hp < student.hp_max:
        student.update_hp(subject, frame_time)
    else:
        game_framework.change_state(gameover_state)


def draw(frame_time):
    clear_canvas()

    room.draw(frame_time)
    student.draw(frame_time)
    subject.draw(frame_time)
    for box in randombox:
        box.draw(frame_time)

    update_canvas()