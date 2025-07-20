import pygame as py
from scenes.mainscreen import show_mainscreen

py.init()
py.mixer.init()

screen = py.display.set_mode((640, 360))
py.display.set_caption("Grow Chick!")

clock = py.time.Clock()
fullscreen = False
running = True

while running:
    events = py.event.get()

    for event in events:
        if event.type == py.QUIT:
            running = False

        elif event.type == py.KEYDOWN:
            if event.key == py.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)
                else:
                    screen = py.display.set_mode((640, 360))

    show_mainscreen(screen, events)
    
    py.display.update()
    clock.tick(60)

py.quit()