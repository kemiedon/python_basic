# -*- coding: utf-8 -*-
"""
主題：Python 常用的內建函式庫 (Common Built-in Libraries)

說明：
Python 擁有一個強大的標準函式庫，提供了許多現成的模組（modules）來處理各種常見任務。
我們可以使用 `import` 關鍵字來引入這些模組，並使用它們提供的功能。
這可以大大簡化我們的程式碼，避免「重新發明輪子」。
"""

# --- 範例 1: math 模組 - 數學運算 ---
import math

print("--- 1. math 模組 ---")
# 計算平方根
sqrt_of_16 = math.sqrt(16)
print(f"16 的平方根是: {sqrt_of_16}")

# 使用圓周率常數
print(f"圓周率 (pi) 的值約為: {math.pi}")

# 無條件進位與捨去
num = 3.7
print(f"{num} 無條件進位是: {math.ceil(num)}")
print(f"{num} 無條件捨去是: {math.floor(num)}")
print("-" * 20)


# --- 範例 2: re 模組 - 檢查資料格式 ---
import re
print("\n--- 2. re 模組 ---")
def 驗證電子郵件(字串):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', 字串) is not None

def 是否正整數(數值):
    return 數值 > 0

print(驗證電子郵件("abc@xyz.com"))  # True
print(驗證電子郵件("hello.world"))  # False
print(是否正整數(-5))  


# --- 範例 3: datetime 模組 - 處理日期與時間 ---
import datetime
print("\n--- 3. datetime 模組 ---")
time = datetime.datetime.now()
print(time)  # 顯示目前日期時間

new_format = time.strftime("%Y-%m-%d %H:%M")
print(new_format)  # 格式化輸出

tomorrow = time + datetime.timedelta(days=1)
print(tomorrow)  # 計算一天之後


# --- 範例 4: random 模組 - 產生隨機數 ---
import random

print("\n--- 4. random 模組 ---")
# 產生一個 1 到 10 之間的隨機整數
random_int = random.randint(1, 10)
print(f"1到10之間的隨機整數: {random_int}")

# 從列表中隨機選擇一個元素
fruits = ["蘋果", "香蕉", "櫻桃", "橘子"]
random_fruit = random.choice(fruits)
print(f"從列表中隨機選擇的水果: {random_fruit}")

# 將列表的元素隨機排序 (原地修改)
print(f"排序前的列表: {fruits}")
random.shuffle(fruits)
print(f"隨機排序後的列表: {fruits}")
print("-" * 20)


# --- 範例 5: os 模組 - 與作業系統互動 ---
print("\n--- 5. os 模組 ---")
import os

print(os.getcwd())             # 目前目錄
print(os.listdir('.'))         # 現在資料夾的檔案列表
os.mkdir('test')               # 建新資料夾
os.system('echo Hello World')  # 執行系統指令（顯示 Hello World）
print("-" * 20)

# --- 範例 6: json 模組 - 處理 JSON 資料 ---
import json

person_dict = {"name": "小明", "age": 25, "isStudent": True}
json_string = json.dumps(person_dict, ensure_ascii=False, indent=4)
print("Python 字典轉換為 JSON 字串:")
print(json_string)
print("-" * 20)
