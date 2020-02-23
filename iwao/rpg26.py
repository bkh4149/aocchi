# coding: utf-8


""" rpg.py 
パズルRPG

rpg24　2017/09/25
  ハエ男はハエ男をすり抜けられないようにする

rpg23　2017/09/25
　ステージ１　薬草100本集めるクリア
　ステージ０　薬草30本集めたらクリア 

パズルRPG
rpg22　2017/09/20
　ハエ男が薬草を通り抜けられないのはおかしい
　

rpg21　2017/09/20
　ハエ男はハエ男で塞げ
　死んだハエ男が邪魔で他のハエ男が通過できなくなるよ


rpg20　2017/09/20
　ステージ１クリアの条件
　　薬草を50個get


rpg19　2017/09/18
 真面目にヒットポイントがゼロになったときの処理を作る
　「死んでしまうとは情けない」
　　もう一度頑張るか（y/n）

rpg18　2017/09/18
 とりあえず１ステージでは薬草がポイントでいい
　ハエ男から逃げながらの薬草作り
　薬草はランダムに生えるという設定


rpg17　2017/09/10

アイデイア
　ハエ男の死骸はしばらく置いておくと腐ってキノコが生えてくる
　そのキノコはムシキノコといい港で売れる（結構高価）
　（また、ハエ男に対してかなりの攻撃力がある（ほぼ一発で仕留められる））
　というより、ハエ男を一時的に動けなくシてしまう（そのすきに逃げられる）
　港では船がやってくると武器を買うことが出来る

rpg16　2017/09/09
 hp　と薬草を表示する
 薬草を採れるようにした

　アイデア
　　石を積めるようにする
　　なるべくたくさん並べると高得点
　
　　or　穴に落とす

　　or　海に埋めて隣の島まで行く




rpg15　2017/09/08
　とりあえず薬草をつくる
　

  変数変更
　
　変化しない
　　通過できる
　　　野　	0	NO

　　通過できない
　　　森	201	BUSH
　　　山	202	YAMA
　　　海	203	UMI

　
　変化する

　　  石	50	ISHI　	味方に押されると動く
　　　穴	51	ANA	穴掘り名人（101）に掘られると穴が開く　小さい穴と大きな穴
　　　穴2	52	ANA2	掘り始め
　　　穴3	53	ANA3	途中
　　　薬草	61	YAKU	薬草　成長　（種→若葉→成長
　　　薬草2	62	YAKU2	薬草　種
　　　薬草3	63	YAKU3	薬草　若葉
　　　薬草4	64	YAKU3	薬草　枯れ

　動く
　　　自分　　	100	PLYR	プレイヤー
　　　自分　　	100	PLYR2	レベル2
　　　自分　　	100	PLYR3	レベル3

　　　穴掘り	110		ステージ2で登場


　　　ハエ男	200	HAE	味方と遭遇すると戦闘モードになる
　　　ゲジ男	210	GEJI	味方と遭遇すると戦闘モードになる


rpg14　2017/09/07

 思いついたこと
　自ら陣地を築いた後、その中で平和にクラス
　　中で薬草栽培
　　海から外国人がやってきて貿易をする
　　巨石は大変高価　（彼らに巨石は動かせない）
　　それを船まで積めたら薬草20個と交換とか
　　薬草はちょっと効き目がなさすぎるので効果を３倍にする

アイデア
    森には石が置けない
　　　ハエ男（巨大モンスターは通れない）が小さいハエ男は通れる
　　　ハエ男は通れる

rpg13.py　2017/09/06
　大幅に構造を変えたのでハエ男が出ない、戦闘モードにもならない、ので直した

　キャラはアニメーション
　回復の薬草をget出来るようにする


課題
　ハエ男が死んだ後、残骸が残っている　消えるようにしたい
　徐々に腐るというのも面白いのかも

　薬草は育つようにしたい
　一回刈ってもまた生えてくるみたいな
　種を採って栽培も可能みたいなこと

　
rpg
～～～～～～～～～～～～～～～～～～～～～～～～～
ストーリー

＊第一話　ハエ男の大発生
よいか
今のお前ではハエ男に勝てぬ
やつらと戦ってなならぬ

なあに、冬になって寒くなれば
やつらは勝手に死ぬ
それまでのしんぼうじゃ

あっ、それと
島の薬そうはなるべくたくさん採っておけ
いざという時に役に立つからな

そして、冬になったらほこらにいってみるといい
また、会おう

おっと忘れておった
お前には巨石を動かす力がある
その力を使って身を守るのじゃ
　　　石
虫　　石　人
　　　石

斜めの壁はときどき突破される
　　　石
　　石　虫人
　石


こうして補強すれば大丈夫
　　　石
虫　石石　人
　石石
～～～～～～～～～～～～～～～～～～～～～～～～～

rpg12.py　2017/09/06

　大幅に構造を変えた
　テーブルを二枚用意、一枚は動かないモノ（海や野など）、
　もう一枚は動くもの（人、石など）
　ぶつかり判定は個別にやるのではなくて、動くもののテーブルをみて行う

　動かない
　　野０　森１　山２　海３	
　　野以外の場所には動けない
　
　動くもの
　　０：何もない

　　５０：石　	味方に押されると動く
　　５１：穴	穴掘り名人（１０１）に掘られると穴が開く　小さい穴と大きな穴
　　５２：やくそう　育つ　種→若葉→成長

　　100：味方　１００
　　101：堀さん　穴堀名人　ステージ２で登場

　　200:ハエ男（味方と遭遇すると戦闘モードになる）
　　201:ハエ男の死骸
　　202:虫キノコ
　　220:ゲジ男

　とりあえず石を動くようにした
　しかし大幅に変えたのでハエ男が出ない、戦闘モードにもならない
　次はここを直す

rpg11.py　2017/08/30
　石を表示、動かせるようにする
　石を動かすときは石の外側に回って押すだけでいい

　まずは画面上に石を配置する

  tb_map[]にはハエ男や人は描かない、背景のみ
　これらはアニメーションするので都度、彼らのx,yから別別に描いていく

　石とか穴の扱いはどうするか
　　50番代に　して、海や山とはちょっと違う
　　しかし、背景描画時に一緒に描くみたいな感じかな
　　これらはアニメーションしないので

  とはいえ今後いろんなキャラが増えてきたときに、個別で当たり判定をやっていると
　とても大変なことになる
　なので、tb_map[][]で一元管理しておくことにする


　今のところ
　　野０　森１　山２　海３	
　　石５０　穴５１
　　味方１００
　　敵２００
　　と言った感じに決めておく


　ぶつかり判定はワンループ（1/30秒）で二回やらないように注意が必要
　例えば

　ループ
　　味方
　　敵
　　背景
　ループ終了

　という流れだと、味方でぶつかり判定して、敵でもぶつかり判定すると
　ぶつかったときのルーチンを二回やってしまうことになる


rpg10.py　2017/08/19

　戦闘で逃げる
  戦闘時、アクションの結果は１秒にしているが　hit　any　keyとする

  2017/08/29やっとHITANYKEYができた

 elif event.type == KEYDOWN: でeventを取得した後
event.typeを見るのではなくてevent.keyを見れば良いのだった。
      num=event.key　★ここがポイントだった
理由については未だに不明だが...


    #キーが押されるまでstop
    def hitanykey(self,xx3,yy3,yl):
        mm="すすむにはなにかキーを押してね"
        tm = ft_small.render(mm, False,(0,0,0))
        sc.blit(tm,(xx3,yy3+yl*2)) 
        pygame.display.update()

        kn=0
        while kn==0:
            kn=self.getkey3()


    #hit any キー入力　(キーが押されるまでstopで使う)
    def getkey3(self):
        num=0
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame. quit() 
                sys. exit()
            elif event.type == KEYDOWN: 
                num=event.key　★ここがポイントだった
        return num


rpg9.py　2017/08/19
　戦闘で戦うをやる

　戦う　は敵のhpを減らす　30-80のダメージ

　逃げるは　-50のダメージでフィールドに戻る

　いずれにしても１ターン毎に敵から攻撃を食らって30-80のダメージを受ける
　hpがゼロなら負け「しんでしまうとはなさけない」を表示
　

rpg8.py　2017/08/19
 
　ハエ男から１マス分まで近づくと戦闘が始まる
　最初はハエ男は強いので逃げるべし
　ただし、追いつかれるとやばいので、前もってトラップ（穴）を仕掛けておくみたいなことができるようにしたい

  ハエ男が追いかけてくる感じなのでそれぞれのハエ男に
　プレイヤーのデータ（hpや座標など）を渡し、ハエ男の中で戦闘
　　　戦闘はとりあえず　薬草をつかうまで

rpg7.py　2017/08/19

 とりあえずハエ男を登場させてぶらぶら動かすまで



rpg6.py　2017/08/18
  ブッシュや海山は通れないようにする

        #フィールド　野以外はいけない
　ようにした

rpg5.py　2017/08/17
  　フィールドプレイヤー表示できたがキー入力で時々止まる
　  ランダムで抜ける部分をコメントアウトし忘れ、戦闘モードはまだ作っていなかったのだ
　　正しく動いていたのだ

    mapに山と海を追加

rpg4.py　2017/08/17
　クラス化、セオリーにしたがってアイコンでクラス化する

　　フィールド map
　　プレイヤー player

  　フィールドプレイヤー表示できたがキー入力で全く動かない

　　　　ハエ男　これはver5で

　結構集中が必要、3,4時間まとめてやったほうがいい
　　大まかなプログラム構造や、座標とかは紙に書くといい

　あと、ある程度作ったらとにかく動かしたほうが速い
　pythonはエラーメッセージが優秀なので

rpg2.py　2017/08/11



  とりあえず、歩いていたら
　　適当にハエ男がでてきて戦ったり
　　茂みでは回復の薬草が取れる
　　歩くとヒットポイントがマイナス１

●ハエ男との戦い
　そいつをやっつける

　１：戦う　　　　　敵に30-50のダメージで、こちらもヒットポイントを10-30失う
　２：逃げる　　　　ヒットポイントを50失う
　３：回復の薬草　　ヒットポイントを10-20回復
　４：魔法を使う　　敵全体にダメージ　レベルアップして魔術が使える場合のみ

　みたいな形で選択

　どちらかのヒットポイントがゼロになったら勝ち負けが確定
　自分が負けたら終了

　３匹やっつけたらレベルアップ



rpg1.py　2017/08/11

　キー入力を受け付ける
　上下左右に画面をスクロールして

  プレイヤーがアニメで少し動く
　　歩いている感じ


rpg.py　2017/08/10
　全マップは配列行列で持っておく
　その一部を表示させる
　テストでスクロールしてみるまで

全マップ
　3200*2400ドット（64*48　マス　
　背景行列tb_map[]　

表示部分　画面に見えている部分
　800*600ドット　（16＊12　マス
　背景表示の位置を表す変数
　　xms(0,47)　xmsから幅の分(16マス)
　　yms(0,35)　ymsから縦横行の長さのぶん(12マス)

プレイヤーの位置　（マスで数える
　xply(0,63),yply(0,47)
　移動は　上下1マスずつだが、
　　画面上で移動せず、背景が動く、キャラは向きがかわる
　　　上下左右のキーをgetしたらvx,vyをひとマスずつ動かしすぐにゼロに戻す　




"""
#------------準備---------------------------------------------------

