# 定義一個函式
def say_hello():
    print("Hello, Python!")


say_hello()  # 呼叫這個函數，就會印出 Hello, Python!


# 有參數的函式
def greet(name, age):
    print(f"{name} 今年 {age} 歲")


greet("小明", 18)

# 指定名稱傳值
# greet(age=18, name="小明")


# 未輸入參數時用預設值
def greet(name, age=20):
    print(f"{name} 今年 {age} 歲")


greet("小美")  # age自動是20


# 有返回值的函式
def add(x, y):
    return x + y


result = add(3, 7)  # result 得到 10

# 變數作用域
value = 10  # 全域變數


def show():
    print(value)  # 這裡也能用 value


show()


# 區域變數
def func():
    x = 5  # 區域變數，只能在 func 裡用
    print(x)


func()
print(x)  # 這裡會出錯，因為 x 不存在

# 使用global關鍵字
value = 10


def update():
    global value
    value = 99  # 直接改全域


update()
print(value)

# lambda函式
add = lambda x, y: x + y
result = add(3, 7)  # result 得到 10

# map函式
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(f"map 範例 (每個數字乘以2): {doubled}")  # [2, 4, 6, 8, 10]

# filter函式
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"filter 範例 (只保留偶數): {even_numbers}")  # [2, 4]

# sorted函式
# 假設我們想根據字串的長度來排序
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda word: len(word))

print(f"sorted 範例 (根據字串長度排序): {sorted_words}")
# ['date', 'apple', 'cherry', 'banana']
