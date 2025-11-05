# source/util/functions.py
"""개발에 필요한 함수 모듈"""

import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
if os.path.join(BASE_DIR, "source") not in sys.path:
    sys.path.append(os.path.join(BASE_DIR, "source"))

import pygame as py
py.init()

def load_text(text: str, font_path: str, size: int, color: tuple = None, bg_color: tuple = None):
    """텍스트 객체를 로드"""

    if not color:
        color = (0, 0, 0)

    font = py.font.Font(font_path, size)
    text_surface = font.render(text, True, color, bg_color)

    return text_surface

def show_text(screen, text_surface, coordinates: tuple):
    """텍스트 객체를 표시"""

    rect = text_surface.get_rect()
    rect.center = coordinates
    screen.blit(text_surface, rect)

    return rect

def load_img(img_path: str, scale: tuple = None):
    """이미지 객체를 로드"""

    image = py.image.load(img_path).convert_alpha()

    if scale:
        image = py.transform.scale(image, scale)

    return image

def show_img(screen, img_surface, coordinates: tuple):
    """이미지 객체를 표시"""

    rect = img_surface.get_rect()
    rect.center = coordinates
    screen.blit(img_surface, rect)

    return rect