# --- 練習題一：判斷營業時間與狀態 ---
"""
使用 if-elif-else 結構判斷多重狀態，模擬商店營業邏輯。

寫一個程式，接收當前時間 current_hour（24 小時制）和商店狀態 is_holiday（是否為假日）。
請根據以下條件判斷商店應顯示的訊息：
1. 如果是假日（is_holiday 為 True），商店總是印出 "今日公休。"
2. 如果是非假日：
    a. 時間在 9 到 18 點之間（含 9 點，不含 18 點），印出 "營業中，歡迎光臨！"
    b. 其他時間印出 "非營業時間，請明天再來。"
"""
print("--- 練習題一：判斷營業時間與狀態 ---")
current_hour = 10
is_holiday = False

# --- 開始作答 ---
if is_holiday:
    print("今日公休。")
else:
    if 9 <= current_hour < 18:
        print("營業中，歡迎光臨！")
    else:
        print("非營業時間，請明天再來。")
print("-" * 20)


# --- 練習題二：判斷會員折扣 (中等) ---
"""
寫一個程式，根據客戶的消費金額 amount 和是否為會員 is_member 來計算最終應付金額。

- 如果是會員（is_member 為 True）且消費金額超過 1000 元，給予 8 折優惠。
- 如果不是會員但消費金額超過 500 元，給予 9 折優惠。
- 其他情況則不打折。
"""
print("--- 練習題二：判斷會員折扣 ---")
amount = 1200
is_member = True

# --- 開始作答 ---
if is_member and amount > 1000:
    final_amount = amount * 0.8
    print(f"會員價 8 折！最終金額為：{final_amount} 元")
elif not is_member and amount > 500:
    final_amount = amount * 0.9
    print(f"優惠價 9 折！最終金額為：{final_amount} 元")
else:
    final_amount = amount
    print(f"無折扣，最終金額為：{final_amount} 元")
print("-" * 20)


# --- 練習題三：判斷年度季節 (進階) ---
"""
寫一個程式，接收一個代表月份的整數 month（範圍 1 到 12），並判斷它屬於哪個季節。
春季： 3, 4, 5 月
夏季： 6, 7, 8 月
秋季： 9, 10, 11 月
冬季： 12, 1, 2 月
如果月份不在 1 到 12 的範圍內，印出 "月份輸入錯誤。"
"""
print("--- 練習題三：判斷年度季節 ---")
month = 8

# --- 開始作答 ---
if month in [3, 4, 5]:
    print(f"{month} 月是春季。")
elif month in [6, 7, 8]:
    print(f"{month} 月是夏季。")
elif month in [9, 10, 11]:
    print(f"{month} 月是秋季。")
elif month in [12, 1, 2]:
    print(f"{month} 月是冬季。")
else:
    print("月份輸入錯誤。")
print("-" * 20)
