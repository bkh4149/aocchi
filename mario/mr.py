import pygame
from pygame.locals import *
import sys



def disp(screen,font,txt,x,y):
        tmp_txt = font.render(txt, True, (55,55,55))   # 描画する文字列の設定
        screen.blit(tmp_txt, [x, y])# 文字列の表示位置  

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    screen.fill((255,255,255))  # 画面を白に
    pygame.display.update()     # 画面更新
    gMap = pygame.image.load("sprite3.png").convert_alpha()   #マリオのマップチップ読み込み
    clock = pygame.time.Clock()#FPS設定用の準備
    font = pygame.font.Font(None, 55)               # フォントの設定(55px)

    #マリオの位置
    mx=100
    my=350
    vx=4#速度
    vy=0
    ay=1#加速度

    
    #マップチップの座標用のベース
    basew = 48
    baseh = basew*2
    #マップチップの座標
    x0 = 2*basew #2列め
    y0 = 0      #最上段　0段目
    x1 = 3*basew #3列目
    y1 = 3*basew #３段目
    
    #座った絵
    x2a = 1*basew #1列め
    y2a = 0       #最上段　0段目
    x2b = 1*basew #1列め
    y2b = 3*basew #３段目
    
    #少し伸びたチップ
    xl0 = 2*basew#２列め
    yl0 = 7*basew#7段目
    xl1 = 2*basew#3列め
    yl1 = 7*basew#7段目
    xlw = basew
    ylw = basew * 4
    
    jf = 0#ジャンプ中か 0:not 1:ジャンプ中　 2:２段ジャンプ中p
    down_ct=0#落下中カウンタ（伸びるよう）
    
    ct = 0 #アニメ用カウンタ
    ctmax = 8 #アニメ用カウンタ
    ctchg = 4 #アニメ用カウンタの定数
    
    #黄色のオブジェクトの座標や大きさ
    rrx = 400
    rry = 400
    rrw = 100
    rrh = 150
    
    rr = Rect(rrx, rry, rrw, rrh)
    
    while (1):
        screen.fill((255, 255, 255))  # 画面を白に
        t = "mx=" + str(mx) + "  my=" + str(my)
        txt = font.render(t, True, (55, 55, 55))   # 描画する文字列の設定
        screen.blit(txt, [20, 20])# 文字列の表示位置        

        t = "vx=" + str(vx) + "  vy=" + str(vy) + "   jf=" + str(jf)
        txt = font.render(t, True, (55, 55, 55))   # 描画する文字列の設定
        screen.blit(txt, [20, 80])# 文字列の表示位置        

        t = "rrx=" + str(rrx) + "  rry=" + str(rry) + "  rrw=" + str(rrw) + "  rrh=" + str(rrh)
        txt = font.render(t, True, (55, 55, 55))   # 描画する文字列の設定
        screen.blit(txt, [20, 140])# 文字列の表示位置        
        
        
        #黄色のオブジェクト描画
        pygame.draw.rect(screen, (255, 255, 0), rr)

        ##マリオの位置の計算
        #マリオがジャンプしてないとき
        if jf == 0:
            #マリオが右から走って左壁の衝突検出
            if vx < 0 and rrx+rrw-40 < mx < rrx+rrw and  rry-baseh < my < rry+rrh:
                vx = 0
                disp(screen, font, "right", 20, 200)
        
            #マリオが左から来て、右壁の衝突検出
            elif vx > 0 and rrx < mx+basew < rrx+40 and  rry-baseh < my < rry+rrh:
                vx = 0
                disp(screen, font, "left", 20, 200)

            #それ以外
            else:
                #下に台があるか
                if rry <= my+baseh <= rry+15 and rrx-basew < mx < rrx+rrw: #下に台がある場合
                    if rrx +rrw -20 < mx < rrx+rrw:
                        #jf=1
                        mx +=20
                    elif rrx -basew  < mx < rrx-basew+20:
                        #jf=1
                        mx -=20
                    else:    
                        disp(screen, font, "on the table", 20, 200)
                        mx += vx
                        my = rry-baseh #高さをrryに揃える
                    
                else:#台がない    
                    if my < 450:#空中か
                        jf = 1  # 落下モードにする
                        down_ct = +1
                        
                    else:
                        mx += vx
                        my = 450
                        down_ct = 0
                  
        #マリオがジャンプ
        elif jf >= 1:
            #マリオが速度ゼロで上にジャンプして着地、上の壁検出
            if vx == 0 and rrx-basew < mx < rrx+rrw and  rry < my+baseh < rry+50:
                vy = 0
                jf = 0
                my = rry-baseh
                disp(screen, font, "jump center", 20, 200)

            
            #マリオが右からジャンプして着地、上の壁検出
            elif vx < 0 and rrx-basew < mx < rrx+rrw and  rry < my+baseh < rry+50:
                vy = 0
                jf = 0
                my = rry-baseh
                disp(screen, font, "jump right", 20, 200)
                
            #マリオが左からジャンプして着地、上の壁検出
            elif vx > 0 and rrx < mx+basew < rrx+rrw+basew and  rry < my+baseh < rry+50:
                vy = 0
                jf = 0
                my = rry-baseh
                disp(screen, font, "jump left", 20, 200)
            
            #それ以外
            else:#x:等速　y:定加速度運動
                mx += vx
                my += vy
                vy+=ay#加速度　定加速度運動
                if my >= 450:#ボトムか
                    vy = 0
                    jf = 0
                    my = 450
                    disp(screen,font,"Bottom", 20, 200)
                else:
                    disp(screen,font,"Down", 20, 200)
                    

        ##アニメ用の設定　
        ct += 1  # 動作のカウンタ
        if abs(vx)>4:
            ctmax=4
            ctchg=ctmax/2
        elif abs(vx)>3:
            ctmax=6
            ctchg=ctmax/2
        elif abs(vx)>2:
            ctmax=8
            ctchg=ctmax/2
        elif abs(vx)>1:
            ctmax=10
            ctchg=ctmax/2
        else :
            ctmax=20
            ctchg=ctmax/2
            
        #座っているところ 
        if vx==0:
            if ct % ctmax < ctchg:
                screen.blit(gMap ,(mx,my),(x2a,y2a,basew,baseh))
            else:
                screen.blit(gMap ,(mx,my),(x2b,y2b,basew,baseh))
        #右向き 
        elif vx>0:                 
            if ct % ctmax < ctchg:
                screen.blit(gMap ,(mx,my),(x0,y0,basew,baseh))
            else:
                screen.blit(gMap ,(mx,my),(x1,y0,basew,baseh))

        #左向き 
        elif vx<0:#←
            if ct % ctmax < ctchg:
                screen.blit(gMap ,(mx,my),(x0,y1,basew,baseh))
            else:#←
                screen.blit(gMap ,(mx,my),(x1,y1,basew,baseh))
            
        
        pygame.display.update()     # 画面更新
        clock.tick(30)
        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
                
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
                else:
                    if event.key == K_LEFT:
                        vx -= 1  
                    elif event.key == K_RIGHT:
                        vx += 1  
                    elif event.key == K_UP:
                        my -= 4  
                    elif event.key == K_DOWN:
                        my += 4  
                    elif event.key == K_SPACE:
                        #print("@1 jf=",jf,"  vy=",vy)
                        if jf <= 1:
                            vy=-15
                            jf += 1
                            #print("@2 jf=",jf,"  vy=",vy)
if __name__ == "__main__":
    main()

