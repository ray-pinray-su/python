# 華氏轉攝氏
try:
    c = float(input("請輸入華氏溫度:"))
    if c == int(c):
        c = int(c)
    h = (c - 32) * 5 / 9
    if h == int(h):
        h = int(h)
    print(f"華氏溫度{c}等於攝氏溫度{h}")
except:
    print("輸入錯誤!")
