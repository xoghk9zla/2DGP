import game_framework
import title_state
import main_state

from pico2d import *


name = "GameoverState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('gameover.png')


def exit():
    global image
    del(image)


def update(frame_time):
    global logo_time

    if logo_time > 3.0:
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass




