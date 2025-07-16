import pygame as py
import os

def show_main_screen(screen):
    clock = py.time.Clock()
    running = True

    btn_path = os.path.join("assets", "ui", "icons", "button_play.png")
    font_path = os.path.join("assets", "ui", "fonts", "Paperlogy-8ExtraBold.ttf")

    font = py.font.Font(font_path, 128)
    
    play_button = py.image.load(btn_path)
    play_button = py.transform.scale(play_button, (256, 256))
    play_button_rect = play_button.get_rect(center = (400, 400))

    title_text = font.render("병아리를 키워라!", True, (255, 186, 0))
    title_text_rect = title_text.get_rect(center = (400, 200))

    while running:
        screen.fill((255, 255, 255))

        screen.blit(title_text, title_text_rect)
        screen.blit(play_button, play_button_rect)

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

            elif event.type == py.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    print("게임 시작!") # 추후 게임 시작 함수로 연결
                    running = False

        py.display.update()
        clock.tick(60)
