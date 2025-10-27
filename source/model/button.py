import pygame as py
from source.util.functions import load_img, show_img

class Button:
    """버튼 이미지 표시 및 이벤트 처리 관리"""

    def __init__(self, screen, image_path: str, scale: tuple, coordinates: tuple = None):
        self.screen = screen
        self.image = load_img(image_path, scale)
        self.coordinates = coordinates
        self.rect = None
        self.hovered = False
        self.clicked = False
        self.scale = scale

    def draw(self):
        """버튼 이미지 표시 및 rect 생성"""
        self.rect = show_img(self.screen, self.image, self.coordinates)

    def manage_event(self, event):
        """클릭/호버 이벤트 관리 및 사이즈 변경"""

        if event.type == py.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.clicked = True
            self.change_size()

        elif event.type == py.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
            self.change_size()

    def change_size(self):
        """클릭/호버 여부에 따라 버튼 이미지 크기 변경"""

        if self.hovered and not self.clicked:
            hovered_scale = (int(self.scale[0] * 1.5), int(self.scale[1] * 1.5))
            self.image = py.transform.scale(self.image, hovered_scale)

        elif self.hovered and self.clicked:
            self.image = py.transform.scale(self.image, self.scale)
