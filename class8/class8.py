import random as r  # 匯入隨機模組，取別名為r

# random.randrange 的設定範圍方式跟range一樣
# randrange 的功能是隨機取得一個數，range 是產生一組數字
print(r.randrange(10))  # 隨機取得0~9的其中一個數
print(r.randrange(1, 10))  # 隨機取得1~9的其中一個數
print(r.randrange(1, 10, 2))  # 隨機取得(1,3,5,7,9)的其中一個數

# random.randint 的設定範圍方式包含開始和結束
# randint 不能跳數字，會取得連續範圍內的隨機數
print(r.randint(1, 10))  # 隨機取得1~10的其中一個數

# 猜數字遊戲
import random as r

x = r.randint(1, 100)  # 隨機產生1~100的數字
q = 0  # 使用者輸入的數字
while True:
    q = int(input("請輸入1~100的整數"))
    if q == x:
        break
    if q > x:
        print("再小一點")
        continue  # 跳過本次迴圈，執行下一次
    print("再大一點")
print("恭喜答對")
# List清單(List)
# List可以存入很多資料，每筆資料用逗號隔開
# List可以存入不同型態的資料
# List最外層用方括號[]包起來
L = [1, 2, 3, 4, 5]  # 存放數字的List
print(L)
# 不同型態混合的List
l = [1, 2, 3, 4, 5, "hello", ["f", 2]]


# List取值
# List取值方式和字串一樣，用[]取值
# List當中資料的編號(index)都從0開始
l = [1, 2, 3, 4, 5]
print(l[0])  # 取得第1個值
print(l[2])  # 取得第3個值
print(l[1])  # 取得第2個值

# List取值的方式也可以用[:] 取一段範圍
# 設定範圍的方式跟range很像，不包含最後一個數
print(l[1:4:2])  # 取得索引1到3，間隔2的值
print(l[0:3])  # 取得索引0到2的值
print(l[:3])  # 取得從開始到索引2的值
print(l[3:])  # 取得從索引3到最後的值
print(l[:])  # 取得所有值


# List長度 len()
# len() 函式可以取得List的長度，也就是List當中有幾筆資料
l = [1, 2, 3, 4, 5]
print(len(l))  # 取得List長度

# 重要：不要跟index混淆，index是資料編號，len是資料數量

# len可以搭配for迴圈使用來取得List當中的所有資料
for i in range(len(l)):  # 這邊的i是index，用來逐一存取每個元素
    print(l[i])

for i in l:  # 這邊的i是資料本身
    print(i)
# 兩種方式都可以使用，看需求選擇


# 飲料販賣機(改進版)
juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    for index in range(len(juice_list)):
        print(f"{index + 1}. {juice_list[index]}")  # 列印飲料編號和名稱
    choice = int(input("請輸入編號:"))  # 取得使用者選擇
    if choice < 1 or choice > len(juice_list):  # 檢查輸入是否有效
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    if choice == len(juice_list):  # 如果選擇關閉選項
        print("~~系統關閉~~")
        break  # 跳出迴圈
    print(f"您點的商品是{juice_list[choice - 1]}")  # 列印使用者選擇的飲料
