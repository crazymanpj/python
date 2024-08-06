import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pdf2docx import parse

# 创建窗口
window = tk.Tk()
window.title("PDF转Word工具")
window.geometry("300x300")

# 输入框和按钮
input_label = tk.Label(window, text="上传PDF文件路径：")
input_label.pack(pady=10)

input_entry = tk.Entry(window, width=40)
input_entry.pack()

upload_button = tk.Button(window, text="上传文件", command=lambda: upload_file(input_entry))
upload_button.pack(pady=10)

convert_button = tk.Button(window, text="转换为Word", command=lambda: convert_to_word(input_entry))
convert_button.pack(pady=10)

# 上传文件函数
def upload_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    entry.delete(0, tk.END)
    entry.insert(tk.END, file_path)

# 转换为Word函数
def convert_to_word(entry):
    file_path = entry.get()
    if file_path:
        word_file_path = os.path.splitext(file_path)[0] + ".docx"
        parse(file_path, word_file_path)
        messagebox.showinfo("转换成功", "成功将PDF转换为Word！")
        os.startfile(word_file_path)

window.mainloop()