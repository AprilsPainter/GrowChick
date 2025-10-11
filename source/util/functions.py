# source/util/funtions.py
"""개발에 필요한 함수 모듈"""

import pygame as py
py.init()

def load_text(text, font_path, size, color, bg_color=None):
    """텍스트 객체를 로드"""

    font = py.font.Font(font_path, size)
    text_surface = font.render(text, True, color, bg_color)
    return text_surface

def show_text(screen, text_surface, w_r=None, h_r=None, x_c=None, y_c=None):
    """텍스트 객체를 표시"""

    if x_c and y_c:
        rect = text_surface.get_rect()
        rect.center = (x_c, y_c)
        screen.blit(text_surface, rect)
        
    elif w_r and h_r:
        w, h = screen.get_size()
        x = w * w_r
        y = h * h_r
        
        rect = text_surface.get_rect()
        rect.center = (x, y)
        screen.blit(text_surface, rect)
        
    return rect    

def load_img(img_path, scale=None):
    """이미지 객체를 로드"""

    image = py.image.load(img_path).convert_alpha()

    if scale:
        image = py.transform.scale(image, scale)

    return image

def show_img(screen, img_surface, w_r=None, h_r=None, x_c=None, y_c=None):
    """이미지 객체를 표시"""

    if w_r and h_r:
        screen_width, screen_height = screen.get_size()
        x = screen_width * width_ratio
        y = screen_height * height_ratio

        rect = img_surface.get_rect()
        rect.center = (x, y)
        screen.blit(img_surface, rect)
        
    elif x_c and y_c:
        rect = img_surface.get_rect()
        rect.center = (x_c, y_c)
        screen.blit(img_surface, rect)
        
    return rect