import math
import random
import time
import sys 
import pygame 
from pygame.locals import *
#from pygame.locals import QUIT, Rect

#-----------------------------
#変化しない　map上に書く
NO=0    #野
BUSH=201#森	201	BUSH
YAMA=202#山	202	YAMA
UMI=203 #海	203	UMI

#若干変化するが動かない→map上に書く

ISHI=50	#石	50	ISHI　	味方に押されると動く
ANA=55	#　　　穴	55	ANA	穴掘り名人（101）に掘られると穴が開く　小さい穴と大きな穴
"""
　　　穴2	56	ANA2	掘り始め
　　　穴3	57	ANA3	途中
"""

YAKU=61	#薬草	61	YAKU	薬草　成長　（種→若葉→成長
"""
　　　薬草2	62	YAKU2	薬草　種
　　　薬草3	63	YAKU3	薬草　若葉
　　　薬草4	64	YAKU3	薬草　枯れ
"""

SIGAI=70	#ハエ男の死骸
MUSHITAKE1=71	#虫たけ

#-----------------------------
#動き回る　chr上に書く

NON=0
PLYR=100#自分　　	100	PLYR	プレイヤー
HORI=110#穴掘り	110		ステージ2で登場

#TEKI
HAE=200#ハエ男	200	HAE	味方と遭遇すると戦闘モードになる
GEJI=210#ゲジ男	210	GEJI	味方と遭遇すると戦闘モードになる

