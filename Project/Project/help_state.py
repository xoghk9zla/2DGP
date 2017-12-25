import random
import json
import os

from pico2d import *

import game_framework
import main_state

name = "HelpState"

image = None


def enter():
    global image
    image = load_image('images/states/help.png')

    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            game_framework.pop_state()
        pass


def update(frame_time):
    pass


def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    main_state.font.draw(700, 25, 'F1: back', (0, 0, 0))
    update_canvas()