import sys
import pygame as py

py.init()

screen = py.display.set_mode((640, 360))
py.display.set_caption("Grow Chick!")

WHITE = (255, 255, 255)

Running = True
while Running:
    screen.fill(WHITE)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            Running = False
            
    py.display.flip()
    
py.quit()
sys.exit()