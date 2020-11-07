import pygame
from pygame.locals import *
import sys
import time
import combinient

# キー入力


def main():
    pygame.init()                           # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    ck = pygame.time.Clock()#スピード調節

    while True:
        #自分
        print("ムカシ,ムカシ")
        time.sleep(1)
        print("..")
        print("..")
        time.sleep(1)
        print("というわけだ！ ")
        print("理解したら 1を押してね")
        n = combinient.numkey()
        if n == 1:
            return
