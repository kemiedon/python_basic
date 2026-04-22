"""
字串組合對照範例
為什麼要學字串組合？
- 幾乎所有對外顯示都需要「把變數塞進一句話」
- log 訊息、報表文字、錯誤提示、API 回應
"""

# ============================================
# 範例 1：訂單資訊顯示
# ============================================
print("=== 範例 1：訂單資訊顯示 ===\n")

# 訂單資料
order_id = 123
total_amount = 580
payment_status = "已付款"

# 方式 1：使用 + 運算子（不推薦，難以閱讀且容易出錯）
message1 = (
    "訂單 #"
    + str(order_id)
    + "，總金額 "
    + str(total_amount)
    + " 元，付款狀態："
    + payment_status
)
print("使用 + 運算子：")
print(message1)
print()

# 方式 2：使用 f-string（推薦，可讀性高）
message2 = f"訂單 #{order_id}，總金額 {total_amount} 元，付款狀態：{payment_status}"
print("使用 f-string：{message2}")

print()

# ============================================
# 範例 2：Log 訊息記錄
# ============================================
print("=== 範例 2：Log 訊息記錄 ===\n")

# 系統資訊
timestamp = "2026-01-29 14:30:15"
user_id = "user_8888"
action = "登入"
ip_address = "192.168.1.100"

# 使用 + 運算子（混亂且容易出錯）
log1 = "[" + timestamp + "] 使用者 " + user_id + " 從 " + ip_address + " 執行 " + action
print("使用 + 運算子：")
print(log1)
print()

# 使用 f-string（清楚明瞭）
log2 = f"[{timestamp}] 使用者 {user_id} 從 {ip_address} 執行 {action}"
print("使用 f-string：")
print(log2)
print()

# ============================================
# 範例 3：錯誤提示訊息
# ============================================
print("=== 範例 3：錯誤提示訊息 ===\n")

# 錯誤資訊
filename = "data.csv"
line_number = 42
error_type = "格式錯誤"

# 使用 + 運算子
error1 = "檔案 " + filename + " 第 " + str(line_number) + " 行發生 " + error_type
print("使用 + 運算子：")
print(error1)
print()

# 使用 f-string
error2 = f"檔案 {filename} 第 {line_number} 行發生 {error_type}"
print("使用 f-string：")
print(error2)
print()

# ============================================
# 範例 4：除錯時印出變數值
# ============================================
print("=== 範例 4：除錯時印出變數值 ===\n")

# 程式變數
username = "Alice"
score = 95
level = 12
is_premium = True

# 使用 + 運算子（需要轉換型別，麻煩）
debug1 = (
    "使用者名稱: "
    + username
    + ", 分數: "
    + str(score)
    + ", 等級: "
    + str(level)
    + ", 會員: "
    + str(is_premium)
)
print("使用 + 運算子：")
print(debug1)
print()

# 使用 f-string（自動轉換型別，方便）
debug2 = f"使用者名稱: {username}, 分數: {score}, 等級: {level}, 會員: {is_premium}"
print("使用 f-string：")
print(debug2)
print()

# ============================================
# 範例 5：報表文字生成
# ============================================
print("=== 範例 5：報表文字生成 ===\n")

# 銷售數據
product_name = "筆記型電腦"
sold_count = 45
revenue = 1350000
growth_rate = 23.5

# 使用 + 運算子（冗長且容易出錯）
report1 = (
    "商品「"
    + product_name
    + "」本月銷售 "
    + str(sold_count)
    + " 台，營收 "
    + str(revenue)
    + " 元，成長率 "
    + str(growth_rate)
    + "%"
)
print("使用 + 運算子：")
print(report1)
print()

# 使用 f-string（簡潔清楚）
report2 = f"商品「{product_name}」本月銷售 {sold_count} 台，營收 {revenue} 元，成長率 {growth_rate}%"
print("使用 f-string：")
print(report2)
print()

# f-string 還可以格式化數字
report3 = f"商品「{product_name}」本月銷售 {sold_count} 台，營收 {revenue:,} 元，成長率 {growth_rate:.1f}%"
print("使用 f-string + 格式化：")
print(report3)
print()

# ============================================
# 範例 6：API 回應訊息
# ============================================
print("=== 範例 6：API 回應訊息 ===\n")

# API 資訊
status_code = 200
request_id = "req_abc123xyz"
processing_time = 0.145

# 使用 f-string 生成 API 回應
api_response = f"請求成功 (狀態碼: {status_code})，請求 ID: {request_id}，處理時間: {processing_time:.3f} 秒"
print(api_response)
print()

# ============================================
# 總結比較
# ============================================
print("=" * 50)
print("總結：")
print("=" * 50)
print("✗ 使用 + 運算子的缺點：")
print("  1. 需要手動轉換型別（str()）")
print("  2. 程式碼難以閱讀，很多引號和加號")
print("  3. 容易出錯（忘記空格、引號配對）")
print()
print("✓ 使用 f-string 的優點：")
print("  1. 自動轉換型別")
print("  2. 程式碼清楚，一眼看出訊息格式")
print("  3. 支援運算式和格式化")
print("  4. 適合所有需要組合字串的場景")
