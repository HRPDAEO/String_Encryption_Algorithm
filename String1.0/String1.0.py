import tkinter as tk

def reverse_text():
    input_text = entry.get()
    reversed_text = input_text[::-1]
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, reversed_text)

app = tk.Tk()
app.title("String1.0")

frame = tk.Frame(app)
frame.pack(pady=10)

label = tk.Label(frame, text="请输入原文:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

button = tk.Button(frame, text="执行", command=reverse_text)
button.pack(side=tk.LEFT)

text_output = tk.Text(app, height=10, width=60)
text_output.pack(pady=10)

app.mainloop()