pygame.init()

#global
sc = pygame.display.set_mode(( 800, 600))

#for windows
msgothic = r'c:\windows\fonts\msgothic.ttc'

#for linux
#msgothic ="/usr/share/fonts/truetype/takao-gothic/TakaoExGothic.ttf" 

#文字表示用フォント
ft_small = pygame.font.Font(msgothic, 24)
ft_mid= pygame.font.Font(msgothic, 48)
ft_big= pygame.font.Font(msgothic, 72)


#背景行列
tb_map = [[0 for x in range(64)] for y in range(48)]#変化しない　野、海、山、川、森
tb_chr = [[0 for x in range(64)] for y in range(48)]#変化する　プレイや、ハエ男　石

#------------クラス---------------------------------------------------
#ハエ男

class monster():

    #戦闘画面で使用
    gbg1 = pygame.image.load("bug1.png").convert_alpha()#　200 200
    gbg2 = pygame.image.load("bug2.png").convert_alpha()#　200 200

    xmm=0#プレイヤーの位置
    ymm=0
   
    keitai=1#形態　1:普通　2:仮死状態　3:復活直前　4:凶悪化
    hp=200#最初のｈｐ
    ct_a=0


    def __init__(self):
        self.xmm=10#プレイヤーの位置
        self.ymm=10
        self.keitai=1#レベル
        self.hp=200#最初のｈｐ
        self.ct_a=00#

    #モンスター　形態に応じた分岐
    def calc_monster(self,pl):
        if self.keitai==1:
            self.calc_m1(pl)
        elif self.keitai==2:
            self.calc_m2(pl)
        elif self.keitai==3:
            self.calc_m3(pl)
        elif self.keitai==4:
            self.calc_m4(pl)
        else :
            pass

    #第一形態
    def calc_m1(self,pl):
        fout=0
        #乱数に応じ、ハエ男の次の仮位置の計算
        tx=self.xmm+random.randint(0,2)-1
        ty=self.ymm+random.randint(0,2)-1

        #import pdb;pdb.set_trace() #debug

        #まずは枠内かのチェック
        fl= self.check_monster(tx,ty)

        if fl==0:#枠内ならば

            #枠内かつ(野または薬草）ならば
            if tb_map[ty][tx]==NO or tb_map[ty][tx]==YAKU:
                #位置の更新
                tb_chr[self.ymm][self.xmm]=NON   #古い位置にいたハエ男を消す
                tb_map[self.ymm][self.xmm]=NO    #古い位置に生えていた薬草を消す
                self.xmm=tx
                self.ymm=ty
                tb_chr[self.ymm][self.xmm]=HAE #新しい位置に移動する

        #周囲１マス以内にプレイヤーがいたなら戦闘モード開始
        xt=pl.xmp-self.xmm
        if -1<=xt and xt<=1:
            
            yt=pl.ymp-self.ymm
            if -1<=yt and yt<=1:
                fout=self.battle(pl)
                #fout 0:  1:plがやられた　2:ハエ男がやられた　3:両方やられた　4:plが逃げた

        if fout==2:
        #2:ハエ男がやられた
            #tb_map[self.ymm][self.xmm]=SIGAI
            #tb_chr[self.ymm][self.xmm]=NON
            self.keitai=2#形態を変えるだけ
            fout=0       #ハエ男は死なない　
        return fout




    #第2形態
    def calc_m2(self,pl):
        fout=0

        #周囲１マス以内にプレイヤーがいたなら戦闘モード開始
        xt=pl.xmp-self.xmm
        if -1<=xt and xt<=1:
            yt=pl.ymp-self.ymm
            if -1<=yt and yt<=1:
                fout=self.battle(pl)
                #fout 0:  1:plがやられた　2:ハエ男がやられた　3:両方やられた　4:plが逃げた
        """
        if fout==2:
        #2:ハエ男がやられた
            tb_map[self.ymm][self.xmm]=SIGAI
            tb_chr[self.ymm][self.xmm]=NON

        """
        return fout

    #動けるかどうかチェック,外れていたら1（動けない）を戻す　OKならゼロ
    def check_monster(self,x,y):
        #結果はfkagで　0:動けるよ　1:そっちには動けないお
        flag=0

        #枠内かどうか
        if x<8 or x>56:
            flag=1
        if y<6 or y>42:
            flag=1

        #他のハエがいるか いるなら１（動けない）
        if tb_chr[y][x]==HAE:
            flag=1
        return flag #結果　0:動けるよ　1:そっちには動けないお

    #-----ここからちょっと毛色が違う処理------------------
    def battle(self,pl):
        cb = pygame.time.Clock()
        ct=0
        fout=0#脱出フラグ　1:脱出　
        # 0:  1:plがやられた　2:ハエ男がやられた　3:両方やられた　4:plが逃げた

        #タイトル,ハエ男表示位置
        xx=100
        yy=70

        #コマンド　表示位置
        xx2=150
        yy2=400

        #状態表示位置
        xx3=400
        yy3=400
    
        while True:
            #xms,yms=getkey(xms,yms)
            sc.fill(( 230, 0,0))

            #ハエ男表示
            self.disp_monster(ct,xx,yy)

            #プレイヤー選択
            yl=30

            mm="Level="+str(pl.lv)+"  HP="+str(pl.hp)
            tm = ft_small.render(mm, False,(0,0,0))
            sc.blit(tm,(xx2,yy2)) 


            mm="どうしますか？"
            tm = ft_small.render(mm, False,(0,0,0))
            sc.blit(tm,(xx2,yy2+yl*1)) 
    
            mm="１：たたかう"
            tm = ft_small.render(mm, False,(0,0,0))
            sc.blit(tm,(xx2,yy2+yl*2)) 
    
            mm="２：にげる"
            tm = ft_small.render(mm, False,(0,0,0))
            sc.blit(tm,(xx2,yy2+yl*3)) 
    
            mm="３：やくそう"
            tm = ft_small.render(mm, False,(0,0,0))
            sc.blit(tm,(xx2,yy2+yl*4)) 
            
            #戦闘モードのキー入力　(1-3だけ返す)
            #def getkey2(self):
            #　　結果　1:戦う　2:逃げる　3:やくそう
            num=self.getkey2()

            if num==1:
                mm="勇者はハエ男に突っ込んでいった"
                tm = ft_small.render(mm, False,(0,0,0))
                sc.blit(tm,(xx3,yy3)) 

                hp_atk=random.randint(30,100)#ハエ男のダメージ
                hp_dmg=random.randint(30,100)#プレイヤーのダメージ

                mm="敵に"+str(hp_atk)+"、自分に"+str(hp_dmg)+"のダメージ"
                self.hp-=hp_atk #ハエ男に攻撃、hpを奪う
                pl.hp-=hp_dmg   #プレイヤーのダメージ分hpが奪われた
                tm = ft_small.render(mm, False,(0,0,0))
                sc.blit(tm,(xx3,yy3+yl*1)) 
                pygame.display.update()

                self.hitanykey(xx3,yy3,yl)

                if self.hp<0:
                    fout=2
                    break
                if pl.hp<0:
                    fout+=1
                    break


                #tn=self.getkey3()
                #cb.tick(1) #1秒

            elif num==2:
                pl.hp-=50#逃げのペナルティ
                fout=4
                break


            elif num==3 and pl.yaku>=1:
                mm="薬草をつかった"
                tm = ft_small.render(mm, False,(0,0,0))
                sc.blit(tm,(xx3,yy3)) 
                pl.hp+=50	#hp
                pl.yaku-=1	#薬草マイナス

                mm="ヒットポイントは"+str(50)+"回復"
                tm = ft_small.render(mm, False,(0,0,0))
                sc.blit(tm,(xx3,yy3+yl*1)) 
                pygame.display.update()

                self.hitanykey(xx3,yy3,yl)


                #cb.tick(0.8) #1秒

            #Gメモリ表示
            pygame.display.update()
            cb.tick(30) #毎秒30フレーム
    
        #while end
        return fout

    #キーが押されるまでstop
    def hitanykey(self,xx3,yy3,yl):
        mm="すすむにはなにかキーを押してね"
        tm = ft_small.render(mm, False,(0,0,0))
        sc.blit(tm,(xx3,yy3+yl*2)) 
        pygame.display.update()

        kn=0
        while kn==0:
            kn=self.getkey3()


    #hit any キー入力　(キーが押されるまでstopで使う)
    def getkey3(self):
        num=0
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame. quit() 
                sys. exit()
            elif event.type == KEYDOWN: 
                num=event.key
        return num



    def disp_monster(self,ct,xx,yy):
            #hp_monster=100
            
            mm="ハエ男登場"+str(self.hp)
            tm = ft_big.render(mm, False,(0,0,0))
            sc.blit(tm,(xx,yy)) 

            #黒枠
            col=(0,0,0)
            pygame. draw.rect( sc, col,Rect(xx,yy+100,650,180)) 
            #キャラを少し動かす
            #　　将来的にはここでリアルゲーム要素を入れる　インベーダー的な
            ct+=1
            if ct<10:
                sc.blit(self.gbg1 ,Rect(xx+200,yy+100,200,200))
            elif ct<20:
                sc.blit(self.gbg2 ,Rect(xx+200,yy+100,200,200))
            else:
                ct=0
            return ct
    
    
    #戦闘モードのキー入力　(1-3だけ返す)
    #1:戦う　2:逃げる　3:やくそう
    def getkey2(self):
        num=0
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame. quit() 
                sys. exit()
            elif event.type == KEYDOWN: 
                if event.key==K_1:
                  num=1
                elif event.key==K_2:
                  num=2
                elif event.key==K_3:
                  num=3
    
        return num


