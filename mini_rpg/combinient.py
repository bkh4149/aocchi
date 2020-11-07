import pygame
from pygame.locals import *
import sys
import copy
import random
import time
# キー入力
def numkey():
    kk = 0
    while kk==0:
        #イベントキューからキーボードやマウスの動きを取得
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(ないと終われない)
                sys.exit()          #終了（ないとエラーで終了することになる）
            #プレーヤの反応
            elif event.type == KEYDOWN:
                if event.key==K_1:
                    kk = 1
                elif event.key==K_2:
                    kk = 2
                elif event.key==K_3:
                    kk = 3
                elif event.key==K_4:
                    kk = 4
                else:
                    kk = 0
    return kk
