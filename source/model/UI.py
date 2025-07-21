import pygame as py

class UIButton:
    def __init__(self, image, pos):
        self.image = image
        self.rect = image.get_rect(center=pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def click(self, event):
        return event.type == py.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