#------------クラス---------------------------------------------------

#人

class player():

    xmp=8#プレイヤーの位置
    ymp=6
    lv=1#レベル
    hp=100#最初のｈｐ
    yaku=0#薬草　

    def __init__(self):
        self.xmp=8#プレイヤーの最初の位置
        self.ymp=6
        self.lv=1#レベル
        self.hp=100#最初のｈｐ
        self.yaku=0#薬草　

    def calc_player(self):

        #キーボード取得
        xk,yk=self.getkey()
        #import pdb;pdb.set_trace() #debug

        #キーボードに応じて位置の計算
        #とりあえずtx,tyに新しい位置を記録しておく
        tx=self.xmp+xk
        ty=self.ymp+yk

        #まず枠内かどうかチェックし、中ならfl=0、外れていたらfl=1
        fl=self.check_player(tx,ty)

        #枠内なら以下実行
        if fl==0 :

            #枠内かつ野だった
            if tb_map[ty][tx]==NO:

                #tb_char上の位置を更新　　
                tb_chr[self.ymp][self.xmp]=0

                #プレイヤーの位置x,yを更新　　
                self.xmp=tx
                self.ymp=ty


                #tb_char上の位置を更新　　
                tb_chr[self.ymp][self.xmp]=100

            #枠内かつ薬草だった
            elif tb_map[ty][tx]==YAKU: 

                #tb_char上の位置を更新　　
                tb_chr[self.ymp][self.xmp]=0

                #プレイヤーの位置x,yを更新　　
                self.xmp=tx
                self.ymp=ty
                self.yaku+=1

                #tb_char上の位置を更新　　
                tb_chr[self.ymp][self.xmp]=100

                #tb_map上の薬草をなくす
                tb_map[ty][tx]=0


            #石だった場合
            elif tb_map[ty][tx]==50:
                #更にもう1マス先を見る
                ttx=tx+xk
                tty=ty+yk
                #そこが枠内かどうかチェックし、中ならfl2=0、外れていたらfl2=1
                fl2=self.check_player(ttx,tty)
                #枠内なら以下実行
                if fl2==0 :
                    #枠内かつ野だった
                    if tb_map[tty][ttx]==0: 

                        #プレイヤー位置更新
                        tb_chr[self.ymp][self.xmp]=0
                        self.xmp=tx
                        self.ymp=ty
                        tb_chr[self.ymp][self.xmp]=100

                        #石も動かす
                        tb_map[tty][ttx]=50 
                        tb_map[ty][tx]=0 

        #end(if fl==0 :)

        #フィールド　野以外はいけない
        return self.xmp,self.ymp


    #枠内かどうかチェック,外れていたら-1を戻す
    def check_player(self,x,y):
        flag=0
        if x<8 or x>56:
            flag=1
        if y<6 or y>42:
            flag=1
        return flag


    #イベント　キーボード取得
    #http://westplain.sakuraweb.com/translate/pygame/Key.cgi
    def getkey(self):
        x=0
        y=0
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame. quit() 
                sys. exit()
            elif event.type == KEYDOWN :
                if   event.key==K_LEFT :
                    x=-1
                elif event.key==K_RIGHT:
                    x=1
                elif event.key==K_UP   :
                    y=-1
                elif event.key==K_DOWN :
                    y=1
        return x,y



