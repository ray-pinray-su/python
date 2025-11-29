x = input("輸入開始整數")
y = input("輸入開始整數")
for i in range(1, x + 1):
    if x % i == 0:
        y += 1
if y == 2:
    print("質數")
else:
    print("不是質數")
