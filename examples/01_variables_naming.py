# 範例 1: 變數宣告與命名規範 (PEP 8)

# --- 好的命名習慣 (Snake Case) ---
# 變數名稱應該小寫，並用底線分隔單字，使其易於閱讀。
print("--- 好的命名範例 ---")
user_name = "JohnDoe"
user_age = 25
is_active_user = True

print(f"使用者名稱: {user_name}")
print(f"使用者年齡: {user_age}")
print(f"是活躍使用者嗎: {is_active_user}")
print("-" * 20)

# --- 不好的命名習慣 ---
print("--- 不好的命名範例 (請避免) ---")
# 1. 不可使用數字開頭
# 1st_user = "John"  # 這行會產生 SyntaxError

# 2. 不可使用 Python 關鍵字 (如 for, if, class, def 等)
# for = "loop"       # 這行會產生 SyntaxError

# 3. 避免使用不易理解的縮寫
un = "JohnDoe" # 不清楚 un 代表什麼

# 4. Python 變數名稱有區分大小寫
student_name = "Alice"
Student_Name = "Bob"
print(f"student_name: {student_name}")
print(f"Student_Name: {Student_Name}")
print("注意：'student_name' 和 'Student_Name' 是兩個不同的變數！")
