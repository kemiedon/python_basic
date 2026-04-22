import tkinter as tk

root = tk.Tk()
root.title("登入範例")
root.geometry("300x150")

# Label 與 Entry
tk.Label(root, text="帳號：").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="密碼：").grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_user = tk.Entry(root)
entry_pass = tk.Entry(root, show="*")

entry_user.grid(row=0, column=1, padx=5, pady=5)
entry_pass.grid(row=1, column=1, padx=5, pady=5)

def login():
    user = entry_user.get()
    pwd = entry_pass.get()
    print("登入帳號：", user, " 密碼：", pwd)

tk.Button(root, text="登入", command=login).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
