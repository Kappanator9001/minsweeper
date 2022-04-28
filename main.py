import pygame,random, pygame.freetype
from buttons import *
from utility import *
pygame.init()
WIDTH = 6
HEIGHT = 5
w = pygame.display.set_mode([WIDTH*100, HEIGHT*100])
playing = True
buttons = populate([], 6)
button = mineButton(0,0,100,100)

button.color = colors['white']
button.fontcolor = colors['black']
c = pygame.time.Clock()
while playing:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      playing = False
    if event.type== pygame.MOUSEBUTTONDOWN:
      piss
  w.fill(colors['white'])
  for button in buttons:
    button.draw()
  pygame.display.flip()
  c.tick(69)