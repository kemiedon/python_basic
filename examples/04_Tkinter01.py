import tkinter as tk  # 1. 匯入模組

# 2. 建立主視窗
root = tk.Tk()
root.title("Tkinter Demo")  # 設定視窗標題
root.geometry("300x150")  # 設定視窗大小（寬x高）

# 3. 建立元件
label = tk.Label(root, text="請按下面的按鈕")
label.pack(pady=10)  # 使用 pack 佈局並加一點垂直間距


def on_click():
    # 6. 事件處理函式：按下按鈕時要做的事
    label.config(text="按鈕已被按下！")


button = tk.Button(root, text="點我", command=on_click)
button.pack(pady=5)

# 7. 啟動事件迴圈
root.mainloop()
