import random as r  # 這是隨機模組

# random.randrange 設定範圍的方式跟range一樣
# random.randrange的功能是隨機取得一個數,range是產生一組數字
print(r.randrange(10))  # 隨機取得0~9的其中一個數
print(r.randrange(1, 10))  # 隨機取得1~9的其中一個數
print(r.randrange(1, 10, 2))  # 隨機取得(1,3,5,9)的其中一個數

# random.randint 設定範圍的方式是包含開始跟結束
# 不能跳數字
print(r.randint(1, 10))  # 隨機取得0~10的其中一個數

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
