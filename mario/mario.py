"""
変数名変更
basew mw
baseh mh
rrx brx
rry bry
rrw brw
rrh brh
"""

import pygame
from pygame.locals import *
import sys

class mario ():
    def __init__(self):
        #マリオの位置、速度
        self.mx = 100 #位置
        self.my = 350
        self.vx = 4 #速度
        self.vy = 1
        self.ay = 1 #加速度
        #フラグ
        self.jf = 1 #状態　1:ジャンプ中

        #マップチップ
        self.gMap = pygame.image.load("sprite3.png").convert_alpha()   #マリオのマップチップ読み込み
        #マップチップの座標用のベース
        self.mw = 48
        self.mh = self.mw*2
        #マップチップの座標
        self.x0 = 2*self.mw #2列め
        self.y0 = 0         #最上段　0段目
        self.x1 = 3*self.mw #3列目
        self.y1 = 3*self.mw #３段目
        #座った絵
        self.x2a = 1*self.mw #1列め
        self.y2a = 0         #最上段　0段目
        self.x2b = 1*self.mw #1列め
        self.y2b = 3*self.mw #３段目

        #アニメ用カウンタ
        self.ct = 0 #アニメ用カウンタ
        self.ctmax = 8 #アニメ用カウンタ
        self.ctchg = 4 #アニメ用カウンタの定数

    def update(self, bricks):

        # とりあえず進ぬ計算（マリオの位置、速度）ken02.png
        self.mx += self.vx
        self.my += self.vy
        self.vy += self.ay

        #地面との当たりチェック
        if self.my >= 450:
            self.my = 450
            self.vy = 0
        #レンガとの当たりチェック
        for i,brick in enumerate(bricks):
            print("◆",i)
            ht = self.check_pt(brick)

    def check_pt(self, brick):
        #最初のあたりを付ける (中央だけ見る)
        cmx = int(self.mx + self.mw/2)  #マリオのへそ
        cmy = int(self.my + self.mh/2)

        lowx = brick.brx - self.mw/2  #レンガの左端
        hix = brick.brx + brick.brw + self.mw/2  #レンガの右橋
        lowy = brick.bry - self.mh/2  #レンガの上橋
        hiy = brick.bry + brick.brh + self.mh/2  #レンガの下端

        if ((lowx <= cmx  <= hix) and (lowy <= cmy  <= hiy)) :#側面を優先してチェック
            if ((lowx <= cmx  <= brick.brx) and (lowy < cmy  < hiy)) :#左に当たった
                print("left")
                self.mx = brick.brx - self.mw
            elif ((brick.brx + brick.brw <= cmx  <= hix) and (lowy < cmy  < hiy)) :#右に当たった
                print("right")
                self.mx = brick.brx+brick.brw

            elif ((lowx+1 <= cmx  <= hix-1) and (lowy <= cmy  <= brick.bry-20 )) :#上
                print("up")
                self.my = brick.bry-self.mh
                self.vy = 0
            elif ((brick.brx <= cmx  <= brick.brx + brick.brw ) and (brick.bry + brick.brh <= cmy  <= hiy)) :#下に当たった
                print("down")
                self.my = brick.bry + brick.brh
                #self.vy = 0

    def draw(self, screen):
        ##アニメ用の設定　
        self.ct += 1  # 動作のカウンタ
        if abs(self.vx) > 4:
            self.ctmax = 4
            self.ctchg = self.ctmax/2
        elif abs(self.vx) > 3:
            self.ctmax = 6
            self.ctchg = self.ctmax/2
        elif abs(self.vx) > 2:
            self.ctmax = 8
            self.ctchg = self.ctmax/2
        elif abs(self.vx) > 1:
            self.ctmax = 10
            self.ctchg = self.ctmax/2
        else :
            self.ctmax = 20
            self.ctchg = self.ctmax/2
        #座っているところ 
        if self.vx == 0:
            if self.ct % self.ctmax < self.ctchg:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x2a,self.y2a,self.mw,self.mh))
            else:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x2b,self.y2b,self.mw,self.mh))
        #右向き 
        elif self.vx > 0:                 
            if self.ct % self.ctmax < self.ctchg:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x0,self.y0,self.mw,self.mh))
            else:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x1,self.y0,self.mw,self.mh))
        #左向き 
        elif self.vx < 0:#←
            if self.ct % self.ctmax < self.ctchg:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x0,self.y1,self.mw,self.mh))
            else:#←
                screen.blit(self.gMap ,(self.mx,self.my),(self.x1,self.y1,self.mw,self.mh))

    def evt(self):  
        for event in pygame.event.get():  # イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(ないと終われない)
                sys.exit()  #終了（ないとエラーで終了することになる）
                
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    if event.key == K_LEFT:
                        self.vx -= 1  
                    elif event.key == K_RIGHT:
                        self.vx += 1  
                    elif event.key == K_UP:
                        self.my -= 4  
                    elif event.key == K_DOWN:
                        self.my += 4  
                    elif event.key == K_SPACE:#jump
                        self.vy = -15

    def draw_text(self, screen, font):
        #マリオの位置　　　
        t = "mx=" + str(self.mx) + "  my=" + str(self.my) + "  vx=" + str(self.vx) + "  vy=" + str(self.vy)
        txt = font.render(t, True, (55, 55, 55))   # 描画する文字列の設定
        screen.blit(txt, [20, 20])# 文字列の表示位置        

#--------レンガ-------------------------------------------------------
class brick ():
    def __init__(self, brx, bry, brw, brh):
        #黄色のオブジェクトの座標や大きさ
        self.brx = brx
        self.bry = bry
        self.brw = brw
        self.brh = brh
        self.brk = Rect(brx, bry, brw, brh)
        self.brvx = 1

    def update(self):
        self.brx -= self.brvx
        #self.brw -= 1
        if self.brx >= 800 or self.brx <= 0 :
            self.brvx *= -1 

    def draw(self, screen):
        self.brk = Rect(self.brx, self.bry, self.brw, self.brh)
        pygame.draw.rect(screen, (255, 255, 0), self.brk)

#---------------------------------------------------------------
def disp(screen,font,txt,x,y):
        tmp_txt = font.render(txt, True, (55,55,55))   # 描画する文字列の設定
        screen.blit(tmp_txt, [x, y])# 文字列の表示位置  

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    screen.fill((255,255,255))  # 画面を白に
    pygame.display.update()     # 画面更新
    clock = pygame.time.Clock()#FPS設定用の準備
    font = pygame.font.Font(None, 55)               # フォントの設定(55px)
    mr1 = mario() #mario instance
    bk=[]

    bk.append(brick(400, 300, 100, 150)) #brick instance 
    bk.append(brick(500, 300,  80,  50))#brick instance 
    bk.append(brick(700, 200,  100,  50)) #brick instance 
    bk.append(brick(600, 100,  100,  50)) #brick instance 
    #bk5 = brick(700, 400, 80, 50) #brick instance 
    
    while (1):
        screen.fill((255, 255, 255))  # 画面を白に

        #レンガ位置
        bk[3].update()
        bk[2].update()

        #レンガ描画
        for b in bk:
            b.draw(screen)
    
        ##マリオ
        mr1.draw_text(screen, font)  # 状態
        mr1.update(bk)  # 位置の計算
        mr1.draw(screen)  # 描画

        pygame.display.update()     # 画面更新
        # イベント処理
        mr1.evt()
        clock.tick(30)

if __name__ == "__main__":
    main()

