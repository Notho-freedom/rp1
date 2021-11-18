from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
import webbrowser
from tkinter import messagebox
import sqlite3
import pygame

import pygame,sys
from pygame.locals import *
pygame.init()
FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()
#set up the window
screen = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('drawing')
#set up the colors
black = ( 0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = ( 0, 255, 0)
blue = ( 0, 0, 255)

imagex = 320
imagey = 220
direction = 'left'
fontObj = pygame.font.Font('freesansbold.ttf', 32)
text = fontObj.render('Hello World!', True, green, blue)
rect = text.get_rect()
rect.center = (200, 150)
while True:
     screen.fill(white)
     pygame.draw.polygon(screen, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0,106)))
     pygame.draw.line(screen, blue, (60, 60), (120, 60), 4)
     pygame.draw.line(screen, blue, (120, 60), (60, 120))
     pygame.draw.line(screen, blue, (60, 120), (120, 120), 4)
     pygame.draw.circle(screen, blue, (300, 50), 100, 0)
     pygame.draw.ellipse(screen, red, (300, 250, 80,80), 1)
     pygame.draw.rect(screen,red, (200, 150, 100, 50))
     screen.blit(text, rect)
     if direction == 'right':
          imagex += 5
     if imagex == 320:
          direction = 'down'
     elif direction == 'down':
          imagey += 5
     if imagey == 220:
          direction = 'left'
     elif direction == 'left':
          imagex -= 5
     if imagex == 20:
          direction = 'up'
     elif direction == 'up':
          imagey -= 5
     if imagey == 20:
          direction = 'right'
for event in pygame.event.get():
     if event.type == QUIT:
          pygame.quit()
          sys.exit()
pygame.display.update()
fpsClock.tick(FPS)
