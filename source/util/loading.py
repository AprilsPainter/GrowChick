# source/util.common.py

import pygame as py
import os

def load_image(*path_parts, scale = None):
    image = os.path.join(path_parts)
    py.transform.scale(image, scale)
    return image

def load_text(text, *path_parts, size, color):
    path = os.path.join(path_parts)
    font = py.font.Font(path, size)
    text = font.render(text, True, color)
    return text

def load_sound(*path_parts):
    sound = os.path.join(path_parts)
    return sound

def surface_blit(screen, surface, x_r, y_r):
    sw, sh = screen.get_size()
    rect = surface.get_rect(sw * x_r, sh * y_r)
    screen.blit(surface, rect)