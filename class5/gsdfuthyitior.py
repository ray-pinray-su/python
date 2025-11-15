import turtle as t

t.speed(0)
t.forward(-500)
t.left(90)
t.forward(300)
t.right(90)
for i in range(1000):
    t.forward(1000)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(1000)
    t.left(90)
    t.forward(1)
    t.left(90)
t.done()  # 讓視窗保持開啟