#------------クラスmap---------------------------------------------------

#map　背景など
class map():

    gNO  = pygame.image.load("green.png").convert_alpha() #野　50x50
    gBUSH= pygame.image.load("green2.png").convert_alpha()#森　50x50
    gUMI = pygame.image.load("sea.png").convert_alpha()   #海　50x50
    gYAMA = pygame.image.load("mount.png").convert_alpha() #山　50x50
    gISHI = pygame.image.load("stone.png").convert_alpha() #石　50x50
    gYAKU = pygame.image.load("yaku.png").convert_alpha()  #薬草　50x50
    gSIGAI = pygame.image.load("shigai.png").convert_alpha()  #死骸　50x50
    gMUSHITAKE1 = pygame.image.load("mushitake1.png").convert_alpha()  #虫タケ1　50x50


    #プレイヤー
    gPLYR1 = pygame.image.load("man1.png").convert_alpha()#　50x50
    gPLYR2 = pygame.image.load("man2.png").convert_alpha()#　50x50

    #ハエ男
    gHAE1 = pygame.image.load("bug1.png").convert_alpha()#　50x50
    gHAE2 = pygame.image.load("bug2.png").convert_alpha()#　50x50

    act=0

    def __init__(self):

        #石
        for i in range(300):
            rx=random.randint(0,63)
            ry=random.randint(0,47)
            tb_map[ry][rx]=ISHI

        #薬草
        for i in range(50):
            rx=random.randint(0,63)
            ry=random.randint(0,47)
            tb_map[ry][rx]=YAKU

        #虫take0
        for i in range(5):
            rx=random.randint(0,63)
            ry=random.randint(0,47)
            tb_map[ry][rx]=SIGAI

        #虫take1
        for i in range(5):
            rx=random.randint(0,63)
            ry=random.randint(0,47)
            tb_map[ry][rx]=MUSHITAKE1



        #山
        for i in range(600):
            rx=random.randint(0,63)
            ry=random.randint(0,47)
            tb_map[ry][rx]=YAMA



        #海
        for yi in range (48):#海
            tb_map[yi][7]=UMI
            tb_map[yi][63]=UMI
            tb_map[yi][56]=UMI


        #海
        for xi in range (64):#海
            tb_map[5][xi]=UMI
            tb_map[37][xi]=UMI


        #野
        for yi in range (4):
            for xi in range (4):
                tb_map[6+yi][8+xi]=NO

        self.act=0

