# source/scenes/title_scene.py

import pygame as py
import os
from util.functions import load_img, show_img

py.init()

class TitleScene:

    def __init__(self, screen):
        
        self.f11 = False
        self.screen = screen

        bg_path = os.path.join("assets", "backgrounds", "TitleScreen_bg.png")
        self.bg = load_img(bg_path, scale=(1920, 1080))

        PLAY_path = os.path.join("assets", "ui", "icons", "PLAY_btn.png")
        self.PLAY = load_img(PLAY_path, scale=(296, 128))

        QUIT_path = os.path.join("assets", "ui", "icons", "QUIT_btn.png")
        self.QUIT = load_img(QUIT_path, scale=(296, 128))

        Config_path = os.path.join("assets", "ui", "icons", "Config_btn.png")
        self.Config = load_img(Config_path, scale=(128, 128))

    def run(self):
        
        running = True

        while running:

            show_img(self.bg, 0.5, 0.5, self.screen)
            self.PLAY_rect = show_img(self.PLAY, 0.3, 0.4, self.screen)
            self.QUIT_rect = show_img(self.QUIT, 0.7, 0.4, self.screen)
            self.Config_rect = show_img(self.Config, 0.9, 0.1, self.screen)

            events = py.event.get()
            
            for event in events:

                if event.type == py.QUIT:
                    running = False

                elif event.type == py.KEYDOWN and event.key == py.K_F11:
                    self.f11 = not f11

                    if self.f11:
                        py.display.set_mode((1900, 1060))
                    else:
                        py.display.set_mode((1920, 1080), py.FULLSCREEN)

                elif event.type == py.MOUSEBUTTONDOWN and event.key == self.PLAY_rect.collidepoint(event.pos):
                    return "Living room"
        
            py.display.update()

        py.quit()