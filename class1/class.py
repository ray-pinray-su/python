# 這是一般的單行註解
print("Hello World!")  # 這是程式碼後的註解
"""
這

是一般的多行註解
"""
# 基本型態
print("Hello World!")  # 整數 integer, int
print(3.14)  # 浮點數 float, double
print(True)  # 布林值 boolean, bool
print("Hello World!")  # 字串 string, str


# 變數
# 變數是存放資料的記憶體空間,每個變數都要有自己的名稱
# 要存甚麼資料都可以
# 變數名稱命名規則:只能使用英文字,數字,底線,且不能以數字開頭
a = 10  # =的功能是將右邊的資料存到給左邊的變數
b = 20
c = a + b  # 把a和b的值相加後存到c

# 算術運算子
print(a + b)  # 加法
print(a - b)  # 減法
print(a * b)  # 乘法
print(a / b)  # 除法
print(a // b)  # 整除
print(a % b)  # 取餘數
print(a**b)  # 次方

# 運算子優先順序
# 1.括號()
# 2.次方**
# 3.+-(正負號)
# 4.*乘法 /除法 //整數除法 %取餘數
# 5.+-(加減)

# 字串運算
print("Hello" + "World!")  # 字串串接
print("Hello" * 3)  # 字串重複
# print("Hello"+3)  # 錯誤,字串不能加數字
# 除了字串乘法可以跟數字相乘
# 字串跟字串之間只能有加減不能有乘除
w = "Hello"
s = "World"
e = w + "" + s  # 字串串接
print(e)
