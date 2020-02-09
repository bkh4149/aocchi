import pygame
from pygame.locals import *
import sys
import random

class kuro():
    def __init__(self):
        self.rx = random.randint(1, 800)
        self.ry = random.randint(1, 600)
        self.hp = 100
    
    def update(self):
        rvx = random.randint(-1, 1)
        rvy = random.randint(-1, 1)
        self.rx += rvx
        self.ry += rvy                
    
    def draw(self,screen,font,i):
        if self.hp>1:
            tx = str(i)
            pygame.draw.circle(screen,(10,10,10),(self.rx,self.ry),20)
            txt = font.render(tx, True, (255,0,0))
            screen.blit(txt,[self.rx-10,self.ry-17])
    

def main():
    pygame.init()                                 # Pygameの初期化
    font = pygame.font.Font(None, 55)               # フォントの設定(55px)
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    screen.fill((255,255,255))  # 画面を白に
    pygame.display.update()     # 画面更新
    kkk=[kuro() for i in range(10)]
    mx=0
    my=0
    
    while (1):
        screen.fill((255,255,255))  # 画面を白に
        for i in range(10):
            kkk[i].update() 
            kkk[i].draw(screen,font,i)
        pygame.display.update()     # 画面更新

        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
                
            elif event.type == MOUSEBUTTONDOWN: 
                btn = event.button
                mx, my = event.pos
                
                #当たり判定
                for i in range(10):
                    print("i=",i,"  mx=",mx,"  my=",my, "  kkk[i].rx=",kkk[i].rx,"  kkk[i].ry=",kkk[i].ry,)
                    if  kkk[i].rx-50 < mx < kkk[i].rx+50  and  kkk[i].ry-50 < my < kkk[i].ry+50:
                        print("atari")
                        kkk[i].hp = 0
                    else:
                        print("hazure")
                
                mx=0
                my=0

if __name__ == "__main__":
    main()