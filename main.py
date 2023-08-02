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

from my_lib import *


FPS=60
GRID_NUM = 10



class MyPlane():
    def __init__(self, map_origin , gridWidth, col, row, hide = False, heading = "up") -> None:
        self.img = pygame.image.load(rc_plane_up)
        self.col = col
        self.row = row
        self.origin = map_origin
        self.gridWidth = gridWidth
        self.hide = hide
    
    def draw(self, surface:pygame.Surface):
        rect = self.img.get_rect()
        x = self.origin[0] + self.gridWidth*self.col + self.gridWidth/2
        y = self.origin[1] + self.gridWidth*self.row + self.gridWidth/2 + 6
        rect.center = x, y
        surface.blit(self.img, rect)
        
class MyPlanePark():
    def __init__(self, surface:pygame.Surface, origin_pos, side_len, gird_num = 10) -> None:
        self.surface:pygame.Surface = surface
        self.origin = origin_pos
        self.sideLen = side_len
        self.girdNum = gird_num
        self.rect_outline = pygame.Rect(self.origin[0]-1, self.origin[1]-1, self.sideLen+2, self.sideLen+2)
        self.rect = pygame.Rect(self.origin[0], self.origin[1], self.sideLen, self.sideLen)
        self.gridWidth = side_len / gird_num
        print("gridWidth = ", self.gridWidth)
        
        self.plane1 = MyPlane(self.origin, self.gridWidth, 5,5)
        self.plane2 = MyPlane(self.origin, self.gridWidth, 2,2)
        self.plane3 = MyPlane(self.origin, self.gridWidth, 2,8)

    def highlightGrid(self,col,row):
        x = self.origin[0] + self.gridWidth*col
        y = self.origin[1] + self.gridWidth*row
        rect = pygame.Rect(x, y, self.gridWidth+1, self.gridWidth+1)
        pygame.draw.rect(self.surface, color_red, rect, 2)
        
        
    def update(self):
        pygame.draw.rect(self.surface, color_white, self.rect_outline, 2)
        # pygame.draw.rect(self.surface, color_red, self.rect, 2)
        origin = self.origin
        lineWidth = 1
        grid_width = self.gridWidth
        mapLen = self.sideLen
        for i in range(1,self.girdNum):
            start = [origin[0], origin[1] + grid_width * i]
            end = [origin[0]+mapLen, origin[1] + grid_width * i]
            pygame.draw.line(self.surface,color_white,start,end,lineWidth)
        for i in range(1,self.girdNum):
            start = [origin[0] + grid_width * i, origin[1]]
            end = [origin[0] + grid_width * i, origin[1]+mapLen]
            pygame.draw.line(self.surface,color_white,start,end,lineWidth)
        
        # draw plane
        self.plane1.draw(self.surface)
        self.plane2.draw(self.surface)
        self.plane3.draw(self.surface)
        
    def getGridPos(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        ox = self.origin[0]
        oy = self.origin[1]
        grid_width = self.gridWidth
        col = int((x-ox)/grid_width)
        row = int((y-oy)/grid_width)
        return (col,row) # x,y





if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("邹邹的猜飞机大战")
    FPSClock=pygame.time.Clock()
    screen = pygame.display.set_mode((640,480))
    
    
    
    sideLen = int((min(screen.get_width(), screen.get_height()) - 100)/GRID_NUM)*GRID_NUM
    pos_leftTop = [(screen.get_size()[0] - sideLen)/2, (screen.get_size()[1] - sideLen)/2]
    plane_park = MyPlanePark(screen, pos_leftTop, sideLen, GRID_NUM)

    
    while True:
        col = 0
        row = 0
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            col,row = plane_park.getGridPos([x,y])
            print(col,row)
            
        screen.fill(back_color)
        font = pygame.font.SysFont("Microsoft Yahei", 20)
        txtsurf = font.render("邹邹的猜飞机大战", True, color_white)
        screen.blit(txtsurf,((screen.get_width() - txtsurf.get_width()) // 2,10))
        

        
        plane_park.update()
        plane_park.highlightGrid(col,row)
        
        pygame.display.update()
        FPSClock.tick(FPS)