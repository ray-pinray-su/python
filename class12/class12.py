# 新增/修改字典
# 直接指定key對應的 value,如果key已存在就是修改,如果key不存在就是新增
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10
print(d)
d["蓮霧"] = 15
print(d)


# 刪除字典內容
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")  # 刪除蘋果
# 如果要刪掉不存在的key,會KeyError,所以加入第二參數,當key不存在時,不會有變化
popitem = d.pop("蓮霧", "資料不存在")  # 不會有變化
print(d)  # {'香蕉': 30, '橘子': 25}
print(popitem)  # 資料不存在

# len:取得字典中有多少個key-value配對
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))  # 3

# 檢查某個key是否存在於字典中
# 使用先前檢查可以避免KeyError
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("蘋果" in d)  # True
print("蓮霧" in d)  # False


# 檢查某元素是否在list中
# 使用in可以快速檢查某元素有沒有在list當中
l = [1, 2, 3, 4, 5]
print(3 in l)  # True
print(10 in l)  # False
