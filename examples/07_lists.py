# -*- coding: utf-8 -*-
"""
主題：串列 (Lists)

說明：
串列是 Python 中最常用的資料結構之一。它是一個有序且可變（mutable）的集合。
- 有序（Ordered）：串列中的元素有固定的順序，這個順序不會改變。
- 可變（Mutable）：你可以新增、刪除或修改串列中的元素。
- 允許多個相同的值：串列中可以包含重複的元素。

串列使用方括號 `[]` 來定義，元素之間用逗號 `,` 分隔。
"""

# 範例 1：建立串列
print("--- 範例 1: 建立串列 ---")
# 一個包含數字的串列
numbers = [1, 2, 3, 4, 5]
print(f"數字串列: {numbers}")

# 一個包含字串的串列
fruits = ["蘋果", "香蕉", "櫻桃"]
print(f"水果串列: {fruits}")

# 一個混合類型的串列
mixed_list = [1, "Hello", 3.14, True]
print(f"混合串列: {mixed_list}")

# 範例 2：存取串列元素
print("\n--- 範例 2: 存取元素 ---")
# 索引值從 0 開始
first_fruit = fruits[0]
print(f"第一個水果是: {first_fruit}")

second_number = numbers[1]
print(f"第二個數字是: {second_number}")

# 範例 3：修改串列元素
print("\n--- 範例 3: 修改元素 ---")
print(f"原來的水果串列: {fruits}")
fruits[1] = "藍莓"  # 將 '香蕉' 改成 '藍莓'
print(f"修改後的水果串列: {fruits}")

# 範例 4：常用的串列方法
print("\n--- 範例 4: 常用方法 ---")
# .append()：在串列末尾新增元素
fruits.append("橘子")
print(f"append '橘子' 後: {fruits}")

# .remove()：移除指定的第一個符合的元素
fruits.remove("蘋果")
print(f"remove '蘋果' 後: {fruits}")

# len()：取得串列長度
print(f"串列現在的長度是: {len(fruits)}")
