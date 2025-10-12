# source/scenes/living_room.py
"""거실, 인게임 기본 장소"""

import os
import pygame as py
from source.util.functions import load_img, load_text, show_img, show_text
from source.util.paths import text_font_path

py.init()

class LivingRoom:
    def __init__(self, screen):
        self.screen = screen
        self.f11 = False
        
        self.BG_1_PATH = os.path.join("assets", "backgrounds", "living-room_day.png")
        self.BG_2_PATH = os.path.join("assets", "backgrounds", "living-room_evening.png")
        self.BG_3_PATH = os.path.join("assets", "backgrounds", "living-room_night.png")
        self.STATUS_FRAME_PATH = os.path.join("assets", "ui", "layout", "status-frame.png")
        self.TEXT_FRAME_PATH = os.path.join("assets", "ui", "layout", "text-frame.png")
        self.CLOSE_WINDOW_PATH = os.path.join("assets", "ui", "icons", "close-window.png")
        
        self.BG_1 = load_img(self.BG_1_PATH, scale=(1920, 1080))
        self.BG_2 = load_img(self.BG_2_PATH, scale=(1920, 1080))
        self.BG_3 = load_img(self.BG_3_PATH, scale=(1920, 1080))
        self.STATUS_FRAME= load_img(self.STATUS_FRAME_PATH, scale=(926, 926))
        self.TEXT_FRAME = load_img(self.TEXT_FRAME_PATH, scale=(760, 760))
        self.CLOSE_WINDOW = load_img(self.CLOSE_WINDOW_PATH, scale=(66, 66))
        
    def run(self):
        screen = self.screen
        while True:
            self.screen.fill((0, 0, 0))
            
            show_img(screen, self.BG_1, w_r=0.5, h_r=0.5)
            show_img(screen, self.STATUS_FRAME, x_c=281, y_c=559)
            show_img(screen, self.CLOSE_WINDOW, x_c=477, y_c=969)
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    return "quit"
                
                elif event.type == py.KEYDOWN and event.key == py.K_F11:
                    self.f11 = not self.f11
                    
                    if self.f11:
                        py.display.set_mode((1890, 1060))
                    else:
                        py.display.set_mode((1920, 1080), py.FULLSCREEN)
                        
            py.display.update()
