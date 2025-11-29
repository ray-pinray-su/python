# for...else 迴圈
# 當for迴圈正常結束時，會執行else區塊
# 如果迴圈中有break語句，else區塊不會執行
# example:
for i in range(5):
    print(i)
else:
    print("for迴圈正常結束")

# while...else 迴圈
# 當while迴圈正常結束時，會執行else區塊
# 如果迴圈中有break語句，else區塊不會執行
# example:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while迴圈正常結束")

# else在Python中的三種用法
# 1.if...elif...else 當前面的條件都不成立時，會執行else區塊
# 2.try...except...else 當try區塊正常執行時，會執行else區塊
# 3.for...else 和 while...else 當迴圈正常結束時，會執行else區塊

# 倒數計時器
# 這個程式會根據使用者輸入的秒數進行倒數計時
import time

倒數秒數 = int(input("請輸入倒數秒數: "))  # 取得使用者輸入的秒數
while 倒數秒數 > 0:
    print(f"倒數計時: {倒數秒數} 秒")  # 列印目前倒數秒數
    time.sleep(1)  # 暫停1秒
    倒數秒數 -= 1  # 秒數減1
else:
    print("時間到！")  # 倒數結束時列印訊息


# 迴圈的break只會跳出內層的for迴圈
# 所以判斷break屬於哪個迴圈時,必須注意縮排
# 例如:
for i in range(5):  # 外層迴圈
    for j in range(5):  # 內層迴圈
        if i == 2 and j == 2:
            break  # 跳出內層迴圈
        print(f"i={i}, j={j}")  # 列印i和j的值
# 這裡的break只會跳出內層的for 迴圈
# 外層的for迴圈還是會繼續執行


# continue
# 迴圈的continue可以用來跳過當前的迴圈，直接進入下一次迴圈
# 例如:
for i in range(5):
    if i == 2:
        continue  # 如果i是偶數，跳過本次迴圈
    print(i)  # 列印奇數
# 這裡的continue會跳過i等於2的情況，直接進入i等於3迴圈
# 所以輸出的結果是0,1,3,4
# continue也可以用在while迴圈中
# 例如:
i = 0
while i < 5:
    if i == 2:
        continue  # 如果i是2，跳過本次迴圈
    print(i)  # 列印i的值
    i += 1  # 每次迴圈加1
# continue也要判斷所屬的迴圈,要注意縮排
