

import pygame, sys

from my_lib import *

mapGridCnt = 10

class MyDrawer:
    def __init__(self, surface:pygame.Surface) -> None:
        self.surface = surface
    
        
    def draw_line(self,start, end, width, color=(255,255,255)):
        pygame.draw.line(self.surface,color,start,end,width)

    def draw_square(self, start_pos, width, height, line_width = 2, color=(255,255,255)):
        pos_leftTop = start_pos
        pos_rightTop = [start_pos[0]+width, start_pos[1]]
        pos_leftBottom = [start_pos[0], start_pos[1]+height]
        pos_rightBottom = [start_pos[0]+width, start_pos[1]+height]
        self.draw_line(pos_leftTop, pos_rightTop, line_width , color)
        self.draw_line(pos_leftTop, pos_leftBottom, line_width , color)
        self.draw_line(pos_rightTop, pos_rightBottom, line_width , color)
        self.draw_line(pos_leftBottom, pos_rightBottom, line_width , color)
        
        
    def draw_map(self, size:list, color=(255,255,255)):
        lineWidth = 1
        row_cnt = size[0]
        # col_cnt = size[1]
        s_width = self.surface.get_size()[0]
        s_height = self.surface.get_size()[1]
        print(s_width, s_height)
        mapLen = min(self.surface.get_size()[0], self.surface.get_size()[1])
        mapLen = mapLen - 100
        mapLen = (mapLen/row_cnt)*row_cnt
        
        pos_leftTop = [(s_width - mapLen)/2, (s_height - mapLen)/2]
        # self.draw_square(pos_leftTop, mapLen, mapLen)
        self.draw_square([pos_leftTop[0]-2, pos_leftTop[1]-2], mapLen+4, mapLen+4)
        
        grid_width = mapLen/row_cnt
        for i in range(1,row_cnt):
            start = [pos_leftTop[0], pos_leftTop[1] + grid_width * i]
            end = [pos_leftTop[0]+mapLen, pos_leftTop[1] + grid_width * i]
            self.draw_line(start, end, lineWidth)
        for i in range(1,row_cnt):
            start = [pos_leftTop[0] + grid_width * i, pos_leftTop[1]]
            end = [pos_leftTop[0] + grid_width * i, pos_leftTop[1]+mapLen]
            self.draw_line(start, end, lineWidth)
        return pos_leftTop
    
def findGrid(originPos, mousePos):
    gx = 0
    gy = 0
    x = mousePos[0]
    y = mousePos[1]
    ox = originPos[0]
    oy = originPos[1]
    
    for ix in range(ox, )
    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    drawer = MyDrawer(screen)
    
    pygame.display.set_caption("邹邹的猜飞机大战")

    fpsClock = pygame.time.Clock()


    screen.fill(backcolor)
    font = pygame.font.SysFont("Microsoft Yahei", 20)
    txtsurf = font.render("邹邹的猜飞机大战", True, white)
    screen.blit(txtsurf,((screen.get_width() - txtsurf.get_width()) // 2,10))
    
    
    originPos = drawer.draw_map([mapGridCnt,mapGridCnt])
    pygame.display.update()

    
    # rect3 = pygame.rect()
    while True:
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            print(x,y)