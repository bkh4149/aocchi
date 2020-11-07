import random
class Monster():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.hp = random.randint(15,50)
        self.at = random.randint(11,20)
        self.aj = random.randint(1,10)
        self.att = random.randint(1,10)
        self.mp = 0
        self.df = random.randint(1,10)
        self.gems = ["光の剣","氷結の剣","海割の剣","山割の剣","真贋の書","超薬草","得体のしれない鍵","人魚の涙"]
        self.r1 = random.randint(0,len(self.gems)-1)
        self.gem = self.gems[self.r1]
    def up(self, map):
        r = random.randint(1,6)
        if r<=3:
            rx = r-2
            ry = 0
        else:
            rx = 0
            ry = r-5
        oldx = self.x
        oldy = self.y
        self.x += rx
        self.y += ry
        if map.mp[self.y][self.x]=="～" or map.mp[self.y][self.x]=="山" or map.mp[self.y][self.x]=="　":
            self.x = oldx
            self.y = oldy
        #print("@100 self.x=",self.x, " self.y=",self.y)