import pygame
from pygame.locals import *
import sys
import copy
import random
import time
import combinient

# キー入力
class drug():
    def __init__(self):
        self.list = [
            {"name":"闇の薬",  "price":300},
            {"name":"薬草",  "price":200},
            {"name":"効かない薬",    "price": 50},
        ]
    def lst(self):
        n=1
        for l in self.list:
            print(n, l["name"], "  価格", l["price"] )
            n += 1
    def choice(self, p1):
        self.lst()
        ch = combinient.numkey()
        if 1<= ch <= len(self.list):
            print(self.list[ch-1]["name"],"を購入",)
    def talk(self):
        print("バケモノがだれかなんて、わかんないね")
        time.sleep(2)
    def sell(self,p1):
        print("なにをうりますか")
        for n,item in enumerate( p1.items):
            print(n+1, item)
        ch = combinient.numkey()#▲現状４つまでしかない
        if p1.items[ch-1]=="薬草":
            p1.items.pop(ch-1)
            p1.money += 300
            print("資金が",p1.money,"になった")
        else:
            print("それは買えないな")
        time.sleep(2)
def main(p1):
    pygame.init()                           # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    sp1 = drug()
    while True:
        #自分
        print("くすり臭い薬屋へようこそ")
        print("　どうする？　1:買う 2:話す 3:出る 4:売る")
        kk = combinient.numkey()
        if kk == 1:#買う
            sp1.choice(p1)
        elif kk == 2:#売る
            sp1.talk()
        elif kk == 3:#出る
            break
        elif kk == 4:#売る
            sp1.sell(p1)
    return 
