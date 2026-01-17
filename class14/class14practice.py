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

    def add():
        n = input("請輸入水果名稱:")
        p = int(input("請輸入價格:"))
        g[n] = p

    def edit():
        n = input("請輸入要修改的水果名稱:")
        if n in g:
            p = int(input("請輸入新的價格:"))
            g[n] = p
        else:
            print("沒有這水果")

    def delete():
        n = input("請輸入要刪除的水果名稱:")
        if n in g:
            g.pop(n)
        else:
            print("沒這水果")

    if c == 0:
        add()
    elif c == 1:
        edit()
    elif c == 2:
        delete()

    elif c == 3:
        print("離開程式")
        break
print("=" * 100)


水果 = {"蘋果": 25, "香蕉": 20, "橘子": 30}


def edit():
    """修改水果價格"""
    新水果 = input("請輸入你要新增的水果名稱:")
    新價格 = input(f"請輸入{新水果}的價格")
    水果[新水果] = 新價格
    print(新水果, "以新增，價格", 新價格)


def add():
    """新增水果價格"""
    新水果 = input("請輸入你要修改的水果名稱:")
    新價格 = input(f"請輸入{新水果}的新價格")
    水果[新水果] = 新價格
    print(新水果, "以修改為", 新價格, "元")


def delete():
    """刪除水果"""
    新水果 = input("請輸入你要刪除的水果名稱:")
    del 水果[新水果]
    print(新水果, "以刪除")


功能清單 = [add, edit, delete]

while True:
    print("目前水果價格")
    for key in 水果:
        print(key, ":", 水果[key], "元")
    for i, 功能 in enumerate(功能清單, start=1):
        print(f"{i}. {功能.__doc__}")
    print(f"{len(功能清單)+1}. 離開系統")

    選擇 = int(input(f"請選擇功能(1~4): "))
    if 選擇 == (len(功能清單) + 1):
        print("感謝使用水果店價格查詢系統")
        break
    else:
        功能清單[選擇 - 1]()
    print("=" * 26)
