# List 更新資料
# 用起來跟一般的變數很像，直接用賦值運算子 = 來更新
# 要注意的是必須指定 index(編號)位置來更新特定元素
l = ["apple", "banana", "cherry"]
l[1] = "orange"  # 把 index 1 的資料更新成 orange


# 天氣預報修改器
# 這個程式會讓使用者修改指定星期的天氣狀況
wheather = ["晴天", "多雲", "雨天", "晴天", "雷陣雨", "晴天", "陰天"]
while True:
    try:
        day = int(input("請輸入要修改星期幾(1-7):"))  # 取得使用者輸入的星期數
    except:
        print("請輸入數字")  # 輸入不是數字時提示
        continue
    if day > 7 or day < 1:
        print("請輸入1-7的數字")  # 檢查輸入範圍
        continue
    wheather2 = input("請輸入新的天氣狀況:")  # 取得新的天氣狀況
    wheather[day - 1] = (
        wheather2  # 將新天氣存入 List 對應位置（day-1 因為 index 從 0 開始）
    )
    print(wheather[:6])  # 列印修改後的天氣預報
    break  # 跳出迴圈


# call by value
# 在一般情況下,存資料到變數當中是採用call by value的方式
a = 1
b = a
b = 22
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置,所以改b會影響a
b[0] = 22
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的質給b,但是a跟b指向不同的記憶體位置
b[0] = 22
print(a, b)
