# 範例 4: 型別轉換

# --- 使用+號做字串串接 ---
first_name = "Grace"
last_name = "Hopper"

# 使用 + 組合姓名，並在中間加上空格和逗號
full_name = last_name + ", " + first_name
print(f"使用 '+' 組合的結果: {full_name}")


# --- 組合字串與數字 (需要手動轉型) ---
item = "筆記型電腦"
price = 35000

# 錯誤示範：直接將字串與數字相加會導致 TypeError
# description = "商品: " + item + ", 價格: " + price  # 這行會報錯

# 正確作法：使用 str() 將數字轉換為字串
description = "商品: " + item + ", 價格: " + str(price)
print(f"使用 '+' 組合字串與數字: {description}")

# --- 範例 1: 使用f-string ---
first_name = "Grace"
last_name = "Hopper"

# 在字串前加上 'f'，並將變數用 {} 包起來
full_name = f"{last_name}, {first_name}"
print(f"使用 f-string 的結果: {full_name}")


# --- 範例 2: 組合字串與數字 (無需手動轉型) ---
item = "筆記型電腦"
price = 35000

# f-string 會自動處理數字轉型
description = f"商品: {item}, 價格: {price}"
print(f"使用 f-string 組合字串與數字: {description}")


# --- 範例 3: 在 f-string 中使用表達式 ---
quantity = 2
total_price = f"總價是 {price * quantity} 元" # 直接在 {} 中進行運算
print(f"在 f-string 中運算: {total_price}")



# --- 型別轉換 (Type Casting) ---
print("--- 型別轉換 ---")

# 1. 字串轉數字
str_num = "100"
int_num = int(str_num)
float_num = float(str_num)

print(f"原始字串: '{str_num}', 型別: {type(str_num)}")
print(f"轉換為整數: {int_num}, 型別: {type(int_num)}")
print(f"轉換為浮點數: {float_num}, 型別: {type(float_num)}")
print("-" * 10)

# 2. 數字轉字串
age = 25
age_str = str(age)
print(f"原始數字: {age}, 型別: {type(age)}")
print(f"轉換為字串: '{age_str}', 型別: {type(age_str)}")

# 錯誤示範：不同型別直接運算會導致 TypeError
# print("Your age is " + age) # 這行會報錯
print("Your age is " + age_str) # 這樣才是正確的
print("-" * 20)

# --- 運算子優先級 (Operator Precedence) ---
# Python 遵循數學中的運算規則 (PEMDAS/BODMAS)
# 1. 括號 ()
# 2. 次方 **
# 3. 乘 * / // %
# 4. 加 + -
print("--- 運算子優先級 ---")

result1 = 10 + 2 * 3  # 優先算 2 * 3 = 6, 再算 10 + 6 = 16
print(f"10 + 2 * 3 = {result1}")

result2 = (10 + 2) * 3 # 括號優先, 先算 10 + 2 = 12, 再算 12 * 3 = 36
print(f"(10 + 2) * 3 = {result2}")

result3 = 100 / 10 * 2 # 乘除同級，由左至右計算。100/10=10, 10*2=20
print(f"100 / 10 * 2 = {result3}")
