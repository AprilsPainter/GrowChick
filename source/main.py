# source/main.py

import pygame as py
from scenes.title_scene import TitleScene

screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
py.display.set_caption("Grow Chick!")

current_scene = "Title"

while True:
    if current_scene == "Title":
        scene = TitleScene(screen)
    
    elif current_scene == "Quit":
        break

    next_scene = scene.run()
    current_scene = next_scene

py.quit()