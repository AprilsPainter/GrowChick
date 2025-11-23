"""거실 Scene"""
# source/scenes/living_room.py

import os
import pygame as py
from source.model.system import System
from source.util.functions import load_img, show_img
from source.util.assets_manager import bg_path

class LivingRoom:
    """거실 씬: 배경 표시, 전체화면 토글, 이벤트 처리"""

    def __init__(self, screen: py.Surface, system: System):
        self.screen = screen
        self.system = system
        self.fullscreen = True
        self.next_scene_name = None

        self.background_day = load_img(
            bg_path["living room day"],
            scale=(1920, 1080),
        )
        self.background_evening = load_img(
            bg_path["living room evening"],
            scale=(1920, 1080),
        )
        self.background_night = load_img(
            bg_path["living room night"],
            scale=(1920, 1080),
        )

    def update(self):
        """씬 업데이트 처리 (필요 시 구현)"""
        pass

    def draw(self):
        """현재 시간대에 맞는 배경 이미지를 화면에 그림"""
        time_zone = self.system.get_time_zone()
        if time_zone == "day":
            show_img(self.screen, self.background_day, (960, 540))
        elif time_zone == "evening":
            show_img(self.screen, self.background_evening, (960, 540))
        elif time_zone == "night":
            show_img(self.screen, self.background_night, (960, 540))

    def manage_event(self, event):
        """이벤트 관리"""
        if event.type == py.QUIT:
            self.next_scene_name = "quit"
        elif event.type == py.KEYDOWN and event.key == py.K_F11:
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                py.display.set_mode((1920, 1080), py.FULLSCREEN)
            else:
                py.display.set_mode((1890, 1060))
