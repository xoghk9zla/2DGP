import game_framework
import main_state

from pico2d import *


name = "TitleState"
image = None
image_button = None
button_time = 0.0

def enter():
    global image, image_button
    image = load_image('images/states/title.png')
    image_button = load_image('images/states/title_button.png')

def exit():
    global image, image_button
    del(image)
    del(image_button)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_F5):
                game_framework.pop_state()


def draw(frame_time):
    global button_time

    clear_canvas()
    image.draw(400, 300)
    if button_time % 2 < 1:
        image_button.draw(400, 200, 600, 150)

    update_canvas()


def update(frame_time):
    global button_time
    button_time += frame_time
    pass


def pause():
    pass


def resume():
    pass