import turtle as t

t.penup()
t.speed(0)
t.forward(-700)
t.left(90)
t.forward(350)
t.right(90)
t.pendown()
for i in range(400):
    t.forward(2000)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(2000)
    t.left(90)
    t.forward(1)
    t.left(90)
t.done()  # 讓視窗保持開啟
