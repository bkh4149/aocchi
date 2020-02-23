bx=100
by=100
bw=130
bh=130


mx=1200
my=200
mw=50
mh=50




#左上
if ((bx < mx < bx+bw) and (by < my <by+bw)) or ((bx < mx+mw < bx+bw) and (by < my <by+bw)) or ((bx < mx < bx+bw) and (by < my+mh <by+bw)) or ((bx < mx+mw < bx+bw) and (by < my+mh <by+bw)) :
    print("hit")
else:
    print("err")
    


