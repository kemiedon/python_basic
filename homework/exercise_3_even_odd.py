# -*- coding: utf-8 -*-

"""
練習題 2：判斷是否為偶數
輸入一個整數，判斷它是偶數還是奇數。
印出「這是偶數」或「這是奇數」。
"""

# 提示使用者輸入一個數字
input_str = input("請輸入一個整數：")

# 將輸入的字串轉換為整數
number = int(input_str)

# 使用 % 運算子檢查餘數是否為 0
if number % 2 == 0:
    print(f"數字 {number} 是偶數。")
else:
    print(f"數字 {number} 是奇數。")