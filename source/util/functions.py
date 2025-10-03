# source/util/funtions.py

import pygame as py
py.init()


# 텍스트 객체 로드
def load_text(text, font_path, size, color, bg_color=None):

    font = py.font.Font(font_path, size)
    text_surface = font.render(text, True, color, bg_color)
    return text_surface

# 텍스트 객체 화면에 표시
def show_text(text_surface, width_ratio, height_ratio, screen):

    screen_width, screen_height = screen.get_size()
    x = screen_width * width_ratio
    y = screen_height * height_ratio

    rect = text_surface.get_rect()
    rect.center = (x, y)

    screen.blit(text_surface, rect)

    return rect

# 이미지 객체 로드
def load_img(img_path, scale=None):

    image = py.image.load(img_path).convert_alpha()

    if scale:
        image = py.transform.scale(image, scale)

    return image

# 이미지 객체 화면에 표시
def show_img(img_surface, width_ratio, height_ratio, screen):

    screen_width, screen_height = screen.get_size()
    x = screen_width * width_ratio
    y = screen_height * height_ratio
    
    rect = img_surface.get_rect()
    rect.center = (x, y)

    screen.blit(img_surface, rect)

    return rect
