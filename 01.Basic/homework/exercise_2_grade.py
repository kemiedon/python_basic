# -*- coding: utf-8 -*-

"""
練習題 1：決定分數等級
請使用 if、elif、else 結構。

已知一個分數 score，請根據分數印出等級（A、B、C、D）：
A：90 分以上
B：80~89 分
C：60~79 分
D：60 分以下

範例：score = 78，輸出 C級：順利通過。
"""

score = 78  # 您可以更改這個分數來測試不同的結果

if score >= 90:
    print(f"分數 {score} 是 A 級：表現優異！")
elif score >= 80:
    print(f"分數 {score} 是 B 級：做得很好！")
elif score >= 60:
    print(f"分數 {score} 是 C 級：順利通過。")
else:
    print(f"分數 {score} 是 D 級：需要再加油！")
