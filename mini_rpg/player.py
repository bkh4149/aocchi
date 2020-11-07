import pygame
from pygame.locals import *
import sys
import time
import creature

class Player(creature.Creature):
    def __init__(self):
        super().__init__()#親を引き継ぐ
        self.x=1#フィールドでの座標
        self.y=1
        self.tx=1#街ナカ用の座標
        self.ty=1
        self.hp = 20#ヒットポイント
        self.at = 5#攻撃力
        self.aj = 5#速度 攻撃頻度（パンチの数みたいなもの）
        self.df = 10#防御力（攻撃を受けたときのダメージをへらす）
        self.df_rate = 1.0#防御力アップ分
        self.buki = ""#装備している武器
        self.buki_rate = 1.0#攻撃力アップ分
        self.items = []#持ち物
        self.name = "山本太郎"
        self.story = 1#ストーリフラグ　話の進行に合わせてアップ
        self.money = 30#うんこな剣が買える金額

    def pr(self):
        print(self.x,self.y)

    def fight(self):
        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            #print("   up@1")
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
            elif event.type == KEYDOWN:
                if event.key==K_1:
                    print("攻撃")#攻撃
                elif event.key==K_2:
                    print("逃げる")#逃げる
                elif event.key==K_3:
                    print("薬草")#薬草

    def buy(self):
        # イベント処理
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            #print("   up@1")
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
            elif event.type == KEYDOWN:
                if event.key==K_1:
                    print("買う")#
                elif event.key==K_2:
                    print("売る")#
                elif event.key==K_3:
                    print("出る")#

    def up(self, map):
        # イベント処理
        ret = 0
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            #print("   up@1")
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
            elif event.type == KEYDOWN: 
                oldx=self.x
                oldy=self.y
                if event.key==K_LEFT:
                    self.x -= 1#横方向
                elif event.key==K_RIGHT:
                    self.x += 1#横方向
                elif event.key==K_UP:
                    self.y -= 1#たて方向
                elif event.key==K_DOWN:
                    self.y += 1#たて方向
                if map.mp[self.y][self.x]=="～" or map.mp[self.y][self.x]=="山":#動けない
                    self.x = oldx
                    self.y = oldy
                if map.mp[self.y][self.x]=="宝":
                    ret = 11
                    self.items.append("宝物") #拾ったら袋（items）に入れる
                    map.mp[self.y][self.x]="　"#地図から宝を消す
                if map.mp[self.y][self.x]=="薬":
                    ret = 12
                    self.items.append("薬草") #拾ったら袋（items）に入れる
                    map.mp[self.y][self.x]="　"#地図から消す
                if map.mp[self.y][self.x]=="町":
                    ret = 3

        #戻り値　0:なにもない　3:街   11:宝   12:薬草
        return ret  #なにもないときは必ず0を返す、そうしないとエラーになるので
    #街ナカ用
    def upTown(self, map):
        # イベント処理
        ret = 0
        lll={"武":2, "店":6, "薬":7, "教":8, "宿":10, "門":30, "城":31}
        for event in pygame.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == QUIT:      # 閉じるボタンが押されたら終了
                pygame.quit()          # Pygameの終了(ないと終われない)
                sys.exit()             #終了（ないとエラーで終了することになる）
            elif event.type == KEYDOWN: 
                oldtx=self.tx
                oldty=self.ty
                if event.key==K_LEFT:
                    self.tx -= 1#横方向
                    if self.tx < 0:
                        self.tx = oldtx
                elif event.key==K_RIGHT:
                    self.tx += 1#横方向
                    if self.tx > 10:
                        self.tx = oldtx
                elif event.key==K_UP:
                    self.ty -= 1#たて方向
                    if self.ty < 0:
                        self.ty = oldty
                elif event.key==K_DOWN:
                    self.ty += 1#たて方向
                    if self.ty > 10:
                        self.ty = oldty
                if map.mapt[self.ty][self.tx]=="出":
                    ret = 4
                elif map.mapt[self.ty][self.tx]=="口" or map.mapt[self.ty][self.tx]=="＋":
                    self.tx = oldtx
                    self.ty = oldty
                else:
                    tgt = map.mapt[self.ty][self.tx]
                    try:
                        ret = lll[tgt]
                    except KeyError:
                        ret = 0
        return ret #なにもないときは必ず0を返す、そうしないとエラー
