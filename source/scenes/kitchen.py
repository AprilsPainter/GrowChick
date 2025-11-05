# source/scenes/kitchen.py

import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
if os.path.join(BASE_DIR, "source") not in sys.path:
    sys.path.append(os.path.join(BASE_DIR, "source"))

import pygame as py
from source.model.status_window import StatusWindow
from source.model.system import System
from source.util.functions import load_img, load_text, show_img, show_text

py.init()

class Kitchen:
    def __init__(self, screen: py.Surface):
        self.screen = screen
        self.system = System()
        self.status_window = StatusWindow(self.screen, self.system)
        self.time_zone = self.system.get_time_zone()

        # 이미지 경로
        background_img_path = os.path.join("assets", "backgrounds", "kitchen.png")

        # 이미지 로드
        self.background_img = load_img(background_img_path, (1920, 1080))

    def run(self):
        "주방 화면 루프 실행 및 이벤트 처리"

        self.screen.fill((0, 0, 0))

