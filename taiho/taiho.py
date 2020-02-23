import pygame
from pygame.locals import *
import sys

class ball():
    def __init__(self,bx,by,vx,vy,ct) :
        self.bx = bx
        self.by = by
        self.vx = vx
        self.vy = vy
        self.ct = ct
        self.a = 1

    def draw(self,screen,fl):
        if fl >= 1: 
            pygame.draw.circle(screen,(10,10,10),(self.bx,self.by),10)

    def update(self):
        self.bx += self.vx
        self.by += self.vy
        self.vy += self.a

class gun():
    def __init__(self,gx,gy) :
        self.gx = gx
        self.gy = gy
        self.gMap = pygame.image.load("sprite3.png").convert_alpha()   #マリオのマップチップ読み込み
        #マップチップの座標用のベース
        self.basew = 48
        self.baseh = self.basew*2
        #マップチップの座標(大砲)
        self.mc_x0 = 15* self.basew #
        self.mc_y0 = 0 #最上段　0段目
        #fire
        self.mc_x1 = 10* self.basew #10列め
        self.mc_y1 = 6 * self.basew  #6段目
        self.mx=120 #大砲の位置
        self.my=450 #
        self.fl=0 #フラグ
        self.ct=0 #カウンタ

    def draw(self,screen):
        #大砲描画    
        screen.blit(self.gMap ,(self.mx,self.my),(self.mc_x0,self.mc_y0,self.basew*2,self.basew*2))
        #火花描画
        if self.fl==2: 
            screen.blit(self.gMap ,(self.mx+60,self.my),(self.mc_x1, self.mc_y1, self.basew, self.basew))
            #pygame.draw.circle(screen,(10,10,10),(bx,by),10,)
            self.ct +=1
            if self.ct >2: 
                self.fl=1
                self.ct=0
    def update(self):
        pass

#------------------------------------------------------------------
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    screen.fill((255,255,255))  # 画面を白に
    sd_hit = pygame.mixer.Sound("bomb.wav")
    pygame.display.update()     # 画面更新
    clock = pygame.time.Clock()#FPS設定用の準備
    g1 = gun(100,200)#ガンのインスタンス化
    while (1):
        screen.fill((255,255,255))  # 画面を白に
        g1.update()
        g1.draw(screen)
        if g1.fl > 0:
            b1.update()
            b1.draw(screen,g1.fl)

        pygame.display.update()     # 画面更新
        clock.tick(30)

        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
            elif event. type == KEYDOWN: 
                if event.key==K_SPACE:
                    b1= ball(200,480,15,-15,2)
                    g1.fl=2
                    sd_hit.play()
if __name__ == "__main__":
    main()