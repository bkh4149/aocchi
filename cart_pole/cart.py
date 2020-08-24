import pygame
from pygame.locals import *
import sys
import math
import random
    
x0=400
y0=400

class bura():
    def __init__(self,r,o):
        #全部正規座標で考える
        self.oo = o # 角度 radじゃない単純角度
        self.ov = 0 # 角速度
        self.oa = 0 # 角加速度
        self.xp = 0 # 棒先の位値
        self.yp = 0
        self.xo = 0 # 棒元の位値
        self.yo = 0
        self.hp = 100
        
        #描画用
        self.xpic = 0 # 棒先の位値
        self.ypic = 0
        self.xpic0 = 0 # 棒元の位値
        self.ypic0 = 0
        #拡大用
        self.r = r  # 半径
        
    def update(self, screen):
        if self.oo<0 or self.oo>180:
            self.hp=0
            return
        #print("@update-----")
        # 某元と棒先の角度を計算
        self.oo= math.acos(self.xp - self.xo)*180/3.14 
        
        #角度から角加速度を計算
        self.oa = -(math.cos(self.oo*3.14/180))  # radを角度に戻して計算
        #print("  @u20 self.oa=",self.oa)
        
        #角加速度から角速度
        self.ov += self.oa
        #print("  @u30 self.ov=",self.ov)
        
        #角速度から角度
        self.oo += self.ov
        #print("  @u40 self.oo = ",self.oo)
        
        # 角度からxpic,ypicを計算    
        ora = self.oo * 3.14/180
        #print("  @u50 ora=",ora)
        self.xp = math.cos(ora)+self.xo
        self.yp = math.sin(ora)+self.yo
        #print("  @u55 self.xp=",self.xp)
        #描画のため拡大
        self.xpic  = int(x0 + self.xp*self.r)
        self.ypic  = int(y0 - self.yp*self.r)
        self.xpic0 = int(x0 + self.xo*self.r)
        self.ypic0 = int(y0 - self.yo*self.r)
        # 描画
        pygame.draw.circle(screen, (100,100,100), (self.xpic,self.ypic), 10)     
        pygame.draw.circle(screen, (10,10,10), (self.xpic0, self.ypic0), 5)  
    
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 800))  # 800*600の画面
    ck = pygame.time.Clock()
    b = bura(300,90) 
    screen.fill((255,255,255))  # 画面を白に
    pygame.display.update()     # 画面更新
    
    while (1):
        ck.tick(10) 
        screen.fill((255, 255, 255))  # 画面を白に
        b.update(screen)
        pygame.display.update()     # 画面更新

        if b.hp==0:
            sys.exit()
        # イベント処理
        for event in pygame.event.get():# イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             # 終了（ないとエラーで終了することになる）
            elif event. type == KEYDOWN: 
                if event.key==K_LEFT:
                    b.xo -= 0.03 #横方向の速度
                elif event.key==K_RIGHT:
                    b.xo += 0.03 #横方向の速度                  
                

if __name__ == "__main__":
    main()

