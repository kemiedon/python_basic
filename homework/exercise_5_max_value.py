# -*- coding: utf-8 -*-

"""
練習題 4：最大值判斷
宣告三個變數：a, b, c。
使用條件判斷，找到最大的值並印出。

範例：a = 3, b = 7, c = 5，輸出 最大值是 7
"""

a = 3
b = 7
c = 5

if a >= b and a >= c:
    max_value = a
elif b >= a and b >= c:
    max_value = b
else:
    max_value = c

print(f"a={a}, b={b}, c={c} 中，最大值是 {max_value}")