def hello(name: str = "Singular") -> None:  # 函數傳入參數都是區域變數
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數:\n
    name:str-姓名

    回傳:None

    範例:hello("Ray")#Hello,Ray!
    """
    print(f"Hello,{name}!")


# 讀取指令說明
print(hello.__doc__)
print(hello.__name__)  # 顯示:add函式的名稱


# eval(input())-這個函式可以把輸入的字串當成程式碼來執行
# 例如:
ans = eval("5+3")
print(ans)  # 8

# 這樣就可以讓使用者輸入數學算式,然後計算結果
# 例如:
ans = eval(input("請輸入數學算式:"))
print("計算結果:", ans)
# 例如輸入:
# 5+3
# 顯示:8

# 檔案讀寫
# 判斷檔案是否存在 - 使用 os.path.isfile() 函式
import os

# 相對路徑代表相對於目前的工作目錄的路徑
# 絕對路徑代表完整的路徑
if os.path.isfile("class17/hw.py"):
    # C:\Users\User\Desktop\python_test\class17\hw.py
    print("檔案存在！")
else:
    print("檔案不存在！")

# open() 開啟模式
# r - 讀取模式、檔案必須存在
# w - 寫入模式、檔案不存在會自動建立
# a - 附加模式、檔案不存在會自動建立
# r+ - 讀取與寫入模式、檔案必須存在
# w+ - 讀取與寫入模式、檔案不存在會自動建立
# a+ - 讀取與附加模式、檔案不存在會自動建立

# 讀取檔案 - 使用 open() 函式
# 例如：
file = open("class18/file_test.py", "r")
print(file.read())
file.close()

# 讀取檔案 - 使用 with open() as
# 例如：
with open("class18/file_test.py", "r") as file:
    print(file.read())

# 寫入檔案 - 使用 open() 函式
# 例如：
file = open("class18/file_test.py", "w")
file.write("print('write file test')")
file.close()


# 寫入檔案 - 使用 with open() as
# 例如：
with open("class18/file_test.py", "w") as file:
    file.write("print('Hello World!')")
