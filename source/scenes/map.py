import os
import pygame as py
from util.common import load_image
from model.GameManager import game_manager
from model.UI import UIButton


btn_park = btn_backstreet = btn_chickenstore = None
img_background = img_park = img_backstreet = img_chickenstore = None
initialized = False

def show_map(screen, events):
    global btn_park, btn_backstreet, btn_chickenstore
    global img_background, img_park, img_backstreet, img_chickenstore
    global initialized

    if not initialized:
        background_path = os.path.join("assets", "backgrounds", "background_map.png")
        park_path = os.path.join("assets", "ui", "icons", "button_park.png")
        backstreet_path = os.path.join("assets", "ui", "icons", "button_backstreet.png")
        chickenstore_path = os.path.join("assets", "ui", "icons", "button_chickenstore.png")

        img_background = load_image(background_path, scale=(1980, 1080))
        img_park = load_image(park_path, scale=(240, 135))
        img_backstreet = load_image(backstreet_path, scale=(240, 135))
        img_chickenstore = load_image(chickenstore_path, scale=(240, 135))

        s_width, s_height = screen.get_size()

        btn_park = UIButton(img_park, (s_width / 2, s_height / 3))
        btn_backstreet = UIButton(img_backstreet, (s_width / 2, s_height / 2))
        btn_chickenstore = UIButton(img_chickenstore, (s_width / 2, s_height * 2 / 3))

        initialized = True

    screen.blit(img_background, (0, 0))
    btn_park.draw(screen)
    btn_backstreet.draw(screen)
    btn_chickenstore.draw(screen)

    for event in events:
        if event.type == py.MOUSEBUTTONDOWN:
            if btn_park.click(event):
                result, item = game_manager.walk_manager.walk("공원", game_manager.chick)
                print(result, item)
                return "main"

            elif btn_backstreet.click(event):
                result, item = game_manager.walk_manager.walk("뒷골목", game_manager.chick)
                print(result, item)
                return "main"

            elif btn_chickenstore.click(event):
                result, item = game_manager.walk_manager.walk("치킨집", game_manager.chick)
                print(result, item)
                return "main"
