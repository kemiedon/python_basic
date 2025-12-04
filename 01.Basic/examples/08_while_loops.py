# -*- coding: utf-8 -*-
"""
主題：While 迴圈 (While Loops)

說明：
While 迴圈會在指定的條件為真（True）時，重複執行一個程式碼區塊。
它適用於不知道需要迭代幾次，只知道在什麼條件下應該停止的情況。

重要：
必須確保迴圈內的條件最終會變為假（False），否則會導致無窮迴圈（infinite loop）。

語法：
while 條件:
    # 執行的程式碼區塊
    # (通常需要更新條件變數)
"""

# 範例 1：基本的計數
print("--- 範例 1: 從 1 數到 5 ---")
count = 1
while count <= 5:
    print(f"計數: {count}")
    count += 1  # 更新條件變數，使其朝著結束條件前進

print("迴圈結束！")

# 範例 2：搭配 break 敘述
# break 可以強制跳出迴圈
print("\n--- 範例 2: 使用 break ---")
# while True:  # 一個看似無窮的迴圈
#     user_input = input("輸入 'exit' 來離開迴圈: ")
#     if user_input == "exit":
#         print("偵測到 'exit'，即將離開迴圈...")
#         break  # 跳出迴圈
#     print(f"你輸入了: {user_input}")

print("成功離開迴圈。")
