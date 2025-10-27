"""타이틀 화면"""

import os
import pygame as py
from source.util.functions import load_img, show_img

py.init()


class TitleScene:
    """타이틀 화면 표시 및 이벤트 처리"""

    def __init__(self, screen: py.Surface):
        self.screen = screen
        self.fullscreen_enabled = False

        py.display.set_caption("Grow Chick!")

        # 이미지 경로
        background_path = os.path.join("assets", "backgrounds", "title-screen.png")
        play_button_path = os.path.join("assets", "ui", "icons", "play-bar.png")
        setting_button_path = os.path.join("assets", "ui", "icons", "setting.png")
        info_button_path = os.path.join("assets", "ui", "icons", "information.png")
        exit_button_path = os.path.join("assets", "ui", "icons", "exit.png")

        # 이미지 로드
        self.background = load_img(background_path, scale=(1920, 1080))
        self.play_button = load_img(play_button_path, scale=(408, 176))
        self.setting_button = load_img(setting_button_path, scale=(138, 138))
        self.info_button = load_img(info_button_path, scale=(130, 130))
        self.exit_button = load_img(exit_button_path, scale=(120, 120))

    def run(self) -> str:
        """타이틀 화면 루프 및 이벤트 처리"""
        while True:
            self.screen.fill((0, 0, 0))

            # 이미지 중심 좌표 튜플
            background_center = (960, 540)
            play_center = (960, 678)
            setting_center = (960, 917)
            info_center = (777, 917)
            exit_center = (1151, 917)

            # show_img 호출 시 **위치 매개변수로 튜플 전달**
            show_img(self.screen, self.background, background_center)
            play_rect = show_img(self.screen, self.play_button, play_center)
            setting_rect = show_img(self.screen, self.setting_button, setting_center)
            info_rect = show_img(self.screen, self.info_button, info_center)
            exit_rect = show_img(self.screen, self.exit_button, exit_center)

            # 이벤트 처리
            for event in py.event.get():
                if event.type == py.QUIT:
                    return "quit"

                elif event.type == py.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(event.pos):
                        return "living room"
                    elif setting_rect.collidepoint(event.pos):
                        # TODO: SettingScene 호출
                        pass
                    elif info_rect.collidepoint(event.pos):
                        # TODO: InfoScene 호출
                        pass
                    elif exit_rect.collidepoint(event.pos):
                        return "quit"

                elif event.type == py.KEYDOWN and event.key == py.K_F11:
                    self.fullscreen_enabled = not self.fullscreen_enabled
                    if self.fullscreen_enabled:
                        py.display.set_mode((1890, 1060))
                    else:
                        py.display.set_mode((1920, 1080), py.FULLSCREEN)

            py.display.update()
