import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    screen.fill((255,255,255))  # 画面を白に
    pygame.display.update()     # 画面更新
    gMap = pygame.image.load("sprite3.png").convert_alpha()   #マリオのマップチップ読み込み
    sd_hit = pygame.mixer.Sound("hit.wav")
    #マップチップの座標用のベース
    basew = 48
    baseh = basew*2
    #マップチップの座標
    x0 = 15*basew #
    y0 = 0      #最上段　0段目
    bx=180
    by=500
    fl=1
    mx=120
    my=450
    a=1
    vx=1
    vy=50
    #fire
    x1 = 10*basew #10列め
    y1 = 6*basew  #6段目
    
    
    clock = pygame.time.Clock()#FPS設定用の準備
    
    while (1):
        screen.fill((255,255,255))  # 画面を白に
        #大砲    
        screen.blit(gMap ,(mx,my),(x0,y0,basew*2,baseh))
        if fl==2: 
            screen.blit(gMap ,(mx+60,my),(x1, y1, basew, basew))
            #pygame.draw.circle(screen,(10,10,10),(bx,by),10,)
            ct +=1
            if ct >2: 
                fl=1
                ct=0
 
        #bomb
        bx+=vx
        by+=vy
        vy +=a
        
        print(bx,by,vx,vy)
        if fl>=1: 
            pygame.draw.circle(screen,(10,10,10),(bx,by),10,)
            
           
            
        pygame.display.update()     # 画面更新
        clock.tick(30)

        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
            elif event. type == KEYDOWN: 
                if event.key==K_SPACE:
                    bx = 200
                    by = 480
                    fl = 2
                    vy = -15
                    vx = 15
                    ct=0
                    sd_hit.play()
if __name__ == "__main__":
    main()