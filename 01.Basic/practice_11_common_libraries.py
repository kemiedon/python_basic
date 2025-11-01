# -*- coding: utf-8 -*-
"""
隨堂練習：幸運數字日誌 (Lucky Number Logger)

說明：
程式會產生一個 1 到 20 之間的隨機數字，讓使用者來猜。
不論使用者猜對或猜錯，程式都會將該局的資訊（包含了玩家姓名、遊戲時間、
秘密數字、猜測數字、以及是否猜中）記錄到一個名為 `game_log.json` 的檔案中。

依照提示完成程式。
"""

# 1. 引入必要的函式庫
import random
import datetime
import json
import os

# 2. 設定日誌檔案的名稱
LOG_FILE = "game_log.json"

# 3. 歡迎玩家並取得玩家姓名
player_name = input("歡迎來到幸運數字遊戲！請輸入你的名字：")

# 4. 產生一個 1 到 20 之間的隨機整數作為秘密數字
# 提示：使用 random.randint()
secret_number = random.randint(1, 20)

print(f"你好，{player_name}！我已經想好了一個 1 到 20 之間的數字。")

# 5. 讓使用者猜數字
# 提示：使用 input() 取得使用者輸入，並用 int() 轉換成整數。
# 挑戰：可以試著用 try-except 來處理使用者輸入的不是數字的情況。
guess_str = input("請猜一個數字：")
try:
    user_guess = int(guess_str)
except ValueError:
    print("輸入無效，請輸入數字。遊戲結束。")
    # 如果輸入無效，可以選擇直接結束程式
    exit()

# 6. 判斷使用者是否猜中，並設定結果
if user_guess == secret_number:
    result_message = "恭喜你猜對了！"
    is_win = True
else:
    result_message = f"可惜猜錯了，正確答案是 {secret_number}。"
    is_win = False

print(result_message)

# 7. 準備要記錄的資料
# 提示：將遊戲結果存成一個字典
game_record = {
    "playerName": player_name,
    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "secretNumber": secret_number,
    "playerGuess": guess_str,
    "isWin": is_win,
}

# 8. 讀取舊的日誌，並將新的紀錄附加進去
# 提示：
# - 使用 os.path.exists() 檢查日誌檔案是否存在。
# - 如果存在，用 json.load() 讀取。
# - 如果不存在，就建立一個新的空列表。
# - 使用 .append() 將 game_record 加到列表中。
file_to_check = LOG_FILE
if os.path.exists(file_to_check):
    with open(file_to_check, "r") as f:
        existing_records = json.load(f)
else:
    # 如果檔案不存在，建立一個新的空列表
    existing_records = []
existing_records.append(game_record)

# 將更新後的紀錄寫回 JSON 檔案
with open(file_to_check, "w") as f:
    json.dump(existing_records, f, ensure_ascii=False, indent=4)

# 9. 將更新後的紀錄寫回 JSON 檔案
# 提示：
# - 使用 with open(...) as f: 的語法來開啟檔案。
# - 使用 json.dump() 將資料寫入檔案。
# - 記得設定 ensure_ascii=False 和 indent=4 讓檔案內容更容易閱讀。

print(f"遊戲結果已記錄至 {LOG_FILE}")
