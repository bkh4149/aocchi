import copy
import combinient
import pygame
from pygame.locals import *
import random
import sys
import time

#自分
def player(p1,m1):
    f_battle = 0
    print("あなたのhp",p1.hp)
    print("　どうする？　1:攻撃 2:回復 3:逃走")
    kk = combinient.numkey()
    if kk == 1:
        r=random.randint(1,10)
        if r >= 9:
            print("会心の一撃")
        elif r >= 5:
            print("攻撃成功！")
        else:
            print("外した")
            r=0
        dmg = int(p1.at * p1.buki_rate * p1.level_rate[p1.level] * r/10)
        m1.hp -= dmg
        print("　敵に",dmg,"のダメージを与えた")
        time.sleep(2)
    elif kk == 2:
        p1.hp += 5
        print("　hp回復　5")
    elif kk == 3:
        p1.hp = int(p1.hp/2)
        print("　逃げ出した　")
        f_battle = 1
    return f_battle

#モンスター1匹との戦い
def monster(p1,m1):
    print("　モンスターのhp",m1.hp," 攻撃力",m1.at,"  防御力",m1.df)
    rd=random.randint(1,5)
    if m1.att > rd:
        print("まずい！　敵は攻めてきた！",end="")
        dmg = int(m1.at - (p1.df*p1.df_rate)/2)
        if dmg < 0:
            dmg = 0
        time.sleep(1)
        print("  ",dmg,"のダメージをくらった！")
        p1.hp -= dmg

def battle(p1,m1):
    pygame.init()                           # Pygameの初期化
    screen = pygame.display.set_mode((8, 6))#ダミー　これがないとキー入力を受け付けないので
    ck = pygame.time.Clock()#スピード調節

    while True:
        #自分
        f_battle = player(p1,m1)
        if p1.hp < 0 :#勝負がついた
            print("負けたようじゃな")
            break
        elif f_battle == 1:
            break
        #モンスター
        monster(p1,m1)
        if m1.hp < 0 :#勝負がついた
            print("勝ったようじゃな")
            m1.x=-1#場所を場外に移す
            m1.y=-1
            break

    if m1.hp<0:
        print("おぬしの勝ち",m1.gem,"を入手")
        time.sleep(2)
        flg=1
    elif p1.hp <0:
        print("おぬしの負け")
        time.sleep(2)
        flg=2
    elif f_battle == 1:
        flg=3
    return flg
