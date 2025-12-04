# -*- coding: utf-8 -*-

"""
string_manipulation_exercise.py

這個檔案包含字串處理的練習題。
請在每個練習題下方的 # --- 開始作答 --- 區塊中撰寫你的程式碼。
"""

# --- 練習題 1: 提取檔案副檔名 ---
# 給定一個檔案名稱字串，請提取其副檔名 (不包含'.')。
file_name = "example_document.pdf"
extension = ""

# .split('.') 會將字串用 '.' 分割成一個列表 ['example_document', 'pdf']
extension = file_name.split('.')[-1]
print(f"檔案 '{file_name}' 的副檔名是: {extension}")
print("-" * 20)


# --- 練習題 2: 格式化姓名 ---
# 給定一個格式混亂的名字字串，請將其整理成標準格式：
# 1. 移除前後多餘的空白。
# 2. 將名字轉換為首字大寫的格式 (Title Case)。
messy_name = "  alAn tURiNg  "
formatted_name = ""

# .strip() 用於移除前後空白，.title() 用於將每個單字的首字母轉為大寫
formatted_name = messy_name.strip().title()
print(f"整理前的名字: '{messy_name}'")
print(f"整理後的名字: '{formatted_name}'")
print("-" * 20)


# --- 練習題 3: 計算句子中的單字數量 ---
# 給定一個句子，請計算裡面有多少個單字。
sentence = "Python is a versatile and powerful programming language."
word_count = 0

# .split(' ') 會用空格分割句子成一個單字列表，len() 函式可以取得列表的長度
word_count = len(sentence.split(' '))
print(f"句子 '{sentence}' 中有 {word_count} 個單字。")


# --- 練習題 4: 互動式姓名產生器 ---
# 請撰寫一段程式，完成以下步驟：
# 1. 使用 input() 提示使用者輸入他們的「姓氏」(last name)。
# 2. 使用 input() 提示使用者輸入他們的「名字」(first name)。
# 3. 將姓氏和名字串接起來，並在中間加上一個空格。
# 4. 使用 print() 印出完整的姓名，格式為 "Hello, [名字] [姓氏]!"。
# 範例輸入:
#   請輸入您的姓氏：Wang
#   請輸入您的名字：David
# 範例輸出:
#   Hello, David Wang!
s1 = input("請輸入您的姓氏：")
s2 = input("請輸入您的名字：")
print(s1 , s2, sep='')
print(s1 , s2, sep='')

# --- 練習題 5: 字串切片 (Slicing) ---
# 宣告一個字串，並練習使用不同的切片方式來提取部分字串。
# 語法: string[start:stop:step]
# start: 起始索引 (包含)
# stop:  結束索引 (不包含)
# step:  間隔

example_str = "Hello, Python World!"

# 範例 1: 提取 "Python"
# "Python" 從索引 7 開始，到索引 13 結束。
print(example_str[7:13])

# 範例 2: 從頭提取到 "Python" (不含 "Python")
print(example_str[:6])
print(example_str[0:6])

# 範例 3: 提取最後 6 個字元 ("World!")
print(example_str[-6:])

# 範例 4: 將整個字串反轉
print(example_str[::-1])

# 範例 5: 提取 "Python" (使用負數索引)
# "Python" 從倒數第 13 個字元開始，到倒數第 7 個字元結束。
print(example_str[-13: -7])

# 範例 6: 混合使用正負數索引
# 提取從索引 2 ("l") 開始，到倒數第 8 個字元 (" ") 之前的所有內容。
print(example_str[2: -7])

# 範例 7: 去掉頭尾
# 提取除了第一個和最後一個字元以外的所有內容。
print(example_str[1: -1])

# 範例 8: 提取奇數索引的字元
# 使用 step 參數來跳著提取。
print(example_str[::2])