# source/scenes/title_scene.py
"""타이틀 화면 / 메인화면"""

import os
import pygame as py
from source.util.functions import load_img, load_text, show_img, show_text
from source.util.paths import text_font_path

py.init()

class TitleScene:
    def __init__(self, screen):
        self.screen = screen
        self.f11 = False
        
        py.display.set_caption("Grow Chick!")
        
        BG_PATH = os.path.join("assets", "backgrounds", "title-screen.png")
        PLAY_PATH = os.path.join("assets", "ui", "icons", "play-bar.png")
        SETTING_PATH = os.path.join("assets", "ui", "icons", "setting.png")
        INFO_PATH = os.path.join("assets", "ui", "icons", "information.png")
        EXIT_PATH = os.path.join("assets", "ui", "icons", "exit.png")
        
        self.BG = load_img(BG_PATH, scale=(1920, 1080))
        self.PLAY = load_img(PLAY_PATH, scale=(408, 176))
        self.SETTING = load_img(SETTING_PATH, scale=(138, 138))
        self.INFO = load_img(INFO_PATH, scale=(130, 130))
        self.EXIT = load_img(EXIT_PATH, scale=(120, 120))
        
    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            
            show_img(self.screen, self.BG, w_r=0.5, h_r=0.5)
            PLAY_RECT = show_img(self.screen, self.PLAY, x_c=960, y_c=678)
            SETTING_RECT = show_img(self.screen, self.SETTING, x_c=960, y_c=917)
            INFO_RECT = show_img(self.screen, self.INFO, x_c=777, y_c=917)
            EXIT_RECT = show_img(self.screen, self.EXIT, x_c=1151, y_c=917)
            
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    return "quit"
                
                elif event.type == py.MOUSEBUTTONDOWN and PLAY_RECT.collidepoint(event.pos):
                    return "living room"
                
                elif event.type == py.KEYDOWN and event.key == py.K_F11:
                    self.f11 = not self.f11
                    
                    if self.f11:
                        py.display.set_mode((1890, 1060))
                    else:
                        py.display.set_mode((1920, 1080), py.FULLSCREEN)
                        
            py.display.update()
