# coding:utf-8

# ///////////////////////////////////////////////////////////////
#
# File:    main.py
# Brief:   
#
# Version: v0.0.1
# Author:  firestaradmin
# Date:    2023/08/02
#
# Copyright (c) 2023 LXG
#
# History:
# - 2023/08/02: v0.0.1 initial version
# - ----/--/--: --

# ///////////////////////////////////////////////////////////////




import pygame
import sys
from pygame.locals import QUIT,KEYDOWN

pygame.init()

screen = pygame.display.set_mode((640,480))

back_color=[22,22,22]


while True:
    for event in pygame.event.get():
        if event.type is QUIT:
            exit()
            
    screen.fill(back_color)
    pygame.display.update()
