# source/scenes/title_scene.py
"""타이틀 화면(메인 화면)"""

import os
import pygame as py
from source.util.functions import load_img, show_img

py.init()

class TitleScene:
    """타이틀 화면 구성과 기능을 관리하는 클래스"""

    def __init__(self, screen):

        self.f11 = False
        self.screen = screen

        bg_path = os.path.join("assets", "backgrounds", "TitleScreen_bg.png")
        self.bg = load_img(bg_path, scale=(1920, 1080))

        play_btn_path = os.path.join("assets", "ui", "icons", "PLAY_btn.png")
        self.play_btn = load_img(play_btn_path, scale=(296, 128))
        self.play_btn_rect = None

        quit_btn_path = os.path.join("assets", "ui", "icons", "QUIT_btn.png")
        self.quit_btn = load_img(quit_btn_path, scale=(296, 128))
        self.quit_btn_rect = None

        config_path = os.path.join("assets", "ui", "icons", "Config_btn.png")
        self.config_btn = load_img(config_path, scale=(128, 128))
        self.config_btn_rect = None

    def run(self):
        """객체를 화면에 표시하고 실행 중 기능을 관리"""

        running = True

        while running:

            show_img(self.bg, 0.5, 0.5, self.screen)
            self.play_btn_rect = show_img(self.play_btn, 0.5, 0.75, self.screen)
            self.quit_btn_rect = show_img(self.quit_btn, 0.1, 0.075, self.screen)
            self.config_btn_rect = show_img(self.config_btn, 0.95, 0.1, self.screen)

            events = py.event.get()

            for event in events:

                if event.type == py.QUIT:
                    running = False

                elif event.type == py.KEYDOWN and event.key == py.K_F11:
                    self.f11 = not self.f11

                    if self.f11:
                        self.screen = py.display.set_mode((1910, 1020))
                    else:
                        self.screen = py.display.set_mode((1920, 1080), py.FULLSCREEN)

                elif event.type == py.MOUSEBUTTONDOWN:
                    if self.play_btn_rect.collidepoint(event.pos):
                        return "Living room"

            py.display.update()

        py.quit()
