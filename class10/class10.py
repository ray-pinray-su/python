# append 可以再以存在的List當中加入新的資料
# 可以在程式執行的過程中,隨時存入資料進List的"最後面"
l = ["apple", "banana", "cherry"]
l.append("orange")  # 在List的最後面加入orange
print(l)  # 列印更新後的List


# insert 在程式執行的過程當中可以將資料加入到List的指定位置
# 記得List的index是從0開始
# 如果新增的位置超過List的長度,就會直接加入到最後面
# 如果新增的位置是負數,就會從List的最後面開始算起,例如-1是最後一個位置
l = ["apple", "banana", "cherry"]
l.insert(1, "orange")  # 在index 1的位置加入orange
print(l)  # ['apple', 'orange', 'banana', 'cherry']
l.insert(-1, "grape")  # 在倒數第1個位置加入grape
print(l)  # ['apple', 'orange', 'banana', 'grape', 'cherry']
l.insert(-100, "watermelon")  # 位置超過List長度,直接加入到最前面
print(l)  # ['watermelon', 'apple', 'orange', 'banana', 'grape', 'cherry']


# remove:移除List當中的指定元素
# 電腦會從左到右尋找,找到第一個符合的元素就移除
l = ["apple", "banana", "cherry", "banana"]
l.remove("banana")  # 移除第一個出現的banana
print(l)  # ['apple', 'cherry', 'banana']


# pop:移除並回傳List中的元素
L = ["hello", "world", "python"]
# 不給索引時,預設移除並回傳最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # ['hello', 'world']
s = L.pop(1)  # 如果用變數存,可以取得被移除的元素
print(s)  # world
print(L)  # ['hello']
# 如果輸入的索引超過List長度,會發生錯誤
# 負數索引也可以使用
L = ["hello", "world", "python"]
L.pop(-2)  # 移除倒數第二個元素
print(L)  # ['hello', 'python']
# 負數索引超過List長度也會發生錯誤


l = []
d = ["1.新增", "2.刪除", "3.修改", "4.離開"]
while True:
    print(l)
    for i in d:

        print(i)
    x = input("請輸入指令:")
    if x == "1":

        n = input("請輸入新增的資料:")
        z = input("請問要放在最後面(a)還是指定位置(b)?(輸入a或b):")
        if z == "b":
            pos = int(input("請輸入位置(從0開始):"))
            l.insert(pos, n)
        else:
            l.append(n)
    elif x == "2":

        g = input("請問要刪除第一筆(a)還是指定(b)?(輸入a或b):")
        if g == "b":
            pos = int(input("請輸入位置(從0開始):"))
            if pos >= 0 and pos < len(l):
                l.pop(pos)
            else:
                print("位置不正確")
        if g == "a":
            if n in l:
                l.remove(l[0])
        else:
            print("沒有這筆資料")
    elif x == "3":
        e = input("請問要修改第一筆(a)還是指定(b)?(輸入a或b):")
        if e == "a":
            l[0] = input("請輸入新的資料:")
        if e == "b":
            n = input("請輸入要修改的資料:")
            if n not in l:
                print("沒有這筆資料可以修改")
                continue
            else:
                m = input("請輸入新的資料:")
                index = l.index(n)
                l[index] = m

    elif x == "4":
        print("離開程式")
        break


# enumerate:同時取得List的index跟內容
# 使用enumerate可以在迴圈中同時取得List的index跟內容
l = ["apple", "banana", "cherry"]
for index, value in enumerate(l):
    print(index, value)
    # 0 apple
    # 1 banana
    # 2 cherry


# `in`可以用在很多地方,像是if條件判斷
# 判斷某個元素是否在List當中
l = ["apple", "banana", "cherry"]
if "banana" in l:
    print("有香蕉")
else:
    print("沒有香蕉")

# in在for迴圈中代表迴圈變數會依序取得右邊範圍中的每一個元素
l = ["apple", "banana", "cherry"]
for fruit in l:
    print("我喜歡吃", fruit)

# in還可以用在字串中,檢查某個字串是否在字串中
s = "hello world"
if "world" in s:
    print("有world這個字串")
