"""스탯 창 기능"""
# source/model/status_window.py

import pygame as py
from source.util.functions import load_img, load_text, show_img, show_text
from source.util.assets_manager import path, scale, coords, font_path
from source.model.system import System
from source.model.button import Button
import config


class StatusWindow:
    """게임 화면에 스탯 창을 표시하고 관련 이벤트를 처리합니다."""

    def __init__(self, screen: py.Surface, system: System):
        self.screen = screen
        self.system = system
        self.minimize = False

        self.prev_day = None
        self.prev_actions = None

        # 상태창 프레임 이미지
        self.status_frame = load_img(path["status frame"], scale["status frame"])

        # 버튼
        self.buttons = {
            "minimize": Button(screen, path["minimize"], scale["minimize"], coords["minimize"]),
            "show": Button(screen, path["show"], scale["show"], coords["show"]),
            "bathroom": Button(screen, path["bathroom"], scale["bathroom"], coords["bathroom"]),
            "bedroom": Button(screen, path["bedroom"], scale["bedroom"], coords["bedroom"]),
            "kitchen": Button(screen, path["kitchen"], scale["kitchen"], coords["kitchen"]),
            "living_room": Button(screen, path["living room"],
                                    scale["living room"], coords["living room"]),
            "walk": Button(screen, path["walk"], scale["walk"], coords["walk"])
        }

        # 고정 텍스트 이미지
        self.texts = {
            "stat": load_text("스탯", font_path, 62),
            "charm": load_text("매력", font_path, 44),
            "fullness": load_text("포만감", font_path, 44),
            "hapiness": load_text("행복도", font_path, 44),
            "cleanliness": load_text("청결도", font_path, 44)
        }

        self.texts_coords = {
            "stat": (163, 180),
            "charm": (178, 384),
            "fullness": (154, 464),
            "hapiness": (154, 544),
            "cleanliness": (154, 624)
        }

        self.update_texts(force=True)

    def toggle(self):
        """스탯 창 최소화 상태를 전환합니다."""
        self.minimize = not self.minimize

    def update_texts(self, force: bool = False):
        """현재 날짜와 남은 행동 횟수 텍스트를 업데이트합니다."""
        day = self.system.get_day()
        actions = self.system.get_actions()

        if force or day != self.prev_day:
            self.text_day = load_text(f"{day}일차", font_path, 56)
            self.prev_day = day

        if force or actions != self.prev_actions:
            self.text_actions = load_text(f"잔여 행동 횟수: {actions}회", font_path, 35)
            self.prev_actions = actions

    def draw_stat_bars(self):
        """스탯 값에 따라 변화하는 막대 그래프를 그립니다."""
        bar_colors = config.STAT_BAR_COLORS
        bar_max_width = 220
        bar_height = 28
        bar_positions = {
            "매력": (250, 370),
            "포만감": (250, 450),
            "행복도": (250, 530),
            "청결도": (250, 610)
        }

        for stat_name, (x, y) in bar_positions.items():
            py.draw.rect(self.screen, (255, 255, 255),
                            (x, y, bar_max_width, bar_height), border_radius=4)

            value = self.system.get_stat(stat_name)
            filled = int(bar_max_width * (value / 100))

            py.draw.rect(self.screen, bar_colors.get(stat_name),
                            (x, y, filled, bar_height), border_radius=4)

    def draw(self):
        """스탯 창을 화면에 표시합니다."""
        self.update_texts()

        if not self.minimize:
            show_img(self.screen, self.status_frame, coords["status frame"])

            for button in self.buttons.values():
                button.draw()

            for key, text in self.texts.items():
                show_img(self.screen, text, self.texts_coords[key])

            show_text(self.screen, self.text_day, (405, 180))
            show_text(self.screen, self.text_actions, (279, 272))

            self.draw_stat_bars()
        else:
            self.buttons["show"].draw()

    def manage_event(self, event):
        """버튼 클릭 이벤트를 처리합니다."""
        if self.minimize:
            self.buttons["show"].manage_event(event)

            if (event.type == py.MOUSEBUTTONUP
                    and self.buttons["show"].rect.collidepoint(py.mouse.get_pos())):
                self.toggle()
            return

        # 최소화 버튼 처리
        self.buttons["minimize"].manage_event(event)
        if (event.type == py.MOUSEBUTTONUP
                and self.buttons["minimize"].rect.collidepoint(py.mouse.get_pos())):
            self.toggle()

        # 방 이동 버튼 처리
        for key in ["bathroom", "bedroom", "kitchen", "living_room", "walk"]:
            self.buttons[key].manage_event(event)
