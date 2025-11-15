import turtle as t

t.tracer(False)  # 關閉自動更新畫面

t.penup()
t.shape("circle")
for i in range(100):
    t.forward(i + 10)
    t.right(24)
    t.stamp()
t.update()  # 因為關閉動畫,手動更新畫面
t.done()  # 讓視窗保持開啟


# 五角形星星
import turtle

turtle.pensize(5)  # 設定畫筆粗細=5
turtle.pencolor("yellow")  # 設定畫筆顏色=黃色
turtle.fillcolor("yellow")  # 設定填充顏色=黃色
turtle.begin_fill()  # 開始填充

for i in range(5):
    turtle.forward(200)  # 向前走200單位
    turtle.right(144)  # 向右轉144度

turtle.end_fill()  # 結束填充
turtle.done()  # 讓視窗保持開啟


turtle.clear()  # 清除畫面


x = input("請輸入你的數字:")
x = int(x)
print(int((x + 1) * x / 2))
