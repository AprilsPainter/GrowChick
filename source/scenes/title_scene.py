"""타이틀 Scene"""
# source/scenes/title_scene.py

import os
import pygame as py
from source.model.system import System
from source.util.functions import load_img, show_img
from source.model.button import Button


class TitleScene:
    """타이틀 씬: 배경, 버튼 표시 및 씬 전환 처리."""

    def __init__(self, screen: py.Surface, system: System):
        self.screen = screen
        self.system = system
        self.fullscreen = True
        self.next_scene_name = None

        py.display.set_caption("Grow Chick!")

        self.background = load_img(
            os.path.join("assets", "backgrounds", "title-screen.png"),
            scale=(1920, 1080)
        )

        # 버튼 이미지 경로
        play_path = os.path.join("assets", "ui", "icons", "play-bar.png")
        setting_path = os.path.join("assets", "ui", "icons", "setting.png")
        info_path = os.path.join("assets", "ui", "icons", "information.png")
        exit_path = os.path.join("assets", "ui", "icons", "exit.png")

        self.buttons = {
            "play": Button(self.screen, play_path, scale=(408, 176), coordinates=(960, 678)),
            "setting": Button(self.screen, setting_path, scale=(138, 138), coordinates=(960, 917)),
            "info": Button(self.screen, info_path, scale=(130, 130), coordinates=(777, 917)),
            "exit": Button(self.screen, exit_path, scale=(120, 120), coordinates=(1151, 917))
        }


    def draw(self):
        """타이틀 화면과 버튼을 화면에 그림."""

        self.screen.fill((0, 0, 0))
        show_img(self.screen, self.background, (960, 540))

        for key, button in self.buttons.items():
            button.draw()

    def manage_event(self, event):
        """버튼 클릭 및 전체화면 토글 이벤트 처리."""

        if event.type == py.QUIT:       # 창 닫기
            self.next_scene_name = "quit"

        elif event.type == py.MOUSEBUTTONDOWN:      # 버튼 클릭
            if self.buttons["play"].rect.collidepoint(event.pos):
                self.next_scene_name = "living room"
            elif self.buttons["quit"].rect.collidepoint(event.pos):
                self.next_scene_name = "quit"

        elif event.type == py.KEYDOWN and event.key == py.K_F11:        # F11(전체화면 토글)
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                py.display.set_mode((1920, 1080), py.FULLSCREEN)
            else:
                py.display.set_mode((1890, 1060))
