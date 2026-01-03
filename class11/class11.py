# index:尋找指定元素在List中第一次齣戲的位置
# 如果元素不存在會產生錯誤,所以使用前建議先檢查它是否存在
l = [10, 20, 30, 40, 50]
print(l.index(30))  # 找到數字30在索引位置2

# count:統計某個元素在list中共出現幾次
# 這個方法很適合用來檢查重複元素的數量
l = ["hello", "world", "hello", "python"]
print(l.count("hello"))  # hello出現了2次

# sort:將list中的元素進行排序,預設是由小到大排序
# 注意:這個方法會直接修改原本的list,不會有新的
l = [50, 20, 40, 10, 30]
l.sort()
print(l)

# sort(reverse=True):將list中的元素進行反向排序,由大到小
l = [50, 20, 40, 10, 30]
l.sort(reverse=True)
print(l)

# reverse:將list中的元素順序反轉
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)


# list和字串有很多相似的操作方式
# 我們可以像操作字串一樣來處理list

# 合併兩個list:使用+運算子將兩個list連接在一起
# 這會產生一個全新的list,原本的list不會改變
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2  # 把l1和l2合併成新的list
print(l3)

# 重複list中的內容:使用*運算子將list內容重複多次
# 這在需要建立重複資料時很有用
l = [1, 2, 3]
l = l * 3  # 將list內容重複3次
print(l)


# 不同資料型態之間的轉換技巧
print(range(10))  # range物件本身看不到具體內容,只是一個範圍描述
print(list(range(10)))  # 使用list將range物件轉換成list,可以看到具體內容
print(list("hello"))  # 將字串轉換成list,每個字元成為獨立的一個元素

# split:將一個完整的字串按照指定的分隔符拆分成多個部分,並存入list中
s = "apple,banana,orange"
fruits = s.split(",")  # 以逗號作為分隔符進行拆分
print(fruits)

# join:將List中的多個字串元素合併成一個完整的字串
# 可以指定要用甚麼符號來連接這些元素
l = ["hello", "world", "python"]
s = " ".join(l)  # 使用空格將list中的字串元素連接起來
print(s)


l = "2023/10/20"
l = l.split("/")
l = "-".join(l)
print(l)


# 字典(Dictionary):用來儲存[key-value]配對的資料結構
# 字典很適合用來表示有對應關係的資料,像是商品價格的對應
# 建立字典:使用大括號{},key 和value之間用冒號:分隔
d = {"apple": 150, "banana": 100, "cherry": 200}
print(d)


# 從字典中取得特定key 對應的value
# 如果 key不存在會產生KeyError錯誤
d = {"apple": 20, "banana": 30, "orange": 25}
print(d["apple"])
# print(d["pear"])#這行會產生KeyError:"pear"錯誤

# 遍歷字典:有很多方式可以走字典中的資料
d = {"apple": 20, "banana": 30, "orange": 25}

# (1):直接遍歷字典,會取得所有Key
for k in d:
    print(k)  # 印出key名稱
    print(d[k])  # 用key來取得對應的value

# (2):明確使用keys()方法取得所有key
for k in d.keys():
    print(k)  # 印出key名稱
    print(d[k])  # 用key來取得對應的value

# (3):使用values()方法來取得所有value
for v in d.values():
    print(v)  # 直接印出value,但不知道對應的key是甚麼

# (4):使用items()方式同時取得key和value
# 這是最常用的方式,因為可以同時取得key和value
for k, v in d.items():
    print(f"{k}:{v}")  # 同時印出key和value的配對關係
