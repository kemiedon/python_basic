# Python 入門課程教材

本 repository 包含 Python 入門課程的完整教材與範例程式。

## 📚 課程內容

### 單元一：環境設定

- Anaconda 介紹與安裝
- conda 與 pip 差異
- VS Code 設定
- 虛擬環境管理

### 單元二：變數、資料型別與運算

- 變數命名規則（PEP8）
- 基本資料型別（int, float, str, bool）
- 算術運算子
- 字串組合（+ 運算子 vs f-string）
- 常用容器資料型別（List, Tuple, Dict, Set）

### 單元三：程式設計基礎流程與結構

- if/elif/else 條件判斷
- 比較與邏輯運算子
- for 迴圈（range, enumerate）
- while 迴圈
- break 與 continue 流程控制

### 單元四：錯誤處理

- 常見錯誤訊息解析
- try-except 基本用法
- finally 與 else
- 實務除錯流程

### 單元五：字串與串列操作

- 字串索引與切片
- 字串拼接與重複
- 字串常見方法
- 串列基本操作
- 串列排序與拷貝
- 巢狀串列

### 單元六：元組、字典與集合

- 元組（Tuple）特性與應用
- 字典（Dictionary）操作
- 集合（Set）與集合運算
- 資料結構選擇與轉換

### 單元七：函式設計

- 函式定義與參數傳遞
- return 回傳值
- 變數作用域（全域 vs 區域）
- lambda 匿名函數
- 常用函式庫（math, random, datetime, os, json）

### 實務演練

- 智慧生活小幫手（Smart Life Assistant）
- 綜合應用所有基礎語法

## 📂 資料夾結構

```
python_basic/
├── README.md                    # 本檔案
├── python_basic.md             # 完整教材文件
├── common_container_types.md   # 容器資料型別參考
├── SPEC/
│   └── PROMPT_GUIDE.md        # AI 指令規範
├── examples/                   # 教學範例檔案
│   ├── 00_hello.py
│   ├── 01_variables_naming.py
│   ├── 02_data_types.py
│   ├── 03_operations.py
│   ├── 04_type_conversion_precedence.py
│   ├── 05_conditional_statements.py
│   ├── 06_for_loops.py
│   ├── 07_lists.py
│   ├── 08_while_loops.py
│   ├── 09_error_exception.py
│   ├── 10_functions.py
│   ├── 11_common_libraries.py
│   └── practice_11_common_libraries.py
├── demo/                       # 示範程式與綜合應用
│   ├── cost_example.py
│   ├── if_else_example.py
│   ├── for_while_example.py
│   ├── string_example.py
│   └── string_methods_example.py
├── practice/                   # 課堂練習題
│   ├── cost_exercise.py
│   ├── if_exercise.py
│   ├── for_loop_exercise.py
│   ├── while_loop_exercise.py
│   ├── string_exercise.py
│   ├── string_slicing_practice.py
│   ├── for_while_exercise.py
│   └── christmas_tree_with_numbers.py
└── homework/                   # 回家作業
    ├── exercise_1_basic_calculations.py
    ├── exercise_2_grade.py
    ├── exercise_3_even_odd.py
    ├── exercise_4_sum.py
    ├── exercise_5_max_value.py
    ├── exercise_6_guess_number.py
    ├── exercise_7_nested_loops.py
    └── exercise_9_string_methods_exercise.py
```

## 🚀 使用方式

### 環境需求

- Python 3.10+
- 建議使用 Anaconda 發行版

### 建立虛擬環境

```bash
# 使用 conda 建立環境
conda create -n pyclass python=3.10

# 啟用環境
conda activate pyclass

# 安裝常用套件（選用）
conda install numpy pandas matplotlib
```

### 執行範例

```bash
# 在專案根目錄執行
python examples/00_hello.py
python examples/05_conditional_statements.py
python examples/11_common_libraries.py

# 執行練習題
python practice/cost_exercise.py
python practice/if_exercise.py
```

## 📖 學習建議

1. **循序漸進**：按照單元順序學習，打好基礎
2. **動手實作**：每個範例都要親自執行並修改測試
3. **完成練習**：課堂練習和回家作業都要完成
4. **理解概念**：不要只是背語法，要理解程式邏輯
5. **善用 AI**：遇到問題可以詢問 AI，但要理解答案

## 📝 教材特色

- ✅ **生活化說明**：用日常情境解釋程式概念
- ✅ **完整範例**：所有程式碼都可直接執行
- ✅ **階段式練習**：從簡單到複雜，循序漸進
- ✅ **實務應用**：最後的專題整合所有知識
- ✅ **檔案路徑標示**：教材中清楚標示每個範例的檔案位置

## 🎯 學習目標

完成本課程後，學生將能夠：

- ✅ 建立並管理 Python 開發環境
- ✅ 理解 Python 基本語法與資料型別
- ✅ 使用條件判斷與迴圈處理程式邏輯
- ✅ 進行基本的錯誤處理與除錯
- ✅ 操作字串、串列等資料結構
- ✅ 定義和使用函式
- ✅ 使用常用的 Python 內建模組
- ✅ 開發簡單的互動式應用程式

## 👨‍💻 作者

廣瞻互動媒體設計 林靜君(Kemie)老師

## 📅 更新日期

2025-12-04

## 📄 授權

本教材僅供教學使用。

---

**Happy Coding! 🐍✨**