#hpや薬草など状態表示
    def draw_status(self,pl):
        mm="hp:"+str(pl.hp)+"  薬草："+str(pl.yaku)
        tm = ft_small.render(mm, False,(0,0,0))
        sc.blit(tm,(600,550)) 


#ハエ男や人など動くものをまとめて描画
    def draw_char(self,xms,yms):

        #xmd,ymdはマス座標（フィールドテーブルの中のどこを描くか）
        #xms,ymsはマス座標（フィールドテーブルの中（マップ）の書き始めの位置
        #xi,yi  はマス座標（たんなるカウンタ、for文中のiみたいなもの）
        #　　　　　　　　　　xmc:0-15,　ymc:0-11
        #xs,ysはスクリーン座標

        self.act+=1#カウンタ+1
        if self.act==10:
            self.act=0

        for yi in range(12):
            ymd=yi+yms
            ys=yi*50

            for xi in range(16):
                xmd=xi+xms
                xs=xi*50

                #x,yはスクリーン座標

                #ハエ男
                if tb_chr[ymd][xmd]==HAE:
                    if self.act<=5:
                        sc.blit(self.gHAE1 ,Rect(xs,ys,50,50))
                    else:
                        sc.blit(self.gHAE2 ,Rect(xs,ys,50,50))
                #人
                elif tb_chr[ymd][xmd]==PLYR:
                    if self.act<=5:
                        sc.blit(self.gPLYR1 ,Rect(xs,ys,50,50))
                    else:
                        sc.blit(self.gPLYR2 ,Rect(xs,ys,50,50))


    #import pdb;pdb.set_trace() #debug


