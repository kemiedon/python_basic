"""
主題：常見的 Python 錯誤與例外處理 (Errors and Exceptions)

說明：
在編寫程式時，錯誤是不可避免的。了解不同類型的錯誤可以幫助我們更快地除錯。
Python 會在偵測到錯誤時引發「例外 (Exception)」，並停止程式執行。
我們可以使用 try...except 區塊來「捕捉」這些例外，並執行應對的程式碼，而不是讓程式崩潰。
"""

# --- 1. SyntaxError: 語法錯誤 ---
# 說明：這是最基本的錯誤，表示你的程式碼不符合 Python 的語法規則。
#       通常是拼寫錯誤、漏掉括號、冒號等。
#       這個錯誤在執行前就會被 Python 直譯器發現。
print("--- 1. SyntaxError ---")
# 下面這行如果取消註解，會引發 SyntaxError，因為 print 函數的括號沒有寫完整。
# print("Hello, World!"
print("範例：print('Hi' (漏括號)\n")


# --- 2. NameError: 名稱錯誤 ---
# 說明：當你試圖使用一個尚未被定義（賦值）的變數時，會發生此錯誤。
print("--- 2. NameError ---")
# 下面這行如果取消註解，會引發 NameError，因為變數 `undefined_variable` 不存在。
# print(undefined_variable)
print("範例：print(a) (當 a 從未被宣告過)\n")


# --- 3. TypeError: 型別錯誤 ---
# 說明：當你對一個不支援該操作的型別執行某個操作時，會發生此錯誤。
#       例如，將字串和數字相加。
print("--- 3. TypeError ---")
# 下面這行如果取消註解，會引發 TypeError。
# result = "Hello" + 5
print("範例：3 + 'Hello'\n")


# --- 4. ValueError: 值錯誤 ---
# 說明：當一個函數的參數型別正確，但值不合適時，會引發此錯誤。
#       例如，試圖將一個非數字的字串轉換為整數。
print("--- 4. ValueError ---")
# 下面這行如果取消註解，會引發 ValueError，因為 'xyz' 無法被轉換成數字。
# number = int("xyz")
print("範例：int('xyz')\n")


# --- 5. IndexError: 索引錯誤 ---
# 說明：當你試圖存取序列（如串列、元組）中一個不存在的索引時，會發生此錯誤。
print("--- 5. IndexError ---")
my_list = [10, 20, 30]
# 串列 my_list 只有索引 0, 1, 2。存取索引 3 會引發 IndexError。
# print(my_list[3])
print(f"範例：串列 lst = [1]; print(lst[2]) (索引超出範圍)\n")


# --- 6. KeyError: 鍵錯誤 ---
# 說明：當你試圖存取字典（dictionary）中一個不存在的鍵（key）時，會發生此錯誤。
print("--- 6. KeyError ---")
my_dict = {"name": "Alice", "age": 25}
# 字典 my_dict 中沒有 'city' 這個鍵。
# print(my_dict["city"])
print("範例：d = {}; print(d['key']) (查無此鍵)\n")


# --- 7. ZeroDivisionError: 除以零錯誤 ---
# 說明：當數字運算中，除數為零時，會引發此錯誤。
print("--- 7. ZeroDivisionError ---")
# 下面這行如果取消註解，會引發 ZeroDivisionError。
# result = 10 / 0
print("範例：10 / 0\n")


# --- 8. AttributeError: 屬性錯誤 ---
# 說明：當你試圖存取或呼叫一個物件不存在的屬性（attribute）或方法（method）時，會發生此錯誤。
print("--- 8. AttributeError ---")
# 字串（str）物件沒有一個叫做 'push' 的方法（串列才有 .append()）。
# "hello".push("!")
print("範例：'abc'.push() (字串沒有 push 方法)\n")


# --- 9. IndentationError: 縮排錯誤 ---
# 說明：當程式碼的縮排不正確時，會發生此錯誤。Python 對縮排非常嚴格。
#       這跟 SyntaxError 一樣，在執行前就會被檢查出來。
print("--- 9. IndentationError ---")
# 下面的 if 敘述後方的 print 沒有正確縮排。
# if True:
# print("沒有縮排")
print("範例：if 語句後未縮排\n")


# --- 10. FileNotFoundError: 檔案未找到錯誤 ---
# 說明：當你試圖開啟一個不存在的檔案時，會發生此錯誤。
print("--- 10. FileNotFoundError ---")
# 如果 'non_existent_file.txt' 不存在於當前目錄，下面這行會引發錯誤。
# with open("non_existent_file.txt", "r") as f:
#     content = f.read()
print("範例：open('none.txt')\n")


# --- 如何處理例外 (Exception Handling) ---
print("--- 使用 try...except 處理例外 ---")
try:
    # 我們試著執行可能會出錯的程式碼
    user_input = input("請輸入一個數字：")
    number = int(user_input)
    result = 10 / number
    print(f"10 除以 {number} 的結果是 {result}")
except ValueError:
    # 如果使用者輸入的不是數字，int() 會引發 ValueError
    print("錯誤：請輸入有效的數字，而不是文字。")
except ZeroDivisionError:
    # 如果使用者輸入 0，會引發 ZeroDivisionError
    print("錯誤：不能除以零。")
except Exception as e:
    # 捕捉其他所有未預期的錯誤
    print(f"發生了未預期的錯誤：{e}")
