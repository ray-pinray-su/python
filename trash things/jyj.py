import turtle as t

t.speed(10)
t.pensize(3)


# 函式：畫填滿圓
def filled_circle(color, r):
    t.color("black", color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


# 頭
t.penup()
t.goto(0, -20)
t.pendown()
filled_circle("yellow", 80)

# 左耳
t.penup()
t.goto(-50, 110)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(120)
t.forward(100)
t.setheading(-40)
t.forward(50)
t.setheading(-150)
t.forward(70)
t.end_fill()

# 左耳黑尖
t.penup()
t.goto(-50, 110)
t.setheading(120)
t.forward(60)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.setheading(120)
t.forward(40)
t.setheading(-40)
t.forward(20)
t.setheading(-150)
t.forward(30)
t.end_fill()

# 右耳
t.penup()
t.goto(50, 110)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(60)
t.forward(100)
t.setheading(220)
t.forward(50)
t.setheading(30)
t.forward(70)
t.end_fill()

# 右耳黑尖
t.penup()
t.goto(50, 110)
t.setheading(60)
t.forward(60)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.setheading(60)
t.forward(40)
t.setheading(220)
t.forward(20)
t.setheading(30)
t.forward(30)
t.end_fill()

# 眼睛
t.penup()
t.goto(-30, 40)
t.pendown()
filled_circle("black", 10)

t.penup()
t.goto(30, 40)
t.pendown()
filled_circle("black", 10)

# 臉頰
t.penup()
t.goto(-55, 0)
t.pendown()
filled_circle("red", 18)

t.penup()
t.goto(55, 0)
t.pendown()
filled_circle("red", 18)

# 嘴巴
t.penup()
t.goto(-15, -20)
t.pendown()
t.color("black")
t.setheading(-60)
t.circle(25, 120)
# 身體
t.penup()
t.goto(0, -80)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(-90)
t.forward(120)
t.setheading(180)
t.circle(40, 180)
t.setheading(90)
t.forward(120)
t.end_fill()

# 左手
t.penup()
t.goto(-80, -40)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(-160)
t.circle(40, 120)
t.end_fill()

# 右手
t.penup()
t.goto(80, -40)
t.pendown()
t.begin_fill()
t.setheading(-20)
t.circle(-40, 120)
t.end_fill()

# 左腳
t.penup()
t.goto(-40, -200)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(25)
t.end_fill()

# 右腳
t.penup()
t.goto(40, -200)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# 尾巴（閃電形）
t.penup()
t.goto(70, -110)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.setheading(0)
t.forward(60)
t.setheading(90)
t.forward(40)
t.setheading(-20)
t.forward(70)
t.setheading(-160)
t.forward(70)
t.setheading(90)
t.forward(40)
t.end_fill()

t.hideturtle()
t.done()
