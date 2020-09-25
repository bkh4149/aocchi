import random
N = 100000 #試行回数

#一回の試行
def montyOneTime():
    treasure_door = random.randint(1,3)
    #print("司会：宝は",treasure_door)

    challengers_choice = random.randint(1,3)
    #print("ゲスト：最初の選択",challengers_choice)

    #司会の誘導
    left_door=[1,2,3]
    #当たりの場合
    if challengers_choice == treasure_door:
        left_door.remove(challengers_choice)
        mc_ans = random.choice(left_door)
    #ハズレの場合
    else:
        left_door.remove(treasure_door)
        left_door.remove(challengers_choice)
        mc_ans = left_door[0]
    #print("司会：ハズレの箱は",mc_ans)

    #Change or Not 変えるか否かはランダムで
    r = random.randint(1,2)
    if r==1: #変える
        left_door = [1,2,3]
        left_door.remove(mc_ans)
        left_door.remove(challengers_choice)
        last_answer = left_door[0]
        #print("ゲスト：変更します!")
        chg_flag = 1
    else: #変えない
        last_answer = challengers_choice
        #print("ゲスト：変えません")
        chg_flag = 0
    #print("最終回答は",last_answer)

    #当たり外れの判定
    if last_answer == treasure_door:
        #print("正解です")
        hit_flag = 1
    else:
        #print("残念でした")  
        hit_flag = 0
    return chg_flag, hit_flag    

#変えたときと変えないときの勝率の計算
change_counter = 0  # 変えたとき回数
change_hit_counter = 0  # 変えてヒットの回数
no_change_counter = 0  # 変えないときの回数
nochange_hit_counter = 0  # 変えないでヒットの回数
#N回繰り返す
for i in range(N):
    ch,ok = montyOneTime()
    if ch == 1:#変えたとき
        change_counter += 1
        if ok == 1:
            change_hit_counter += 1
    else:
        no_change_counter += 1
        if ok == 1:
            nochange_hit_counter += 1

print("変えたとき　（回数＝", change_counter, " ヒット数＝", change_hit_counter, " 勝率=", change_hit_counter/change_counter*100, "%）")
print("変えないとき（回数＝", no_change_counter, " ヒット数＝", nochange_hit_counter, " 勝率=", nochange_hit_counter/no_change_counter*100, "%）")
print("トータル　　（回数＝", no_change_counter + change_counter, " ヒット数＝", change_hit_counter + nochange_hit_counter, " 勝率=",(change_hit_counter + nochange_hit_counter)/( change_counter + no_change_counter)*100, "%）")