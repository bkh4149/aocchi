import pygame
from pygame.locals import *
import sys
import math
import random

"""
        中心x 中心y 半径r サイズsize　角度　角速度　

"""
st=[[100,300, 50,  5,0,1.2],
    [100,300, 80, 10,0,1.0],
    [100,300,100, 15,0,0.8],
    [100,300,150, 20,0,0.7],
    [100,300,250, 25,0,0.6],
    [100,300,350, 20,0,0.5],
   ]
    
class  waku():
    def __init__(self, r, v):
        self.rx = r  #半径
        self.ry = r  #
        self.v = v   #角速度
        self.tt = 0  #角度
        self.sz= 15
        self.col=(10,10,10)
    
    def update(self, x0, y0):
        self.x1 = int(math.cos(self.tt) * self.rx) + x0
        self.y1 = int(math.sin(self.tt) * self.ry) + y0
        self.tt += self.v / 100
        
    def draw(self,screen):    
        pygame.draw.circle(screen, self.col, (self.x1, self.y1), self.sz)
    
class  waku2(waku):
    def draw2(self,screen):
        pygame.draw.circle(screen, (210,10,10), (self.x1, self.y1), 10)

class  waku3(waku):
    def draw3(self,screen):    
        pygame.draw.circle(screen, (10,210,10), (self.x1, self.y1), 3)
        
    
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    screen.fill((255, 255, 255))  # 画面を白に
    pygame.display.update()     # 画面更新
    x0 = 300
    y0 = 300
    
    r0 = 0
    r1 = random.randint(100,300)
    r2 = random.randint(100,300)
    r3 = random.randint(100,300)
    r4 = random.randint(10,130)
    r41 = random.randint(10,30)
    
    w0 = waku(r0, 1.2)
    w1 = waku(r1, 0.1)
    w2 = waku(r2, 0.12)
    w21 = waku2(r4, 0.7)
    w211 = waku3(r41, 1.7)
    w22 = waku2(r4+20, 1.2)
    w3 = waku(r3, 0.04)
    w4 = waku(300, 0.14)
  

    while (1):
        screen.fill((255, 255, 255))  # 画面を白に
        w0.update(x0, y0)
        w1.update(x0, y0)
        w2.update(x0, y0)
        w21.update(w2.x1, w2.y1)
        w22.update(w2.x1, w2.y1)
        w211.update(w21.x1, w21.y1)
        w3.update(x0, y0)
        w4.update(x0, y0)
        
        w0.draw(screen)
        w1.draw(screen)
        w2.draw(screen)
        w21.draw2(screen)
        w22.draw2(screen)
        w211.draw3(screen)
        w3.draw(screen)
        w4.draw(screen)
        
        pygame.display.update()     # 画面更新

        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）

if __name__ == "__main__":
    main()
