# source/scenes/kitchen.py

import os
import pygame as py
from source.model.status_window import StatusWindow
from source.model.system import System
from source.util.functions import load_img, show_img
from source.util.assets_manager import bg_path

py.init()

class Kitchen:
    def __init__(self, screen: py.Surface):
        self.screen = screen
        self.system = System()
        self.status_window = StatusWindow(self.screen, self.system)
        self.time_zone = self.system.get_time_zone()

        # 이미지 로드
        self.background_img = load_img(bg_path["kitchen"], (1920, 1080))

    def run(self):
        "주방 화면 루프 실행 및 이벤트 처리"

        self.screen.fill((0, 0, 0))

