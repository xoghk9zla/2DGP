import random
import json
import os

from pico2d import *

import game_framework
import title_state
import shop_state
import gameover_state
import help_state

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
font = None
warning_bgm = None
buy_bgm = None


def enter():
    global student, subject, room, randombox, warning_bgm, buy_bgm, font

    student = Student()
    subject = Subject()
    room = Room()
    randombox = []
    font = load_font('ENCR10B.TTF', 16)

    warning_bgm = load_music('sounds/effects/warning.mp3')
    warning_bgm.set_volume(128)

    buy_bgm = load_music('sounds/effects/buy.mp3')
    buy_bgm.set_volume(128)


def exit():
    global student, subject, room, randombox, warning_bgm, font

    del(student)
    del(subject)
    del(room)
    del(randombox)
    del(warning_bgm)
    del(font)


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
    global x, y, student, subject, randombox

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
                student.attack(subject)
                if random.randint(0, 99) < 15 and len(randombox) == 0:
                    randombox.append(Randombox())
                    for box in randombox:
                        box.take_box_sound.play()
                subject.update_hp(student)
            else:
                for box in randombox:
                    if collide(box, x, y):
                        box.open_box(student)
                        randombox.remove(box)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            room.bgm.pause()
            game_framework.push_state(shop_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            if subject.progress >= 5:
                buy_bgm.play()
                student.skill_self_cancel_a_class(subject)
            else:
                warning_bgm.play()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            if student.gold >= 300 * student.level / 3:
                buy_bgm.play()
                student.skill_drink()
            else:
                warning_bgm.play()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            game_framework.push_state(help_state)


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
    font.draw(700, 25, 'F1: help', (0, 0, 0))

    update_canvas()