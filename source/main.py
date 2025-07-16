import pygame as py
from scenes.mainscreen import show_main_screen

py.init()
screen = py.display.set_mode((0,0), py.FULLSCREEN)  # 1920 x 1080
py.display.set_caption("Grow Chick!")

show_main_screen(screen)

py.quit()