# source/main.py

import pygame as py
import os
from util.functions import load_text, load_img, show_img, show_text
from util.colors import LEMON, ORANGE
from util.paths import text_font_path, title_font_path

py.init()

screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
py.display.set_caption("Grow Chick!")

Title = load_text("병아리를 키워라!", title_font_path, 180, ORANGE)

play_btn_path = os.path.join("assets", "ui", "icons", "button_play.png")
btn_PLAY = load_img(play_btn_path, (450, 189))

running = True
f11 = False

while running:
    screen.fill(LEMON)  # 배경 이미지 임시로 대체

    show_text(Title, 0.5, 0.35, screen)
    show_img(btn_PLAY, 0.5, 0.65, screen)

    events = py.event.get()
    for event in events:
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN and event.key == py.K_F11:
            f11 = not f11
            if f11:
                py.display.set_mode((1900, 1020))
            else:
                py.display.set_mode((1920, 1080), py.FULLSCREEN)
            
    py.display.update()

py.quit()