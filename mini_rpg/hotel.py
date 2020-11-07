import pygame
from pygame.locals import *
import sys
import copy
import random
import time
import combinient

# キー入力
class shop():
    def __init__(self):
        self.list = [
            {"name":"１泊"},
            {"name":"２泊"},
            {"name":"３泊"},
        ]
    def lst(self):
        n=1
        for l in self.list:
            print(n, l["name"] )
            n += 1
    def choice(self, p1):
        self.lst()
        ch = combinient.numkey()
        if 1<= ch <= len(self.list):
            print(self.list[ch-1]["name"],"を購入",)
            p1.hp += 10*ch
    def talk(self):
        print("深夜に質屋の前を通ったらさー")
        time.sleep(1)
        print("中の人の影が狼なのを見ちゃったんだよね")
        time.sleep(1)

def main(p1):
    pygame.init()                           # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    sp1 = shop()
    while True:
        #自分
        print("hp回復の宿へようこそ、１泊で10p回復")
        print("　どうする？　1:泊まる 2:話す 3:出る ")
        kk = combinient.numkey()
        if kk == 1:#買う
            sp1.choice(p1)
        elif kk == 2:#売る
            sp1.talk()
        elif kk == 3:#出る
            break
    return 
