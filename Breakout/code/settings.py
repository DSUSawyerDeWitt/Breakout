import pygame
from os.path import join
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600

COLORS = {'background':'#9abbed', 'UIbackground': '#224d85'}
UISIZE = {'width': WINDOW_WIDTH - 250}
SIZE = {'basic ball' : (30,30), 'basic tile': (50,20)}
SPEED = {'basic ball' : 100}