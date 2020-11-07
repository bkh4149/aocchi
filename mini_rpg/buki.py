import pygame
from pygame.locals import *
import sys
import copy
import random
import time
import combinient

# キー入力
class bukiya():
    def __init__(self):
        self.list = [
            {"name":"光の剣",  "price":500, "add":10, "weight":5},
            {"name":"闇の剣",  "price":200, "add":5, "weight":10},
            {"name":"青竜刀","price":100, "add":3, "weight":15},
            {"name":"うんこな剣",  "price": 30, "add":1, "weight":5}
        ]
    def lst(self):
        n=1
        for l in self.list:
            print(n, l["name"], "  価格", l["price"],  "  強さ", l["add"],"   重さ" ,l["weight"] )
            n += 1
    def buy(self, p1):
        self.lst()
        ch = combinient.numkey()
        if 1<= ch <= len(self.list):
            print(self.list[ch-1]["name"],"を購入",)
            if self.list[ch-1]["price"] <= p1.money:
                p1.at += self.list[ch-1]["add"]
                p1.money -= self.list[ch-1]["price"]
                p1.items.append(self.list[ch-1]["name"])
                print("攻撃力アップ",p1.at,"になった")
                print("お金が",p1.money,"になった")
            else:
                print("お金が足りんよ！")

    def talk(self):
        print("だれが人狼だって？　しらんよ")
        time.sleep(2)
    def sell(self,p1):
        print("なにをうるんだ")
        for n,item in enumerate( p1.items):
            print(n+1, item)
        ch = combinient.numkey()#▲現状４つまでしかない
        if p1.items[ch-1]=="光の剣":
            p1.items.pop(ch-1)
            p1.money += 400
            print("お金が",p1.money,"になった")
        elif p1.items[ch-1]=="闇の剣":
            p1.items.pop(ch-1)
            p1.money += 150
            print("お金が",p1.money,"になった")
        elif p1.items[ch-1]=="うんこな剣":
            p1.items.pop(ch-1)
            p1.money += 10
            print("お金が",p1.money,"になった")
        elif p1.items[ch-1]=="青竜刀":
            p1.items.pop(ch-1)
            p1.money += 80
            print("お金が",p1.money,"になった")
        else:
            print("それは買えないな")
        time.sleep(2)


def main(p1):
    pygame.init()                           # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    bk1 = bukiya()
    while True:
        #自分
        print("ヤバい武器屋へようこそ")
        print("　どうする？　1:買う 2:売る 3:出る 4:話す")
        kk = combinient.numkey()
        if kk == 1:#買う
            bk1.buy(p1)
        elif kk == 2:#売る
            bk1.sell(p1)
        elif kk == 3:#出る
            break
        elif kk == 4:#話す
            bk1.talk()
    return 
