# -*- coding: utf-8 -*-
"""
主題：For 迴圈 (For Loops)

說明：
For 迴圈用於迭代（iterate）一個序列（sequence）中的每個元素。
序列可以是列表（list）、元組（tuple）、字典（dictionary）、集合（set）或字串（string）。
For 迴圈的語法結構清晰，非常適合在已知迭代次數的情況下使用。

語法：
for 變數 in 序列:
    # 執行的程式碼區塊
"""

# 範例 1：迭代一個列表 (list)
print("--- 範例 1: 迭代水果列表 ---")
fruits = ["蘋果", "香蕉", "櫻桃"]
for fruit in fruits:
    print(f"我喜歡吃 {fruit}")

# 範例 2：使用 range() 函數
# range(5) 會產生 0, 1, 2, 3, 4 的序列
print("\n--- 範例 2: 使用 range() ---")
for i in range(5):
    print(f"這是第 {i} 次迴圈")

# 範例 3：迭代一個字串 (string)
print("\n--- 範例 3: 迭代字串 ---")
for char in "Python":
    print(char)

# 範例 4：搭配 enumerate() 獲取索引值
print("\n--- 範例 4: 使用 enumerate() ---")
for index, fruit in enumerate(fruits):
    print(f"水果列表的第 {index} 個元素是 {fruit}")
