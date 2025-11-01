# -*- coding: utf-8 -*-

"""
練習題 3：求和計算
使用 for 迴圈，計算 1 到 100 所有整數的總和。
提示：可以使用變數來累加。
"""

total = 0  # 初始化總和變數

# range(1, 101) 會產生從 1 到 100 的整數序列
for i in range(1, 101):
    total += i  # 將每個數字累加到 total 中

print(f"1 到 100 的總和是：{total}")