# source/model/status.py

import os
import pygame as py
from source.util.functions import load_img, load_text, show_img, show_text
import config

py.init()

class Status:
    def __init__(self, screen):

        layout_path = os.path.join("assets", "ui", "layout", "status-frame.png")
        minimize_path = os.path.join("assets", "ui", "icons", "minimize-window.png")
        show_path = os.path.join("assets", "ui", "icons", "show.png")

        self.screen = screen
        self.layout_img = load_img(layout_path, scale=(888, 888))
        self.minimize_btn = load_img(minimize_path, scale=(60, 60))
        self.show_btn = load_img(show_path, scale = (60, 60))
        
        self.minimize = False
        self.stats = config.DEFAULT_STATS

    def toggle(self):
        self.minimize = not self.minimize

    def draw(self):
        while True:
            if not self.minimize:
                show_img(self.screen, self.layout_img, x_c=282, y_c=562)
                self.minimize_rect = show_img(self.screen, self.minimize_btn, x_c=473, y_c=957)
                
                show_text(self.screen)

            else:
                self.show_rect = show_img(self.screen, self.show_btn, x_c=85, y_c=957)
                
    def manage_event(self, event):
        while True:
            if event.type == py.MOUSEBUTTONDOWN:
                if not self.minimize:
                    if self.minimize_rect.collidepoint(event.pos):
                        self.toggle()
                if self.minimize:
                    if self.show_rect.collidepoint(event.pos):
                        self.toggle()
