juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    for index in range(len(juice_list)):
        print(f"{index + 1}. {juice_list[index]}")  # 列印飲料編號和名稱
    choice = int(input("請輸入編號:"))  # 取得使用者選擇
    if choice < 1 or choice > len(juice_list):  # 檢查輸入是否有效
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    if choice == len(juice_list):  # 如果選擇關閉選項
        print("~~系統關閉~~")
        break  # 跳出迴圈
    print(f"您點的商品是{juice_list[choice - 1]}")  # 列印使用者選擇的飲料