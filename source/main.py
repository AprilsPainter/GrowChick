# source/main.py

import pygame as py
from scenes.title_scene import TitleScene

py.init()

screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
py.display.set_caption("Grow Chick!")

current_scene = "title"

while True:
    if current_scene == "title":
        scene = TitleScreen(screen)
        
    elif current_scene == "quit":
        break

    next_scene = scene.run()
    current_scene = next_scene

py.quit