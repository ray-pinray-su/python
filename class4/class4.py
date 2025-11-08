d = int(input("請輸入成績:"))
if d > 89:
    print("A")
elif d > 79 and d < 90:
    print("B")
elif d > 69 and d < 80:
    print("C")
elif d > 59 and d < 70:
    print("D")
elif d < 10:
    print("你好笨")
else:
    print("E")

y = int(input("請輸入數字:"))
if y % 2 > 0:
    print("奇數")
else:
    print("偶數")

# 匯入模組
import turtle as t  # 匯入海龜模組並取別名為t

t.forward(100)  # 向前走100單位
t.right(90)  # 向右轉90度
t.forward(100)  # 向前走100單位
t.right(90)  # 向右轉90度
t.forward(100)  # 向前走100單位
t.right(90)  # 向右轉90度
t.forward(100)  # 向前走100單位
t.right(90)  # 向右轉90度
t.forward(100)  # 向前走50單位
t.right(90)  # 向右轉90度
t.forward(10000000000000000000000000000000000)  # 向前走100單位
t.done()  # 讓視窗保持開啟


# for example
# for的組成有三個部分
# for迴圈變數 in 範圍:
# 迴圈變數只能活在for迴圈內
# 迴圈變數每回合會取得範圍內的一個值
for i in range(5):  # range(5) 可以產生0~4的數字  range=0,1,2,3,4
    print(i)
for j in range(1, 6):  # range(1,6) 可以產生1~5的數字  range1,2,3,4,5
    print(j)
for k in range(1, 10, 2):  # range(1,10,2) 可以產生1~9的奇數    range=1,3,5,7,9
    print(k)
import turtle as t

for m in range(100):
    t.forward(10)
    t.right(10)
    t.color("red")  # 設定顏色
    t.shape("turtle")  # 設定圖案
    t.penup()  # 提起畫筆
    t.stamp()  # 印出圖案
t.done()