#map描画
#テーブル上の座標と表示上の座標は異なる

    def draw_map(self,xms,yms):

        #xmd,ymdはマス座標（フィールドテーブルの中のどこを描くか）
        #xms,ymsはマス座標（フィールドテーブルの中（マップ）の書き始めの位置
        #xi,yi  はマス座標（たんなるカウンタ、for文中のiみたいなもの）
        #　　　　　　　　　　xmc:0-15,　ymc:0-11
        #xs,ysはスクリーン座標
        for yi in range(12):
            ymd=yi+yms
            ys=yi*50

            for xi in range(16):
                xmd=xi+xms
                xs=xi*50

                #x,yはスクリーン座標
                #野
                if tb_map[ymd][xmd]==NO:
                    sc.blit(self.gNO ,Rect(xs,ys,50,50))

                #森
                elif tb_map[ymd][xmd]==BUSH:
                    sc.blit(self.gBUSH ,Rect(xs,ys,50,50))
                #海
                elif tb_map[ymd][xmd]==UMI:
                    sc.blit(self.gUMI ,Rect(xs,ys,50,50))
                #山
                elif tb_map[ymd][xmd]==YAMA:
                    sc.blit(self.gYAMA ,Rect(xs,ys,50,50))

                #石
                elif tb_map[ymd][xmd]==ISHI:
                    sc.blit(self.gNO ,Rect(xs,ys,50,50))
                    sc.blit(self.gISHI ,Rect(xs,ys,50,50))

                #薬草
                elif tb_map[ymd][xmd]==YAKU:
                    sc.blit(self.gNO ,Rect(xs,ys,50,50))
                    sc.blit(self.gYAKU ,Rect(xs,ys,50,50))

                #死骸
                elif tb_map[ymd][xmd]==SIGAI:
                    sc.blit(self.gNO ,Rect(xs,ys,50,50))
                    sc.blit(self.gSIGAI ,Rect(xs,ys,50,50))


                #虫タケ1
                elif tb_map[ymd][xmd]==MUSHITAKE1:
                    sc.blit(self.gNO ,Rect(xs,ys,50,50))
                    sc.blit(self.gMUSHITAKE1 ,Rect(xs,ys,50,50))

