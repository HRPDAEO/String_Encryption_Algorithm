import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from datetime import datetime

def get_cipher_key():
    now = datetime.now()
    hour, minute = now.hour, now.minute
    shift = minute - hour
    return abs(shift) if shift != 0 else 1

def caesar_cipher(text, mode='encrypt', key=0):
    ascii_start = 32  # ASCII可打印字符起始位置（空格）
    ascii_end = 126  # ASCII可打印字符结束位置（波浪线）
    operation = {'encrypt': lambda x, k: x + k, 'decrypt': lambda x, k: x - k}
    result = ""
    
    for char in text:
        if ascii_start <= ord(char) <= ascii_end:
            shifted = operation[mode](ord(char), key)
            # 确保字符码在可打印范围内
            new_char_code = (shifted - ascii_start) % (ascii_end - ascii_start + 1) + ascii_start
            result += chr(new_char_code)
        else:
            result += char
    return result

def on_encrypt():
    text = entry_text.get()
    key = get_cipher_key()
    encrypted_text = caesar_cipher(text, 'encrypt', key)
    current_time = datetime.now().time().strftime('%H:%M')
    update_result_text(encrypted_text, current_time)

def on_decrypt():
    root.lift()  # 确保主窗口位于最前端
    text = entry_text.get()

    hour = int(simpledialog.askstring("输入小时", "请输入小时:"))
    minute = int(simpledialog.askstring("输入分钟", "请输入分钟:"))
    
    if hour < 0 or minute < 0 or hour > 23 or minute > 59:
        messagebox.showerror("错误", "小时或分钟输入无效，请确保它们在合理的范围内。")
        return
    
    key = minute - hour
    key = abs(key) if key != 0 else 1

    decrypted_text = caesar_cipher(text, 'decrypt', key)
    update_result_text(decrypted_text, f"位移量: {key}")

def update_result_text(text, extra_info):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, text)
    result_text.insert(tk.END, f"\n{extra_info}")

root = tk.Tk()
root.title("String3.1")
root.geometry("800x700")

label_text = tk.Label(root, text="请输入文本:")
label_text.pack(pady=20)

entry_text = tk.Entry(root)
entry_text.pack(fill=tk.X, padx=20, pady=20)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=20, pady=(0,20))

button_encrypt = tk.Button(button_frame, text="加密", command=on_encrypt)
button_encrypt.pack(side=tk.LEFT, padx=10)

button_decrypt = tk.Button(button_frame, text="解密", command=on_decrypt)
button_decrypt.pack(side=tk.LEFT, padx=10)

result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10)
result_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()
