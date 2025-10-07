# source/scenes/living room.py

import pygame as py
import os
from util.functions import load_text, load_img, show_text, show_img
from util.paths import text_font_path, title_font_path
from util.colors import LEMON, ORANGE

py.init()

class TitleScene:
    def __init__(self, screen):
        self.screen = screen
        self.f11 = False

        self.title = load_text("병아리를 키워라!", title_font_path, 180, ORANGE)
        
        play_btn_path = os.path.join("assets", "ui", "icons", "button_play.png")
        self.play_btn = load_img(play_btn_path, (450, 189))

    def run(self):
        running = True

        while running:
            self.screen.fill(LEMON)

            show_text(self.title, 0.5, 0.35, self.screen)
            
            play_btn_rect = show_img(self.play_btn, 0.5, 0.65, self.screen)

            events = py.event.get()
            for event in events:
                if event.type == py.QUIT:
                    running = False
                
                elif event.type == py.KEYDOWN and event.key == K_F11:
                    self.f11 = not f11
                    if self.f11:
                        py.display.set_mode((1900, 1020))
                    else:
                        py.display.set_mode((1920, 1080), py.FULLSCREEN)

                    elif event.type == py.MOUSEBUTTONDOWN and play_btn_rect.collidepoint(event.pos):
                        return "living room"

        py.display.update()