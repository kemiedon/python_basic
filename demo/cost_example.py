# --- 1: 計算總花費。 ---
# 假設書本 250 元，咖啡 75 元。計算總花費。
book_price = 250
coffee_price = 75
total_cost = book_price + coffee_price
print("總花費為:", total_cost)

# --- 2: 購物找零 ---
# 你買了 3 瓶價格為 45 元的飲料和 2 個價格為 30 元的三明治。
# 如果你用一張 500 元的鈔票付款，請問應該找回多少錢？
change = 0
total_spent = (3 * 45) + (2 * 30) # 計算總花費
change = 500 - total_spent        # 計算找零

print(f"應找回 {change} 元。")
print("-" * 20)


# --- 3: 分糖果 ---
# 有 100 顆糖果，要分給 8 個小朋友。請計算每個小朋友可以分到幾顆糖果？剩下幾顆糖果？
candies_per_child = 0
remaining_candies = 0


candies_per_child = 100 // 8 # 使用整數除法
remaining_candies = 100 % 8  # 使用取餘數運算

print(f"每個小朋友可以分到 {candies_per_child} 顆糖果，剩下 {remaining_candies} 顆。")