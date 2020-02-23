import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    sd_hit = pygame.mixer.Sound("hit.wav")

    
    
    while (1):
        screen.fill((255,255,255))  # 画面を白に
        sd_hit.play()                

        pygame.draw.circle(screen,(10,10,10),(100,100),50,)
        pygame.display.update()     # 画面更新

        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）

                
if __name__ == "__main__":
    main()