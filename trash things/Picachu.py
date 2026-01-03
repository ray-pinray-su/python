import turtle as t
import random as r

t.tracer(0)
for i in range(100000):
    a = r.randrange(361)
    t.right(a)
    t.forward(r.randrange(5, 30))
t.update()
t.done()

import turtle as t

t.speed(10)
t.pensize(3)
t.color("black", "yellow")

# 頭
t.begin_fill()
t.circle(100)
t.end_fill()

# 左耳
t.penup()
t.goto(-60, 120)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(120)
t.forward(120)
t.setheading(-60)
t.forward(60)
t.setheading(-150)
t.forward(70)
t.end_fill()

# 左耳黑尖
t.penup()
t.goto(-60, 120)
t.setheading(120)
t.forward(80)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.setheading(120)
t.forward(40)
t.setheading(-60)
t.forward(20)
t.setheading(-150)
t.forward(30)
t.end_fill()

# 右耳
t.penup()
t.goto(60, 120)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(60)
t.forward(120)
t.setheading(-120)
t.forward(60)
t.setheading(30)
t.forward(70)
t.end_fill()

# 右耳黑尖
t.penup()
t.goto(60, 120)
t.setheading(60)
t.forward(80)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.setheading(60)
t.forward(40)
t.setheading(-120)
t.forward(20)
t.setheading(30)
t.forward(30)
t.end_fill()

# 左眼
t.penup()
t.goto(-40, 40)
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

# 右眼
t.penup()
t.goto(40, 40)
t.begin_fill()
t.circle(10)
t.end_fill()

# 臉頰
t.color("red", "red")
t.penup()
t.goto(-70, -10)
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(70, -10)
t.begin_fill()
t.circle(20)
t.end_fill()

# 嘴巴
t.penup()
t.goto(-20, -30)
t.pendown()
t.color("black")
t.setheading(-60)
t.circle(30, 120)

t.hideturtle()
t.done()

pikachu = r"""
 (\__/)
 (•ㅅ•)
 / 　 づ  ⚡
"""
print(pikachu)


import turtle as t

t.speed(10)
t.pensize(3)
t.color("black", "yellow")

# 頭
t.begin_fill()
t.circle(100)
t.end_fill()

# 左耳
t.penup()
t.goto(-60, 120)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(120)
t.forward(120)
t.setheading(-60)
t.forward(60)
t.setheading(-150)
t.forward(70)
t.end_fill()

# 左耳黑尖
t.penup()
t.goto(-60, 120)
t.setheading(120)
t.forward(80)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.setheading(120)
t.forward(40)
t.setheading(-60)
t.forward(20)
t.setheading(-150)
t.forward(30)
t.end_fill()

# 右耳
t.penup()
t.goto(60, 120)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(60)
t.forward(120)
t.setheading(-120)
t.forward(60)
t.setheading(30)
t.forward(70)
t.end_fill()

# 右耳黑尖
t.penup()
t.goto(60, 120)
t.setheading(60)
t.forward(80)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.setheading(60)
t.forward(40)
t.setheading(-120)
t.forward(20)
t.setheading(30)
t.forward(30)
t.end_fill()


# 左眼
t.penup()
t.goto(-40, 140)
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

# 右眼
t.penup()
t.goto(40, 140)
t.begin_fill()
t.circle(10)
t.end_fill()

# 臉頰
t.color("red", "red")
t.penup()
t.goto(-70, 90)
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(70, 90)
t.begin_fill()
t.circle(20)
t.end_fill()

# 嘴巴
t.penup()
t.goto(-20, 70)
t.pendown()
t.color("black")
t.setheading(-60)
t.circle(30, 120)

t.hideturtle()
t.done()
