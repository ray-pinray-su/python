
import random as r

x = r.randint(1, 100)
q = 0
while q != x:
    q = int(input("請輸入1~100的整數"))
    if q > x:
        print("再小一點")
        continue
    print("再大一點")
else:
    print("恭喜答對")