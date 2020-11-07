"""
total.py
単純なゲームだが、クラスをつかって構築
クラス間でのデータのやり取りを学べる

2020/07/05　
  全体を司る（total.py）を追加
　起動は　python mini/total.py
　街を追加
　町から戻るのを追加
　もどったときに位置を忘れているのを修正 (Fixed forgetting the position when you go back)
  バトルお試し用のtestを追加   Added a test to try out the battle.
"""
import pygame
from pygame.locals import *
import sys
import copy
import random
import field
import town
import battle
import monster
import player
import opening
import fish

def main():
    #召喚
    m1 = monster.Monster(4,1)
    m2 = monster.Monster(4,5)
    m3 = monster.Monster(7,5)
    mons = [m1,m2,m3]
    f1 = fish.Fish(9,2)#魚召喚
    p1 = player.Player()
    map1 = field.map()  # map召喚

    #ゲーム全体のモードのコントロール
    mode = 0
    opening.main()
    while True:
        if mode == 0:#野
            mode,id = field.main(p1, mons, f1, map1)#フィールドでの流れ
        elif mode == 3:#街ナカ
            mode = town.main(p1)#街ナカ
        elif mode == 10:#バトル
            m1 = mons[id]
            print("モンスター出現！！ 　hp", m1.hp, " 攻撃力", m1.at, "  防御力", m1.df)
            flag = battle.battle(p1,m1)#戦闘シーン
            if flag == 1:#モンスターをやっつけた
                mons.pop(id)
                mode = 0 #野
            elif flag == 2:#プレイヤが死んだらゲームオーバー
                print("game over")
                return
            elif flag == 3:#プレイヤが逃げ出した
                mode = 0 #野

if __name__ == "__main__":
    main()