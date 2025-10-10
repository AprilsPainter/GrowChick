# source/main.py
"""Scene의 전환을 관리"""

import pygame as py
from source.scenes.title_scene import TitleScene

screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
py.display.set_caption("Grow Chick!")

current_scene = "Title"

while True:
    if current_scene == "Title":
        scene = TitleScene(screen)

    elif current_scene == "Quit":
        break

    NEXT_SCENE = scene.run()
    current_scene = NEXT_SCENE

py.quit()
