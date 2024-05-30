import tkinter as tk
from tkinter import simpledialog
import random

def encrypt():
    text = entry_input.get()
    offset = random.randint(1, 3)
    encrypted_text = ''.join([chr(ord(c) + offset) for c in text]) + str(offset)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, encrypted_text)

def decrypt():
    text_with_offset = entry_input.get()
    try:
        offset = int(text_with_offset[-1])
        text = text_with_offset[:-1]
        decrypted_text = ''.join([chr(ord(c) - offset) for c in text])
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, decrypted_text)
    except ValueError:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "错误：输入格式不正确，请确保以数字结尾。")

# 创建主窗口
root = tk.Tk()
root.title("String 4.0")

# 输入框
entry_input = tk.Entry(root)
entry_input.pack(pady=10)

# 加密按钮
btn_encrypt = tk.Button(root, text="加密", command=encrypt)
btn_encrypt.pack(pady=5)

# 解密按钮
btn_decrypt = tk.Button(root, text="解密", command=decrypt)
btn_decrypt.pack(pady=5)

# 结果显示区域
text_output = tk.Text(root, height=10)
text_output.pack(pady=10)

# 启动事件循环
root.mainloop()
