# source/model/status_window.py

import os
import pygame as py
from source.util.functions import load_img, load_text, show_img, show_text
from source.model.system import System
import config

py.init()


class StatusWindow:
    """인게임 전반에서 스탯 창 표시"""

    def __init__(self, screen, system: System):
        self.screen = screen
        self.system = system
        self.minimize = False

        # day, actions 이전 값 캐싱
        self.prev_day = None
        self.prev_actions = None

        # rect 초기화
        self.minimize_rect = None
        self.show_rect = None

        # 이미지 경로
        status_frame_path = os.path.join("assets", "ui", "layout", "status-frame.png")
        minimize_btn_path = os.path.join("assets", "ui", "icons", "minimize-window.png")
        show_btn_path = os.path.join("assets", "ui", "icons", "show.png")

        # 이미지 로드
        self.status_frame = load_img(status_frame_path, scale=(888, 888))
        self.minimize_btn = load_img(minimize_btn_path, scale=(60, 60))
        self.show_btn = load_img(show_btn_path, scale=(60, 60))

        # 고정 텍스트 로드
        self.text_stat = load_text("스탯", config.FONT_PATH, 62)
        self.text_charm = load_text("매력", config.FONT_PATH, 44)
        self.text_fullness = load_text("포만감", config.FONT_PATH, 44)
        self.text_happiness = load_text("행복도", config.FONT_PATH, 44)
        self.text_cleanliness = load_text("청결도", config.FONT_PATH, 44)

        # 초기 동적 텍스트 생성
        self.update_texts(force=True)

    def toggle(self):
        """스탯 창 최소화 토글"""

        self.minimize = not self.minimize

    def update_texts(self, force=False):
        """System 상태 기반으로 최신 텍스트 생성"""

        day = self.system.get_day()
        actions = self.system.get_actions()

        if force or day != self.prev_day:           # force=True거나 기존 값과 현재 값이 달라졌을 때
            self.text_day = load_text(f"{day}일차", config.FONT_PATH, 56)
            self.prev_day = day

        if force or actions != self.prev_actions:   # force=True거나 기존 값과 현재 값이 달라졌을 때
            self.text_actions = load_text(f"잔여 행동 횟수: {actions}회", config.FONT_PATH, 35)
            self.prev_actions = actions

    def draw_stat_bars(self):
        """값에 따라 달라지는 스탯 바를 그림"""

        bar_colors = config.STAT_BAR_COLORS

        bar_max_width = 220
        bar_height = 28

        bar_positions = {
            "매력": (250, 370),
            "포만감": (250, 450),
            "행복도": (250, 530),
            "청결도": (250, 610)
        }

        for name, (x, y) in bar_positions.items():
            empty_bar = (x, y, bar_max_width, bar_height)
            py.draw.rect(self.screen, (255, 255, 255), empty_bar, border_radius=4)

            value = self.system.get_stat(name)
            filled_bar_width = int(bar_max_width * (value / 100))
            filled_bar = (x, y, filled_bar_width, bar_height)
            bar_color = bar_colors.get(name)
            py.draw.rect(self.screen, bar_color, filled_bar, border_radius=4)

    def draw(self):
        """화면에 최신 상태 객체를 그림"""

        self.update_texts()

        if not self.minimize:
            show_img(self.screen, self.status_frame, (282, 562))
            self.minimize_rect = show_img(self.screen, self.minimize_btn, (473, 957))

            # 텍스트 그리기
            show_text(self.screen, self.text_day, (405, 180))
            show_text(self.screen, self.text_stat, (163, 180))
            show_text(self.screen, self.text_actions, (279, 272))
            show_text(self.screen, self.text_charm, (178, 384))
            show_text(self.screen, self.text_fullness, (154, 464))
            show_text(self.screen, self.text_happiness, (154, 544))
            show_text(self.screen, self.text_cleanliness, (154, 624))

            self.draw_stat_bars()

        else:
            self.show_rect = show_img(self.screen, self.show_btn, (85, 957))

    def manage_event(self, event):
        """클릭 이벤트 제어"""

        if event.type == py.MOUSEBUTTONDOWN:
            if not self.minimize and self.minimize_rect and self.minimize_rect.collidepoint(event.pos):
                self.toggle()
            elif self.minimize and self.show_rect and self.show_rect.collidepoint(event.pos):
                self.toggle()
