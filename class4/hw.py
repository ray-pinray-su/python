# BMI
m = float(input("請輸入你的體重(公斤):"))
h = float(input("請輸入你的身高(公尺):"))
bmi = m / (h**2)
print(f"你的BMI為{bmi}")
if bmi < 14.8:
    print("體重過輕")
if bmi > 20.7:
    print("體重過重")
if 14.8 <= bmi <= 20.7:
    print("體重正常")

# 海龜繪圖,螺旋狀

import turtle as t

t.penup()
t.shape("circle")
for i in range(100):
    t.forward(i * 2)
    t.right(100 - i * 2)
    t.stamp()
t.done()
