import pygame
from pygame.locals import *
import sys
import copy
import random
import time
import combinient
import creature
# キー入力
class king(creature.Creature):
    def __init__(self):
        super().__init__()#親を引き継ぐ
        self.name = "太陽王"
        self.items = [
            {"name":"王の剣",  "price":300, "add":10, "weight":5},
            {"name":"王の闇の剣",  "price":200, "add":5, "weight":10},
            {"name":"剣","price":100, "add":3, "weight":15},
            {"name":"ムカつく王剣",    "price": 50, "add":2, "weight":10},
            {"name":"うんこな王剣",  "price": 30, "add":1, "weight":5}
        ]
 
    def choice(self, p1):
        self.lst()
        ch = combinient.numkey()
        if 1<= ch <= len(self.list):
            print(self.list[ch-1]["name"],"を購入",)
            p1.at += self.list[ch-1]["add"]
            print("攻撃力アップ",p1.at,"になった")
    def talk(self, p1):
        if p1.story == 1:#ストーリフラグ
            print("最近、この街で人か連続して殺されている。")
            print("内臓を食われ、ムゴい死に方だ！")
            print("人間の皮をかぶったバケモノの仕業らしい。")
            time.sleep(3)
            print()
            print("汝の手でバケモノを探ってくれ！")
            print("わしは軍隊を使って、その者を処刑する")
            time.sleep(4)
            print()
            print("よいか、この街の人間はみな正直者の正しい人間じゃ、")
            print("決して嘘はつかん　バケモノ以外はな")
            print("誰がバケモノか、わかったら戻ってこい")
            time.sleep(3)
            p1.story = 2

def main(p1):
    pygame.init()                           # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    k1 = king()#王は人として召喚
    #k1.status()
    while True:
        #自分
        print("王様：よくぞ　ここまで到達した！")
        print("　どうする？　2:話す 3:出る ")
        kk = combinient.numkey()
        if kk == 2:#話す
            k1.talk(p1)
        elif kk == 3:#出る
            break
    return 
