
wheather = ["晴天", "多雲", "雨天", "晴天", "雷陣雨", "晴天"]
while True:
    day = input("請輸入要修改星期幾(1-7):")
    try:
        day = int(day)
    except:
        print("請輸入數字")
        continue
    if day > 7 or day < 1:
        print("請輸入1-7的數字")
        continue
    wheather2 = input("請輸入新的天氣狀況:")
    wheather[day - 1] = wheather2
    print(wheather[:6])