import tkinter as tk
from datetime import datetime

def encrypt_text():
    now = datetime.now()
    hour, minute = now.hour, now.minute
    text = text_input.get("1.0", "end-1c")
    encrypted_text = "".join([chr(((ord(char) - ord('!') + (hour * 60 + minute)) % 94) + ord('!')) if '!' <= char <= '~' else char for char in text])
    
    # 显示加密后的文本
    encrypted_display.delete("1.0", "end")
    encrypted_display.insert("1.0", encrypted_text)
    
    # 显示加密时间
    time_info = f"加密时间: {hour}:{minute}"
    encrypted_display.insert("end", "\n\n" + time_info)

def decrypt_text():
    hour = int(hour_input.get())
    minute = int(minute_input.get())
    text = text_input.get("1.0", "end-1c")
    decrypted_text = "".join([chr(((ord(char) - ord('!') - (hour * 60 + minute) + 94) % 94) + ord('!')) if '!' <= char <= '~' else char for char in text])
    decrypted_display.delete("1.0", "end")
    decrypted_display.insert("1.0", decrypted_text)

# 创建主窗口
root = tk.Tk()
root.title("String3.0")

# 文本输入框
text_input_label = tk.Label(root, text="请输入文本:")
text_input_label.pack()
text_input = tk.Text(root, height=10)
text_input.pack()

# 加密结果显示框
encrypted_label = tk.Label(root, text="加密后文本及时间:")
encrypted_label.pack()
encrypted_display = tk.Text(root, height=10)
encrypted_display.pack()

# 加密按钮
encrypt_button = tk.Button(root, text="加密", command=encrypt_text)
encrypt_button.pack()

# 解密部分
decrypt_frame = tk.Frame(root)
decrypt_frame.pack(pady=10)

hour_input_label = tk.Label(decrypt_frame, text="加密时的小时:")
hour_input_label.pack(side=tk.LEFT)
hour_input = tk.Entry(decrypt_frame)
hour_input.pack(side=tk.LEFT)

minute_input_label = tk.Label(decrypt_frame, text="加密时的分钟:")
minute_input_label.pack(side=tk.LEFT)
minute_input = tk.Entry(decrypt_frame)
minute_input.pack(side=tk.LEFT)

# 解密结果显示框
decrypted_label = tk.Label(root, text="解密后文本:")
decrypted_label.pack()
decrypted_display = tk.Text(root, height=10)
decrypted_display.pack()

decrypt_button = tk.Button(root, text="解密", command=decrypt_text)
decrypt_button.pack()

# 运行主循环
root.mainloop()
