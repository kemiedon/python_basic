# .lower() - 轉小寫
s = "PYTHON"
print(f'"{s}".lower() → {s.lower()}')

# .upper() - 轉大寫
s = "python"
print(f'"{s}".upper() → {s.upper()}')

# .capitalize() - 開頭大寫
s = "hello world"
print(f'"{s}".capitalize() → {s.capitalize()}')

# .title() - 每個單字開頭大寫
s = "hello world"
print(f'"{s}".title() → {s.title()}')

# .strip() - 去除前後空白
s = " hi "
print(f'"{s}".strip() → {s.strip()}')

# .replace(a, b) - 取代字串
s = "2024"
print(f'"{s}".replace("2", "3") → {s.replace("2", "3")}')

# .split() - 拆分成列表
s = "a,b,c"
print(f'"{s}".split(",") → {s.split(",")}')

# .join() - 合併列表成字串
l = ['a', 'b', 'c']
print(f'"-".join({l}) → {"-".join(l)}')

# .find() - 回傳子字串位置
s = "hello"
print(f'"{s}".find("l") → {s.find("l")}')

# .count() - 計算出現次數
s = "banana"
print(f'"{s}".count("a") → {s.count("a")}')

# .startswith() - 是否以特定字開頭
s = "hello"
print(f'"{s}".startswith("he") → {s.startswith("he")}')

# .endswith() - 是否以特定字結尾
s = "hello"
print(f'"{s}".endswith("o") → {s.endswith("o")}')
