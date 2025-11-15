# 箭頭繪圖
x = int(input("請輸入箭頭size:"))
for i in range(x + 1):
    q = "*" * (i * 2 - 1)
    z = " " * (x - i)
    print(z + q)
for t in range(x):
    print(" " * (x - 1) + "*")
