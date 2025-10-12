# source/main.py
"""Scene의 전환을 관리"""

import pygame as py
from source.scenes.title_scene import TitleScene
from source.scenes.living_room import LivingRoom

screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
py.display.set_caption("Grow Chick!")

current_scene = "title"

while True:
    if current_scene == "quit":
        break
    
    elif current_scene == "title":
        scene = TitleScene(screen)
        
    elif current_scene == "living room":
        scene = LivingRoom(screen)

    next_scene = scene.run()
    current_scene = next_scene

py.quit()
