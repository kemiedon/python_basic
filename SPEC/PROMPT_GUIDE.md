# AI 指令規範書

## 語言規定

- **必須使用繁體中文** 進行所有對話和文檔編寫

## 文檔編寫規範

### 教材範例程式碼規範

- **範例程式碼檔案路徑標示**：每個範例程式碼區塊下方必須標示對應的檔案路徑
  - 格式：**`<font style='color: brown;'>`範例檔參考: [相對路徑]`</font>`**
  - 範例：**`<font style='color: brown;'>`範例檔參考: 01.Basic/examples/01_variables_naming.py`</font>`**
- **練習題檔案路徑標示**：練習題需標示對應的練習檔案位置

  - 格式：**`<font style='color: darkblue;'>`練習檔參考: [相對路徑]`</font>`**
  - 範例：**`<font style='color: darkblue;'>`練習檔參考: 01.Basic/practice/cost_exercise.py`</font>`**

- **作業檔案路徑標示**：回家作業需標示作業檔案資料夾
  - 格式：**`<font style='color: darkblue;'>`作業檔參考: [相對路徑]`</font>`**
  - 範例：**`<font style='color: darkblue;'>`作業檔參考: 01.Basic/homework/`</font>`**

### 檔案組織結構

- **examples/** - 存放教學範例檔案（隨教材講解使用）
- **practice/** - 存放課堂練習題
- **homework/** - 存放回家作業
- **demo/** - 存放示範程式與綜合應用範例

## 提交規範

- 每當完成一個任務後，自動 push 到 repository
- Commit 訊息按照以下格式命名：`日期-時間-版本[編號]`
  - 範例：`2025-11-22-17:20:46-1.0[建立專案結構]`
  - 日期格式：YYYY-MM-DD
  - 時間格式：HH:MM:SS（24 小時制）
  - 版本編號：1.0, 1.1, 1.2...（主版本.次版本，按照當日提交次數遞增）
  - 編號說明：用方括號括起來的簡要說明
- 每次 commit 說明需要整理該次更新的內容重點
