"""
フィールド2
"""
import pygame
from pygame.locals import *
import sys
import copy
import os
import time

class map():
    def __init__(self):
        self.mp=[
            ["～","～","～","～","～","～","～","～","～","～"],
            ["～","、","、","、","、","、","、","～","～","～"],
            ["～","、","山","、","宝","、","、","、","～","～"],
            ["～","、","山","、","、","、","、","、","～","～"],
            ["～","、","、","、","、","、","、","、","、","～"],
            ["～","、","山","、","、","、","、","、","、","～"],
            ["～","、","、","町","、","、","、","、","～","～"],
            ["～","、","、","、","、","、","薬","～","～","～"],
            ["～","　","　","、","、","、","、","薬","～","～"],
            ["～","～","　","、","、","、","、","、","～","～"],
            ["～","～","～","～","～","～","～","～","～","～"]
        ]
    def draw(self, ply, mons, fsh):
        os.system('cls')
        cmap = copy.deepcopy(self.mp)
        cmap[ply.y][ply.x]="人"
        cmap[fsh.y][fsh.x]="魚"
        #複数のモンスター
        for m1 in mons:
            cmap[m1.y][m1.x]="も"
        #mapの描画
        for i in cmap:
            for j in i:
                print(j,end="")
            print()    

def main(p1, mons, f1, map1):
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    #map1=map()#map召喚
    flg=0
    ck = pygame.time.Clock()#スピード調節
    while (1):
        ck.tick(1) #1秒間で1フレームになるようにwait

        #プレイヤーの位値の更新
        flg = p1.up(map1)
        if flg >= 1:#町など野にあるもの以外に遭遇したか
            map1.draw(p1,mons,f1)
            if flg == 11:
                print("宝ものを見つけた",p1.items)#持ち物を表示
                time.sleep(2)
            elif flg == 12:
                print("薬草を見つけた",p1.items)#持ち物を表示
                time.sleep(2)
            elif flg == 3:#街
                break
        #モンスター
        for m1 in mons:
            m1.up(map1)#モンスターの位置を更新
        #魚
        f1.up(map1)#魚の位置を更新

        #描画
        map1.draw(p1,mons,f1)

        #モンスターが人と遭遇したか
        for i,m1 in enumerate(mons):
            if m1.x == p1.x and m1.y == p1.y:
                flg = 10
                break#forを抜ける
        if flg == 10:#モンスターと遭遇
            break # whileを抜ける
    print("@2 flg=",flg,"  i=",i)
    return flg,i
