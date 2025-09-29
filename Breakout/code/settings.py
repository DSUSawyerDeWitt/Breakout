import pygame
from os.path import join
from os import walk
from random import choice
from random import uniform
from random import randint
import math

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600
UI_WIDTH, UI_CENTER = 250, (WINDOW_WIDTH - 250) - (250 / 2)

COLORS = {'background':'#9abbed', 'UIbackground': '#224d85', 'UIMenubackground': '#ffffff','UIMenubackgroundborder': '#AFAfAf'}
UISIZE = {'width': WINDOW_WIDTH - 250, 'center': WINDOW_WIDTH - ((WINDOW_WIDTH - (WINDOW_WIDTH - 250)) / 2)}
SIZE = {'basic ball' : (30,30), 'basic tile': (50,20)}
SPEED = {'Ball' : 100} #don't think this is used anymore
UIBALLS = {0: 'Basic Ball', 1: 'Speed Ball', 2: 'Monster Ball', 3: 'Sniper Ball'} #For Placing the UI Ball Images by Name
UIBALLSINVERSE = {'Basic Ball': 0, 1: 'Speed Ball', 2: 'Monster Ball', 3: 'Sniper Ball'}

UIUPGRADES = {0: 'Strength', 1: 'Speed', 2: 'Click', 3: 'Prestige'} #For Placing the UI Upgrade Images by Name (could maybe move in Upgrade_Menu())

NUMBEROFBALLS = {'Basic Ball' : 0, 'Speed Ball' : 0, 'Monster Ball': 0, 'Sniper Ball': 0}
UPGRADELEVELS = {'Strength': 100, 'Speed': 55, 'Click': 10, 'Level Bonus': 3} #How many Times each upgrade was clicked
UPGRADEPRICES = {'Strength': 10, 'Speed': 1, 'Click': 5, 'Level Bonus': 6}

#Strength Menu
STRENGTH_LEVEL = {'Basic Ball': 1, 'Speed Ball' : 2, 'Monster Ball': 3, 'Sniper Ball': 4, 'Click': 1, 'Click Area': 2}
STRENGTH_COST = {'Basic Ball': 100, 'Speed Ball' : 100, 'Monster Ball': 100, 'Sniper Ball': 100, 'Click': 100, 'Click Area': 1000}


SPEED_LEVEL = {'Basic Ball': 100, 'Speed Ball' : 100, 'Monster Ball': 100, 'Sniper Ball': 100} #Set these Back to 1 for starting values.
SPEED_COST = {'Basic Ball': 100, 'Speed Ball' : 100, 'Monster Ball': 100, 'Sniper Ball': 100}



BALL_COST = {'Basic Ball': 100, 'Speed Ball' : 100, 'Monster Ball': 100, 'Sniper Ball': 100}

#Stats
DAMAGE_DONE = {'Basic Ball': 0, 'Speed Ball' : 0, 'Monster Ball': 0, 'Sniper Ball': 0, 'Click': 0}

#Make a Stats Dictonary Eventually