#------------ここまでクラス---------------------------------------------------




#------------ここからメインの関数-------------------------------------------


#フィールドモード
def md_field(ck,pl,mp):

    mt=[]#monster　何匹出るか不明なのでとりあえず
    ct_m=0

    #★ここが実質上のループ　一番使用頻度が高いはず
    while True:
        #1ループに1回やること
        #プレイヤー キー入力、位置計算
        xpl,ypl=pl.calc_player()

        #map表示　最初にマップを描いて,あとでその上にプレイヤーやハエ男を載せる
        mp.draw_map(xpl-8,ypl-6)
        #mapの書き始めは左上の位置を与えるので、プレイヤ位置から-8,-6している

        #100ループに1回やること　薬草
        if ct_m%100==0:
        #薬草
            rx=random.randint(9,55)
            ry=random.randint(7,39)
            if tb_map[ry][rx]==NO:
                tb_map[ry][rx]=YAKU

        #10ループに1回やること
        if ct_m%10==0:

            #ランダムでハエ男発生　
            rr=random.random()
            if rr<0.1:
            #if rr<0.01:
                #import pdb;pdb.set_trace() #debug

                #ハエ男発生
                #クラス　コンストラクタ　配列使用
                mt.append(monster())

            #ハエ男の位置の更新　10ループに一回
            for i in reversed(range(len(mt))):
                fout=mt[i].calc_monster(pl)
                #fout 0:  1:plがやられた　2:ハエ男がやられた　3:両方やられた　4:plが逃げた
                if fout==2:#ハエ男を消す
                    mt.pop(i)

        ct_m+=1#ループカウンタ更新
        if pl.hp<0:
            break

        #char表示（動くものを描画）　プレイヤーやハエ男を載せる
        mp.draw_char(xpl-8,ypl-6)
        #mapの書き始めは左上なので、プレイヤ位置から-8,-6して与える

        #状態表示
        mp.draw_status(pl)


        #Gメモリ表示
        pygame.display.update()
        ck.tick(30) #毎秒30フレーム

    #while end


def disp_level(level,hp,money):
    x1=100
    y1=400
    
    col=(100,100,100)
    pygame. draw.rect( sc, col,Rect(x1,y1,600,50)) 
    
    mm="れべる＝"+str(level)+"　ひっと＝"+str(hp)+"　おかね＝"+str(money)
    tm = ft_small.render(mm, False,(0,0,0))
    sc.blit(tm,(x1,y1)) 
    

#------------ここからメイン関数---------------------------------------------------
def y_key():
        #yキーが押されたかチェック
        kn=0
        while kn==0:
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame. quit() 
                    sys. exit()
                elif event.type == KEYDOWN: 
                    kn=event.key
                    if event.key==K_y:
                      kn=1
        return kn

#------------ここからメイン関数---------------------------------------------------
def main():


    #テーブル初期化
    for iy in range (48):
        for ix in range (64):
            print(ix,iy)
            tb_map [iy][ix]=0
            tb_chr [iy][ix]=0

    ck = pygame.time.Clock()

    sc.fill(( 0, 255,0))#緑バック
    mm="薬草30本集めよ..."
    tm = ft_big.render(mm, False,(0,0,0))
    sc.blit(tm,(100,100)) 

    mm="わかったらなにかキーを押してね"
    tm = ft_small.render(mm, False,(0,0,0))
    sc.blit(tm,(100,200)) 

    pygame.display.update()


    k=y_key()

    sc.fill(( 255, 255, 255))#白バック

    pl=player()#プレイヤー生成　コンストラクタ
    mp=map()#フィールド生成

    #メインループ
    md_field(ck,pl,mp)

    #プレイヤーのhp<0か？
    if pl.hp<0:
        sc.fill(( 0, 0, 255))#青バック
        mm="死んだよー..."
        tm = ft_big.render(mm, False,(0,0,0))
        sc.blit(tm,(100,100)) 

        mm="もう一度プレーするならyを押してね"

        tm = ft_small.render(mm, False,(0,0,0))
        sc.blit(tm,(100,200)) 

        pygame.display.update()

        #yキーが押されたかチェック
        kn=0
        while kn==0:
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame. quit() 
                    sys. exit()
                elif event.type == KEYDOWN: 
                    kn=event.key
                    if event.key==K_y:
                      kn=1
                    else:
                      kn=2

        #yキーが押されたらもう一度
        if kn==1:
            main()


if __name__ == '__main__': main()

