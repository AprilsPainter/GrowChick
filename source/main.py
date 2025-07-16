import pygame as py
import sys

py.init()
width, height = 800, 600
screen = py.display.set_mode((width, height))
py.display.set_caption("Grow Chick!")

WHITE = (255, 255, 255)

running = True