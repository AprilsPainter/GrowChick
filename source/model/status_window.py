"""스탯 창 기능"""
# source/model/status_window.py

import os
import pygame as py
from source.util.functions import load_img, load_text, show_img, show_text
from source.model.system import System
from source.model.button import Button
import config


class StatusWindow:
    """인게임 전반에서 스탯 창 표시 및 버튼 이벤트 관리."""

    def __init__(self, screen: py.Surface, system: System):
        """
        Args:
            screen (pygame.Surface): 화면 서피스.
            system (System): 게임 상태를 관리하는 싱글톤 System 객체.
        """
        self.screen = screen
        self.system = system
        self.minimize = False

        self.prev_day = None
        self.prev_actions = None

        self.status_frame_path = os.path.join("assets", "ui", "layout", "status-frame.png")
        self.minimize_btn_path = os.path.join("assets", "ui", "icons", "minimize-window.png")
        self.show_btn_path = os.path.join("assets", "ui", "icons", "show.png")

        self.room_btn_paths = {
            "bathroom": os.path.join("assets", "ui", "icons", "bathroom-button.png"),
            "bedroom": os.path.join("assets", "ui", "icons", "bedroom-button.png"),
            "kitchen": os.path.join("assets", "ui", "icons", "kitchen-button.png"),
            "living_room": os.path.join("assets", "ui", "icons", "living-room-button.png"),
            "walk": os.path.join("assets", "ui", "icons", "walk-button.png"),
        }

        self.status_frame = load_img(self.status_frame_path, scale=(888, 888))

        self.buttons = {
            "minimize": Button(screen, self.minimize_btn_path, (60, 60), (473, 957)),
            "show": Button(screen, self.show_btn_path, (60, 60), (85, 957)),
            "bathroom": Button(screen, self.room_btn_paths["bathroom"], (60, 60), (154, 800)),
            "bedroom": Button(screen, self.room_btn_paths["bedroom"], (60, 60), (154, 880)),
            "kitchen": Button(screen, self.room_btn_paths["kitchen"], (60, 60), (154, 960)),
            "living_room": Button(screen, self.room_btn_paths["living_room"], (60, 60), (234, 800)),
            "walk": Button(screen, self.room_btn_paths["walk"], (60, 60), (234, 880)),
        }

        self.text_stat = load_text("스탯", config.FONT_PATH, 62)
        self.text_charm = load_text("매력", config.FONT_PATH, 44)
        self.text_fullness = load_text("포만감", config.FONT_PATH, 44)
        self.text_happiness = load_text("행복도", config.FONT_PATH, 44)
        self.text_cleanliness = load_text("청결도", config.FONT_PATH, 44)

        self.update_texts(force=True)

    def toggle(self):
        """스탯 창 최소화 상태 토글."""
        self.minimize = not self.minimize

    def update_texts(self, force: bool = False):
        """System 상태 기반으로 최신 텍스트 생성."""
        day = self.system.get_day()
        actions = self.system.get_actions()

        if force or day != self.prev_day:
            self.text_day = load_text(f"{day}일차", config.FONT_PATH, 56)
            self.prev_day = day

        if force or actions != self.prev_actions:
            self.text_actions = load_text(f"잔여 행동 횟수: {actions}회", config.FONT_PATH, 35)
            self.prev_actions = actions

    def draw_stat_bars(self):
        """값에 따라 달라지는 스탯 바를 화면에 그림."""
        bar_colors = config.STAT_BAR_COLORS
        bar_max_width = 220
        bar_height = 28
        bar_positions = {
            "매력": (250, 370),
            "포만감": (250, 450),
            "행복도": (250, 530),
            "청결도": (250, 610),
        }

        for name, (x, y) in bar_positions.items():
            py.draw.rect(self.screen, (255, 255, 255), (x, y, bar_max_width, bar_height), border_radius=4)
            value = self.system.get_stat(name)
            filled_bar_width = int(bar_max_width * (value / 100))
            py.draw.rect(self.screen, bar_colors.get(name), (x, y, filled_bar_width, bar_height), border_radius=4)

    def draw(self):
        """화면에 스탯 창과 버튼, 텍스트, 스탯 바를 그림."""
        self.update_texts()

        if not self.minimize:
            show_img(self.screen, self.status_frame, (282, 562))
            for key in self.buttons.items():
                self.buttons[key].draw()

            show_text(self.screen, self.text_day, (405, 180))
            show_text(self.screen, self.text_stat, (163, 180))
            show_text(self.screen, self.text_actions, (279, 272))
            show_text(self.screen, self.text_charm, (178, 384))
            show_text(self.screen, self.text_fullness, (154, 464))
            show_text(self.screen, self.text_happiness, (154, 544))
            show_text(self.screen, self.text_cleanliness, (154, 624))

            self.draw_stat_bars()
        else:
            self.buttons["show"].draw()

    def manage_event(self, event):
        """버튼 클릭 및 호버 이벤트 관리."""
        if self.minimize:
            self.buttons["show"].manage_event(event)
            if event.type == py.MOUSEBUTTONUP and self.buttons["show"].rect.collidepoint(py.mouse.get_pos()):
                self.toggle()
        else:
            self.buttons["minimize"].manage_event(event)
            if event.type == py.MOUSEBUTTONUP and self.buttons["minimize"].rect.collidepoint(py.mouse.get_pos()):
                self.toggle()

            for key in ["bathroom", "bedroom", "kitchen", "living_room", "walk"]:
                self.buttons[key].manage_event(event)
