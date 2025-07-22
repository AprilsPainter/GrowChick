# source/scenes/mainscreen.py

import pygame as py
from util.common import load_image, render_text, center_blit
from util.colors import WHITE, YELLOW
from model.common import UIButton

def show_mainscreen(screen, events):

    screen.fill(WHITE)

    s_width, s_height = screen.get_size()

    text_title = render_text(
        "병아리를 키워라!",
        "assets", "ui", "fonts", "Paperlogy-8ExtraBold.ttf",
        size=200, color=YELLOW
    )

    center_blit(screen, text_title, 0.5, 0.375)

    img_play = load_image(
        "assets", "ui", "icons", "button_play.png",
        scale=(400, 400)
    )

    btn_play = UIButton(img_play, pos=(s_width * 0.5, s_height * 0.65))

    for event in events:
        if btn_play.click(event):
            print("추후 게임 시작 함수로 연결") # 임시 텍스트 출력
    
    btn_play.draw(screen)

    py.display.update()