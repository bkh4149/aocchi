
class Creature():
    def __init__(self):
        self.x=0#フィールドでの座標
        self.y=0
        self.tx=0#街ナカ用の座標
        self.ty=0
        self.hp = 0#特性
        self.at = 0#攻撃力
        self.aj = 0#速度
        self.mp = 0#魔法力
        self.df = 0#防御力
        self.df_rate = 1#防御力アップ分
        self.buki = ""
        self.buki_rate = 1#攻撃力アップ分
        self.level = 0#レベル
        self.level_rate = [1, 1.2, 1.5, 2, 3, 5 ]#レベルによる能力アップ分
        self.items = []#持ち物
        self.money = 0#お金
        self.name = ""
        self.kind = "human"

    def status(self):
        print ("name=",self.name)
        print ("money=",self.money)
        for n,l in enumerate( self.items):
            print(n+1, l["name"], "  価格", l["price"],  "  強さ", l["add"],"   重さ" ,l["weight"] )
