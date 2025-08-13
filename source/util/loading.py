# source/util.common.py

import pygame as py
import os

def load_image(*path_parts, scale = None):
    path = os.path.join(*path_parts)
    image = py.image.load(path).convert_alpha()
    if scale:
        image = py.transform.scale(image, scale)
    return image

def load_text(*path_parts, text, size, color):
    path = os.path.join(*path_parts)
    font = py.font.Font(path, size)
    text = font.render(text, True, color)
    return text

def load_sound(path_parts):
    sound = os.path.join(*path_parts)
    return sound

def surface_blit(screen, surface, x_r, y_r):
    sw, sh = screen.get_size()
    rect = surface.get_rect(center=(sw * x_r, sh * y_r))
    screen.blit(surface, rect)