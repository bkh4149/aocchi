import pygame
from pygame.locals import *
import sys
import copy
import time

def main(p1):
    pygame.init()                           # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    while True:
        #自分
        if "宝物" in p1.items:
            print("王の城だぞ　無礼のないようにな！")
            time.sleep(2)
            return 0
        else:
            print("王の城だぞ　宝は持っていないのか")
            print("帰れ！")
            time.sleep(2)
            return 1
