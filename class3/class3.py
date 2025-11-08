# try except 錯誤處理
# 當程式執行的過程中，如果有錯誤發生，就可不用停止程式的執行，而是去執行except的動作
# 可用冒號, 縮排符號, 來區分裡面和外面的內容
try:
    a = int(input("請輸入一個整數:"))  # 裝在try內的程式
except:
    print("請輸入整數!")  # 裝在except內的程式

# except 可以指定錯誤的類型,例如ValueError代表數值錯誤
# 所以except 可以指定多個類,可根據不同的錯誤類型執行不同的程式
try:
    a = int(input("請輸入一個整數:"))
except ValueError:
    print("請輸入整數!")
except ZeroDivisionError:
    print("請輸入正整數!")
except:
    print("發生了一個未知的錯誤!")

else:  # (可選)
    print("沒有錯誤!")
finally:  # (可選)
    print("最後的動作!")

# 比較運算子
print(5 == 5)  # True,5等於5
print(5 != 3)  # True,5不等於3
print(5 > 3)  # True,5小於3
print(5 < 3)  # False,5不大於3
print(5 >= 3)  # True,5大於等於3
print(5 <= 3)  # False,5不小於等於3

# 邏輯運算子
# and代表只要有一個是False就會回傳False
print(True and True)  # True,兩個都是True
print(True and False)  # False,兩個都是False

# or代表只要有一個是True就會回傳True
print(True or True)  # True,兩個都是True
print(True or False)  # True,兩個都是False

# not代表將布林值取反
print(not True)  # False,True不是False
print(not False)  # True,False不是True

# 運算子優先順序
# 1.括號()
# 2.次方**
# 3.+-(正負號)
# 4.*乘法 /除法 //整數除法 %取餘數
# 5.+-(加減)
# 6.not非
# 7.and且
# 8.or或


# if條件判斷
# if後面是條件,如果條件為True就執行縮排裡面的程式
# 可以有多個if,代表其他條件,也可以沒有if
# 最後可以有一個else,代表其他條件都沒有滿足時執行
pwd = input("請輸入密碼:")
if pwd == "123456":
    print("歡迎使用123456")
elif pwd == "12345678":
    print("歡迎使用12345678")
elif pwd == "123456789":
    print("歡迎使用123456789")
else:
    print("滾!")

# if elif else使用時機
# 在有多個有關連的條件需要判斷時,最後只會執行一個
# 多個if使用的時機在每個條件是獨立運作,可能會執行多個區塊
