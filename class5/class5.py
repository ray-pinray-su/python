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
