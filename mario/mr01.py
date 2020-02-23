import pygame
from pygame.locals import *
import sys


class mario ():
    def __init__(self):
        #マリオの位置、速度
        self.mx = 100 #位置
        self.my = 350
        self.vx = 4 #速度
        self.vy = 0
        self.ay = 1 #加速度

        #マップチップ
        self.gMap = pygame.image.load("sprite3.png").convert_alpha()   #マリオのマップチップ読み込み
        #マップチップの座標用のベース
        self.basew = 48
        self.baseh = self.basew*2
        #マップチップの座標
        self.x0 = 2*self.basew #2列め
        self.y0 = 0            #最上段　0段目
        self.x1 = 3*self.basew #3列目
        self.y1 = 3*self.basew #３段目
        #座った絵
        self.x2a = 1*self.basew #1列め
        self.y2a = 0            #最上段　0段目
        self.x2b = 1*self.basew #1列め
        self.y2b = 3*self.basew #３段目

        #フラグ、カウンタなど
        self.jf = 0 #ジャンプ中か 0:not 1:ジャンプ中　 2:２段ジャンプ中p
        self.f_onp = 0
        self.down_ct = 0 #落下中カウンタ（伸びるよう）
        self.ct = 0 #アニメ用カウンタ
        self.ctmax = 8 #アニメ用カウンタ
        self.ctchg = 4 #アニメ用カウンタの定数

    def update(self, bk1, bk2 ,bk3):
        print("◆1")
        self.update_sub(bk1)
        print("◆2")
        self.update_sub(bk2)
        print("◆3")
        self.update_sub(bk3)

    def update_sub(self, brick):
        #マリオがジャンプしてないとき
        if self.jf == 0:
            print("@1a")
            #マリオが右から走って左壁の衝突検出 e2.png
            if self.vx < 0 and (brick.rrx + brick.rrw-40 < self.mx < brick.rrx + brick.rrw) and  (brick.rry < self.my + self.baseh < brick.rry + brick.rrh):
                print("@2a")
                self.vx = 0
                self.mx =  brick.rrx + brick.rrw
            #マリオが左から来て、右壁の衝突検出 e3.png
            elif self.vx > 0 and (brick.rrx < self.mx+self.basew < brick.rrx+40) and  (brick.rry < self.my+self.baseh < brick.rry+brick.rrh):
                print("@2b")
                self.vx = 0
                self.mx =  brick.rrx - self.basew
            #それ以外
            else:
                print("@2c")
                #何らかの台の上にイルか
                if self.f_onp == 1:
                    pass
                else:#何らかの台の上にいない
                    #下に台があるか e4.png
                    if (brick.rry <= self.my+self.baseh <= brick.rry+15) and (brick.rrx-self.basew < self.mx < brick.rrx+brick.rrw):
                        print("@2c1")
                        #下に台がある場合
                        self.mx += self.vx
                        self.vy = 0
                        self.my = brick.rry-self.baseh #高さをrryに揃える
                        self.f_onp=1 #何らかの台に乗った
                    else:
                        print("@2c2")
                        #台がない
                        if self.my < 450:#空中か
                            print("@2c2a")
                            self.jf = 1  # 落下モードにする
                            self.down_ct = +1
                            self.f_onp = 0
                        else: #一番底にいる
                            print("@2c2b")
                            self.mx += self.vx
                            self.my = 450
                            self.down_ct = 0
        #マリオがジャンプ
        elif self.jf >= 1:
            print("@1b")
            #ジャンプして着地、壁の上側検出 1b.png
            if (brick.rry < self.my + self.baseh < brick.rry+50)and(brick.rrx-self.basew < self.mx < brick.rrx+brick.rrw) :
                print("@1b1")
                self.my = brick.rry-self.baseh
                self.vy = 0
                self.jf = 0
                self.f_onp = 1
            #それ以外
            else:#x:等速　y:定加速度運動
                print("@1b2")
                self.mx += self.vx
                self.my += self.vy
                self.vy += self.ay #加速度　定加速度運動
                if self.my >= 450: #ボトムか
                    print("@1b2a")
                    self.vy = 0
                    self.jf = 0
                    self.my = 450
                else:
                    print("@1b2b")
                    pass
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
        if self.vx==0:
            if self.ct % self.ctmax < self.ctchg:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x2a,self.y2a,self.basew,self.baseh))
            else:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x2b,self.y2b,self.basew,self.baseh))
        #右向き 
        elif self.vx>0:                 
            if self.ct % self.ctmax < self.ctchg:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x0,self.y0,self.basew,self.baseh))
            else:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x1,self.y0,self.basew,self.baseh))
        #左向き 
        elif self.vx<0:#←
            if self.ct % self.ctmax < self.ctchg:
                screen.blit(self.gMap ,(self.mx,self.my),(self.x0,self.y1,self.basew,self.baseh))
            else:#←
                screen.blit(self.gMap ,(self.mx,self.my),(self.x1,self.y1,self.basew,self.baseh))

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
                    elif event.key == K_SPACE:
                        if self.jf <= 1:
                            self.vy=-15
                            self.jf += 1

    def draw_text(self, screen, font, brick):
        #マリオの位置　　　
        t = "mx=" + str(self.mx) + "  my=" + str(self.my) + "  vx=" + str(self.vx) + "  vy=" + str(self.vy)
        txt = font.render(t, True, (55, 55, 55))   # 描画する文字列の設定
        screen.blit(txt, [20, 20])# 文字列の表示位置        
        #マリオの速度など
        #t = "vx=" + str(self.vx) + "  vy=" + str(self.vy) + "   jf=" + str(self.jf)
        #txt = font.render(t, True, (55, 55, 55))   # 描画する文字列の設定
        #screen.blit(txt, [20, 80])# 文字列の表示位置        

#--------壁-------------------------------------------------------
class brick ():
    def __init__(self, rrx, rry, rrw, rrh):
        #黄色のオブジェクトの座標や大きさ
        self.rr = Rect(rrx, rry, rrw, rrh)
        self.rrx = rrx
        self.rry = rry
        self.rrw = rrw
        self.rrh = rrh

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rr)

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
    bk1 = brick(400, 400, 100, 150) #brick instance 
    bk2 = brick(300, 300, 80, 50) #brick instance 
    bk3 = brick(200, 200, 80, 50) #brick instance 
    
    while (1):
        screen.fill((255, 255, 255))  # 画面を白に
        mr1.draw_text(screen, font, bk1)
        #黄色のオブジェクト描画
        bk1.draw(screen)
        bk2.draw(screen)
        bk3.draw(screen)
        ##マリオの位置の計算
        mr1.update(bk1,bk2,bk3)
        mr1.draw(screen)
        pygame.display.update()     # 画面更新
        # イベント処理
        mr1.evt()
        clock.tick(3)

if __name__ == "__main__":
    main()

