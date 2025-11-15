x = input("請輸入你的數字:")
x = int(x)
for i in range(1, x + 1):
    if i % 3 == 0 or i % 7 == 0:
        print(i)
