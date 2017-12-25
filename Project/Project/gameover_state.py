import game_framework
import title_state
import main_state

from pico2d import *


name = "GameoverState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('images/states/gameover.png')


def exit():
    global image
    del(image)


def update(frame_time):
    global logo_time

    if logo_time > 3:
        logo_time = 0
        game_framework.change_state(title_state)
    logo_time += frame_time


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    pass


def pause(): pass


def resume(): pass




