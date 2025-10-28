# source/scenes/living_room.py
"""거실, 인게임 기본 장소 Scene"""

import os
import pygame as py
from source.model.status_window import StatusWindow
from source.util.functions import load_img, show_img
from source.model.system import System

py.init()


class LivingRoom:
    """거실 화면 표시 및 전체화면(F11) 토글 처리"""

    def __init__(self, screen: py.Surface):
        self.screen = screen
        self.fullscreen = True

        # 배경 이미지 경로
        self.background_day_path = os.path.join("assets", "backgrounds", "living-room_day.png")
        self.background_evening_path = os.path.join("assets", "backgrounds", "living-room_evening.png")
        self.background_night_path = os.path.join("assets", "backgrounds", "living-room_night.png")

        # 배경 이미지 로드
        self.background_day = load_img(self.background_day_path, scale=(1920, 1080))
        self.background_evening = load_img(self.background_evening_path, scale=(1920, 1080))
        self.background_night = load_img(self.background_night_path, scale=(1920, 1080))

        self.system = System()
        self.status_window = StatusWindow(self.screen, self.system)

    def run(self) -> str:
        """거실 화면 루프 실행 및 이벤트 처리"""
        clock = py.time.Clock()

        while True:
            # FPS 제한 (불필요한 과부하 방지)
            clock.tick(60)

            # 화면 초기화
            self.screen.fill((0, 0, 0))

            # 현재 시간대에 맞는 배경 표시
            time_zone = self.system.get_time_zone()
            if time_zone == "day":
                show_img(self.screen, self.background_day, (960, 540))
            elif time_zone == "evening":
                show_img(self.screen, self.background_evening, (960, 540))
            elif time_zone == "night":
                show_img(self.screen, self.background_night, (960, 540))

            # 스탯 창 표시
            self.status_window.draw()

            # 이벤트 처리
            for event in py.event.get():
                self.status_window.manage_event(event)

                if event.type == py.QUIT:
                    return "quit"

                # 전체화면 토글(F11)
                elif event.type == py.KEYDOWN and event.key == py.K_F11:
                    self.fullscreen = not self.fullscreen
                    if not self.fullscreen:
                        py.display.set_mode((1890, 1060))
                    else:
                        py.display.set_mode((1920, 1080), py.FULLSCREEN)

            # 화면 업데이트
            py.display.update()
