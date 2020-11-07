"""
town.py
"""
import pygame
from pygame.locals import *
import sys
import copy
import os
import buki
import shop
import church
import hotel
import gate
import king
import drug

class Maptown():
    def __init__(self):
        self.mapt=[
            ["口","口","出","口","口","口","口","口","口","口"],
            ["口","　","　","　","　","　","　","　","　","口"],
            ["口","武","口","　","　","口","口","門","口","口"],
            ["口","口","　","　","薬","口","　","　","　","口"],
            ["口","　","　","　","　","口","城","　","　","口"],
            ["口","　","　","　","宿","口","口","口","口","口"],
            ["口","　","　","　","口","口","　","　","　","口"],
            ["口","　","口","　","　","　","　","店","　","口"],
            ["口","　","口","＋","　","＋","　","質","　","口"],
            ["口","　","口","＋","教","＋","　","　","　","口"],
            ["口","出","口","口","口","口","口","口","口","口"]
        ]
    def draw(self,ply):#描画
        os.system('cls')
        cmap=copy.deepcopy(self.mapt)
        cmap[ply.ty][ply.tx]="人"
        for i in cmap:
            for j in i:
                print(j,end="")
            print()    

def main(p1):
    p1.tx=2
    p1.ty=0
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    map2=Maptown()
    ck = pygame.time.Clock()#スピード調節
    fl = 0
    while True:
        oldtx = p1.tx
        oldty = p1.ty
        ck.tick(1) #1秒間で1フレームになるようにwait
        fl = p1.upTown(map2)
        if fl == 4 :#出口
            break
        elif fl ==2: #武器屋
            buki.main(p1)
        elif fl ==6: #店屋
            shop.main(p1)
        elif fl ==7: #薬屋
            drug.main(p1)
        elif fl ==8: #教会
            church.main(p1)
        elif fl ==10: #宿
            hotel.main(p1)
        elif fl ==30: #門
            if gate.main(p1) == 1:#宝を持っていないとき
                p1.tx = oldtx
                p1.ty = oldty
        elif fl ==31: #城
            king.main(p1)
        map2.draw(p1)
    if fl ==4:#出
        return 0#出口なので野に戻る
