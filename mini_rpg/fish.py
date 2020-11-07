import random
class Fish():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.hp = random.randint(15,50)
        self.at = random.randint(11,20)
        self.aj = random.randint(1,10)
        self.att = random.randint(1,10)
        self.df = random.randint(1,10)

    def up(self, map):
        r = random.randint(1,6)
        if r<=3:
            rx = r-2
            ry = 0
        else:
            rx = 0
            ry = r-5
        #位置を更新
        oldx = self.x
        oldy = self.y
        self.x += rx
        self.y += ry
        #枠外なら位置を戻す
        if self.x <0 or self.x > 9 or self.y < 0 or self.y > 10:
            self.x = oldx
            self.y = oldy
            return
        #海以外なら戻す
        if map.mp[self.y][self.x] != "～":
            self.x = oldx
            self.y = oldy
