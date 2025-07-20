import pygame as py
import os

# 이미지 로드 함수(경로, 사이즈(선택))
def load_image(*path_parts, scale = None):    
    path = os.path.join(*path_parts)
    image = py.image.load(path).convert_alpha()
    if scale:
        image = py.transform.scale(image, scale)
    return image

# 효과음 로드 함수(경로)
def load_sound(*path_parts):
    path = os.path.join(*path_parts)
    return py.mixer.Sound(path)

# 텍스트 렌더 함수(텍스트, 폰트 경로, 사이즈, 색상)
def render_text(text, *font_path_parts, size, color):
    font_path = os.path.join(*font_path_parts)
    font = py.font.Font(font_path, size)
    return font.render(text, True, color)

# (화면 비율 이용) UI 가운데 기준 정렬 및 블릿 함수(스크린, UI, 가로 비율, 세로 비율)
def center_blit(screen, surface, x_ratio, y_ratio):
    s_width, s_height = screen.get_size()
    rect = surface.get_rect(center = (s_width * x_ratio, s_height * y_ratio))
    screen.blit(surface, rect)
    return rect