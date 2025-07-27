# source/main.py

import pygame as py
from util.Colors import LEMON

py.init()

mini_screen = (640, 360)
full_screen = py.FULLSCREEN

screen = py.display.set_mode((mini_screen))
py.display.set_caption("Grow Chick!")
screen.fill(LEMON)

running = True
events = py.event.get()

while running:
    for event in events:
        if event == py.QUIT:
            running = False

    py.display.update()

py.quit()