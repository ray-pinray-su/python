g = {"蘋果": 25, "香蕉": 30, "橘子": 40}
l = ["新增水果價格", "修改價格", "刪除", "離開"]
while True:
    print("目前價格:")
    for k, v in g.items():
        print(f"{k}:{v}")
    for i, f in enumerate(l):
        print(f"{i+1}.{f}")
    t = int(input("請選1-4:"))
    c = t - 1
    if c == 0:
        n = input("請輸入水果名稱:")
        p = int(input("請輸入價格:"))
        g[n] = p
    elif c == 1:
        n = input("請輸入要修改的水果名稱:")
        if n not in g:
            print("沒有這筆資料可以修改")
            continue
        p = int(input("請輸入新的價格:"))
        g[n] = p
    elif c == 2:
        n = input("請輸入要刪除的水果名稱:")
        if n not in g:
            print("沒有這筆資料可以刪除")
            continue
        g.pop(n)
    elif c == 3:
        print("離開程式")
        break
print("=" * 100)
