import random
import json
import os

from pico2d import *

import game_framework
import main_state

name = "ShopState"


class Hp_max_up:
    def __init__(self):
        self.x, self.y = 150, 425
        self.x_range, self.y_range = 75 / 2, 75 / 2
        self.price = 1000
        self.increment = 5
        self.explain = 'Increase the student`s max hp.'
        self.image = load_image('images/shop/hp_shop.png')

    def draw(self, frame_time):
        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        main_state.student.hp_max += self.increment
        main_state.student.gold -= self.price
        self.price += 500
        pass


class Damage_up:
    def __init__(self):
        self.x, self.y = 150, 325
        self.x_range, self.y_range = 75 / 2, 75 / 2
        self.price = 1000
        self.increment = 1
        self.explain = 'Increase the student`s damage.'
        self.image = load_image('images/shop/dmg_shop.png')

    def draw(self, frame_time):
        self.image.draw(self.x, self.y)
        pass

    def update(self, frame_time):
        main_state.student.damage += self.increment
        main_state.student.gold -= self.price
        self.price += 500
        pass


x, y = 0, 0

background_image = None
hp_max_up = None
damage_up = None
new_game = True

def enter():
    global background_image, hp_max_up, damage_up, new_game

    if new_game:
        background_image = load_image('images/shop/shop.png')
        hp_max_up = Hp_max_up()
        damage_up = Damage_up()
        new_game = False
    pass


def exit():
    global background_image, hp_max_up, damage_up
    if new_game:
        del(background_image)
        del(hp_max_up)
        del(damage_up)
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global x, y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            main_state.room.bgm.resume()
            game_framework.push_state(main_state)
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if main_state.collide(hp_max_up, x, y):
                if main_state.student.gold > hp_max_up.price:
                    main_state.buy_bgm.play()
                    hp_max_up.update(frame_time)
                else:
                    main_state.warning_bgm.play()
            elif main_state.collide(damage_up, x, y):
                if main_state.student.gold > damage_up.price:
                    main_state.buy_bgm.play()
                    damage_up.update(frame_time)
                else:
                    main_state.warning_bgm.play()
        pass


def update(frame_time):
    pass


def draw(frame_time):
    clear_canvas()
    background_image.draw(400, 300)
    main_state.font.draw(50, 500, 'GOLD: %d' % main_state.student.gold, (255, 228, 0))

    hp_max_up.draw(frame_time)
    main_state.font.draw(hp_max_up.x + 50, hp_max_up.y + 25, 'PRICE: %d' % hp_max_up.price, (0, 0, 0))
    main_state.font.draw(hp_max_up.x + 50, hp_max_up.y, 'INCREMENT: %d' % hp_max_up.increment, (0, 0, 0))
    main_state.font.draw(hp_max_up.x + 50, hp_max_up.y - 25, 'EXPLAIN: %s' % hp_max_up.explain, (0, 0, 0))

    damage_up.draw(frame_time)
    main_state.font.draw(damage_up.x + 50, damage_up.y + 25, 'PRICE: %d' % damage_up.price, (0, 0, 0))
    main_state.font.draw(damage_up.x + 50, damage_up.y, 'INCREMENT: %d' % damage_up.increment, (0, 0, 0))
    main_state.font.draw(damage_up.x + 50, damage_up.y - 25, 'EXPLAIN: %s' % damage_up.explain, (0, 0, 0))
    update_canvas()