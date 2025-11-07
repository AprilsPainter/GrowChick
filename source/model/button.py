# source/model/button.py

import pygame as py
from source.util.functions import load_img, show_img


class Button:
    """버튼 이미지 표시 및 이벤트 처리 관리"""

    def __init__(self, screen, image_path: str, scale: tuple = None, coordinates: tuple = None):
        self.screen = screen
        self.image_path = image_path
        self.scale = scale
        self.coordinates = coordinates

        self.original_image = load_img(image_path, scale)
        self.image = self.original_image.copy()

        self.rect = None
        self.hovered = False
        self.clicked = False

    def draw(self):
        """버튼 이미지 표시 및 rect 반환"""
        self.rect = show_img(self.screen, self.image, self.coordinates)
        return self.rect

    def manage_event(self, event):
        """클릭/호버 이벤트 관리 및 크기 변경"""
        if self.rect is None:
            return

        if event.type == py.MOUSEMOTION:
            hovered_now = self.rect.collidepoint(event.pos)
            if hovered_now != self.hovered:
                self.hovered = hovered_now
                self.update_image()

        elif event.type == py.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.clicked = True
            self.update_image()

        elif event.type == py.MOUSEBUTTONUP:
            if self.clicked and self.rect.collidepoint(event.pos):
                self.on_click()
            self.clicked = False
            self.update_image()

    def update_image(self):
        """상태에 따른 이미지 스케일 업데이트"""
        if self.clicked:
            scale_factor = 0.9
        elif self.hovered:
            scale_factor = 1.1
        else:
            scale_factor = 1.0

        if self.scale:
            new_scale = (int(self.scale[0] * scale_factor), int(self.scale[1] * scale_factor))
            self.image = py.transform.scale(self.original_image, new_scale)

    def on_click(self):
        """버튼 클릭 시 동작"""
        pass
