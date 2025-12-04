"""
for_while_example.py

這個檔案是 for 迴圈與 while 迴圈的教學範例。
"""

# ====================================================================
# For 迴圈：當你知道要「跑幾次」或要「遍歷一個序列」時使用
# ====================================================================

print("--- 1. 使用 range() 函式：執行固定次數 ---")
# range(5) 會產生 0, 1, 2, 3, 4 的序列
print("  range(5):")
for i in range(5):
    print(f"第 {i} 次迴圈")

# range(1, 6) 會產生 1, 2, 3, 4, 5 的序列
print("\n  range(1, 6):")
for i in range(1, 6):
    print(f"數字 {i}")

# range(0, 11, 2) 會產生 0, 2, 4, 6, 8, 10 的序列 (從0開始，到11前，間隔2)
print("\n  range(0, 11, 2) 印出偶數:")
for i in range(0, 11, 2):
    print(f"偶數 {i}")
print("-" * 25)


print("--- 2. 基本用法：遍歷 (Iterate) 一個清單 ---")
fruits = ["apple", "banana", "kiwi"]
for fruit in fruits:
    print(f"清單中的水果：我要吃 {fruit}！")
print("-" * 25)


print("--- 3. 遍歷一個字串 ---")
message = "Python"
for char in message:
    print(f"字串中的字元：{char}")
print("-" * 25)


print("--- 4. 使用 enumerate() 同時取得索引和值 ---")
scores = [95, 88, 76]
for index, score in enumerate(scores):
    print(f"  第 {index + 1} 位學生的分數是 {score}")
print("-" * 25)


print("--- 5. 搭配 break 和 continue ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("  - 使用 break 找到第一個大於 5 的數字就停止:")
for num in numbers:
    if num > 5:
        print(f"    找到了！數字是 {num}")
        break  # 跳出整個 for 迴圈
    print(f"    檢查數字 {num}...")

print("\n  - 使用 continue 跳過所有偶數:")
for num in numbers:
    if num % 2 == 0:
        continue  # 跳過這次迴圈，直接進入下一次
    print(f"    奇數是: {num}")
print("-" * 25)


# ====================================================================
# While 迴圈：當你不知道要跑幾次，但知道「何時該停止」時使用
# ====================================================================

print("--- While 迴圈範例：直到條件滿足才停止 ---")
money_needed = 100
money_saved = 0
count = 1

while money_saved < money_needed:
    print(f"  第 {count} 次存錢，目前金額：{money_saved}")
    money_saved += 30  # 每次存 30 元
    count += 1

print(f"恭喜！終於存到 {money_saved} 元，可以買玩具了。")