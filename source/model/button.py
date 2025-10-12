# source/model/button.py
"""버튼 생성 및 호버 표시 기능을 위한 클래스"""

import pygame as py
py.init()

class Button:
    def __init__(self, img_path, pos):
        self.image = py.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.hovered = False
        self.clicked = False
        
    def update(self, mouse_pos, mouse_clicked):
        if self.rect.collidepoint(mouse_pos):
            if not self.clicked:
                self.hovered = True
        
        else:
            self.hovered = False
            
        if mouse_clicked[0] and self.rect.collidepoint(mouse_pos):
            self.clicked = True
        
        else:
            self.clicked = False
            
    def show(self, screen):
        if self.hovered:
            image = py.transform.scale(self.image, int((self.rect.width * 1.1), int(self.rect.height * 1.1)))
        
        elif self.clicked:
            image = py.transform.scale(self.image, int((self.rect.width * 0.9), int(self.rect.height * 0.9)))
            
        else:
            image = self.image
            
        rect = image.get_rect(center=self.rect.center)
        screen.blit(image, rect.center)