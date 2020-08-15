import pygame
from pygame.locals import *
import sys
import random

#定数
SX=800
SY=600

class snow():#クラス
    def __init__(self,px,py):
        self.px = px
        self.py = py
        self.rr = 2  # サイズ
        self.ct = 0  # 位置の更新をするかしないか
        self.hp = 100  # hp

    # 次の位置を計算
    def draw(self,screen):
        r3 = random.randint(1,3)#位置の更新をするかしないか
        self.ct += r3 #位置の更新をするかしないかランダムで決めている
        if self.ct % 6 ==0:
            r1 = random.randint(1,5)-3
            r2 = random.randint(2,15)
            self.px += r1
            self.py += r2
            if self.py > SY:
                self.hp = 0
            self.ct =0 
        pygame.draw.circle(screen,(100,100,200), (self.px,self.py), self.rr) # 描画

def move(screen,clock):
    ct=0
    hx=100
    while (1):
        hx+=1
        screen.fill((255,255,255))  				# 画面を白に
        #飛行船描画
        pygame.draw.rect   (screen, (5,5,5), Rect(hx+60,90,60,10), 5)
        pygame.draw.ellipse(screen, (5,5,5), Rect(hx,10,190,90), 0)
        if ct>330:
            pygame.draw.ellipse(screen, (255,5,5), Rect(hx+50,50,60,60), 0)
        pygame.display.update()     				# 画面更新
        ev()
        ct+=1
        clock.tick(100)		# 60fps
        if ct >350:
            break        
    return hx

def drop(screen,clock,font, s, hx):       
    ct=0
    while (1):
        screen.fill((255,255,255))  				# 画面を白に
        #飛行船描画
        pygame.draw.rect   (screen, (5,5,5), Rect(hx+60,90,60,10), 5)
        pygame.draw.ellipse(screen, (5,5,5), Rect(hx,10,190,90), 0)
        s.append(snow(hx+80,100,))

        #おちるもの描画
        for i in range(len(s)):
            s[i].draw(screen)
        #インスタンスの削除
        #hpでチェックする場合 、あとでいろんな条件を追加できる
        # for i,a in enumerate(s):
        #     if a.hp == 0:
        #         s.pop(i)
        #y座標でチェックする場合　こっちのほうがシンプルだが、汎用性にかける
        for i,a in enumerate(s):
            if a.py >= SY:
                s.pop(i)
        #print("@1",len(s))

        #文字描画
        txt = font.render("Look at these people", True, (155,5,5))
        txt2 = font.render("They look like trash.", True, (155,5,5))   # 描画する文字列の設定
        if ct >300:
            screen.blit(txt, (20, 100))# 文字列の表示位置
        if ct >600:    
            screen.blit(txt2, (20, 200))# 文字列の表示位置
        pygame.display.update()     				# 画面更新
        # イベント処理
        for event in pygame.event.get():  # イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）
        ct += 1
        clock.tick(100)								# 60fps
        if ct >1000:
            break

def ev():
    # イベント処理
    for event in pygame.event.get():  # イベントキューからキーボードやマウスの動きを取得
        if event.type == QUIT:        # 閉じるボタンが押されたら終了
            pygame.quit()             # Pygameの終了(ないと終われない)
            sys.exit()                # 終了（ないとエラーで終了することになる）

def main():
    clock = pygame.time.Clock()						# FPS固定のため
    pygame.init()                                 	# Pygameの初期化
    screen = pygame.display.set_mode((SX,SY))  	# 800*600の画面
    r1=random.randint(1, 800)
    s=[]
    font = pygame.font.Font(None, 55)               # フォントの設定(55px)

    #idou 
    hx = move(screen,clock)
    #bakuhatu
    #drop
    drop(screen,clock,font, s, hx)
    #talk

if __name__ == "__main__":
    main()