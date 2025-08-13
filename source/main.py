# source/main.py

import pygame as py
from util.colors import LEMON, ORANGE
from util.loading import load_image, load_text, surface_blit

py.init()

screen = py.display.set_mode((640, 360))
py.display.set_caption("Grow Chick!")

title = load_text("assets", "ui", "fonts", "Paperlogy-8ExtraBold.ttf", text="병아리를 키워라!", size=180, color=ORANGE)
btn_play = load_image("assets", "ui", "icons", "button_play.png", scale=(500, 500))

running = True
full_screen = False

while running:
    events = py.event.get()
    for event in events:
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN and event.key == py.K_f:
            full_screen = not full_screen
            if full_screen:
                screen = py.display.set_mode((640, 360))
            else:
                screen = py.display.set_mode((0, 0), py.FULLSCREEN)

    sw, sh = screen.get_size()
    title_rect = title.get_rect(center=(sw * 0.5, sh * 0.375))

    screen.fill(LEMON)
    screen.blit(title, title_rect)
    surface_blit(screen, btn_play, 0.5, 0.625)
    py.display.update()

py.quit()