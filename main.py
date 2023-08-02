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

FPS=60


color_white=[255,255,255]
color_red=[255,0,0]
back_color=[22,22,22]

class MyPlanePark():
    def __init__(self, surface:pygame.Surface, origin_pos, side_len, gird_num = 10) -> None:
        self.surface:pygame.Surface = surface
        self.origin = origin_pos
        self.sideLen = side_len
        self.girdNum = gird_num
        self.rect_outline = pygame.Rect(self.origin[0]-2, self.origin[1]-2, self.sideLen+4, self.sideLen+4)
        self.rect = pygame.Rect(self.origin[0], self.origin[1], self.sideLen, self.sideLen)
        pass

    def update(self):
        pygame.draw.rect(self.surface, color_white, self.rect_outline, 2)
        pygame.draw.rect(self.surface, color_red, self.rect, 2)
        
        
    def getGridPos(self, mouse_pos):
        return (0,0) # x,y


if __name__ == "__main__":
    pygame.init()
    FPSClock=pygame.time.Clock()
    screen = pygame.display.set_mode((640,480))
    plane_park = MyPlanePark(screen, [10,10], 200, 10)
    plane_park.update()
    
    while True:
        for event in pygame.event.get():
            if event.type is QUIT:
                exit()
                
        screen.fill(back_color)
        plane_park.update()
        pygame.display.update()
        FPSClock.tick(FPS)