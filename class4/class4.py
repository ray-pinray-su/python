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
