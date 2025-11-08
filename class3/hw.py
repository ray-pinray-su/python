# 攝氏轉華氏
c = float(input("請輸入你的攝氏:"))
h = c * 9 / 5 + 32
print(f"你的華氏是{h}")


# 華氏轉攝氏
try:
    c = float(input("請輸入華氏溫度:"))
    h = (c - 32) * 5 / 9
    print(f"華氏溫度{c}等於攝氏{h}")
except:
    print("輸入錯誤!")
