x = input("輸入開始整數")
l = 0
y = input("輸入結束整數")
for i in range(int(x), int(y) + 1):
    for k in range(1, i + 1):
        if i % k == 0:
            l += 1
    if l == 2:
        print(i)
    l = 0
