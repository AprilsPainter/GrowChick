import pygame as py
from scenes.mainscreen import show_mainscreen
from scenes.map import show_map

py.init()
py.mixer.init()

screen = py.display.set_mode((640, 360))
py.display.set_caption("Grow Chick!")

clock = py.time.Clock()
fullscreen = False
running = True
current_scene = "main"

while running:
    events = py.event.get()

    # 종료 및 전체화면 조작
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

    if current_scene == "main":
        scene_result = show_mainscreen(screen, events)

        if scene_result == "map":
            current_scene = "map"

    elif current_scene == "map":
        scene_result = show_map_screen(screen, events)

        if scene_result == "main":
            current_scene = "main"

    py.display.update()
    clock.tick(60)

py.quit()