# 字串格式化式化f+string
age = 12
name = "Ray"
print(f"My name is {name} and I am {age} years old.")

"""
只要在字串前加上 f 就能在字串中直接使用大括號{ }
把想帶入的變數或運算式或任何資料
都放在大括號中就可以成為新的字串
"""
# 函數是由名稱和參數(提供的材料)組成,每一個參數都要用逗號隔開
# Max( ) 函式會回傳參數中最大的值
print(max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))

# len( ) 函式會回傳參數(字串)的長度
print(len("Hello World!"))

# type( ) 函式會回傳參數的資料型態
print(type("Hello World!"))
print(type(12))
print(type(True))
print(type(123.435))

# int( ) 函式可以將字串轉換成整數型態
print(int(123))
print(int(123.354))
print(int("true"))
print(int("false"))

# float( ) 函式可以將字串轉換成浮點數型態
print(float(123))
print(float(123.854))
print(float("true"))
print(float("false"))

# bool( ) 函式可以將字串轉換成布林值型態
print(bool(""))
print(bool("true"))
print(bool("false"))
print(bool(123))
print(bool(123.454))
print(bool("hello"))

# str( ) 函式可以將字串轉換成字串型態
print(str(123))
print(str(123.454))

print(str("hello"))

# input( ) 函式可以讓使用者在執行程式時輸入資料
name = input("請輸入你的名字:")  # 提示的文字會顯示在螢幕上，不會被存起來
print(type(name))  # input( ) 函式回傳的資料型態是字串
print(f"你好{name}!")
print("你好" + name + "!")
# age = input("請輸入你的年齡:")
# age = int(age)#把輸入的年齡轉換成整數
age = int(input("請輸入你的年齡:"))  # 直接把 input( ) 函式的回傳值給 int( ) 函式
print(f"你明年就是{age+1}歲了!")

# 圓形面積
面積 = 3.14 * float(input("請輸入你的圓形半徑:")) ** 2
print(f"圓形面積是{面積}")

# 正方形面積
面積 = float(input("請輸入你的正方形邊長:")) ** 2
print(f"正方形面積是{面積}")

# 矩形面積
面積 = float(input("請輸入你的矩形邊長:")) * float(input("請輸入你的矩形高度:"))
print(f"矩形面積是{面積}")
