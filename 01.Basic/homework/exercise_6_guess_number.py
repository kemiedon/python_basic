# -*- coding: utf-8 -*-

"""
練習題 5：while 迴圈猜數字
輸入一個目標數字 answer，寫一個 while 迴圈，每次提示使用者猜一個數字 guess。
如果猜對就結束迴圈並印出「猜中！」；猜錯則繼續提示直到猜對。
"""

answer = 42  # 設定目標數字

while True:  # 建立一個無限迴圈
    # 提示使用者輸入猜測的數字
    guess_str = input("猜一個數字：")
    guess = int(guess_str)

    if guess == answer:
        print("恭喜，猜中了！")
        break  # 猜對了，跳出迴圈
    else:
        print("猜錯了，再試一次！")

print("遊戲結束。")