# -*- coding: utf-8 -*-

import tkinter as tk
import os
import subprocess

def open_console():
    # �������� ���� � ����������, ��� ��������� ����
    current_directory = os.path.dirname(os.path.abspath(__file__))

    if os.name == 'nt':  # ���� �� Windows
        subprocess.Popen(['cmd.exe', '/K', f'cd {current_directory}'])
    else:  # ��� Unix-�������� ������ (Linux, macOS)
        subprocess.Popen(['gnome-terminal', '--working-directory', current_directory])

def change_font():
    global current_font_index
    current_font_index = (current_font_index + 1) % len(fonts)
    label.config(font=fonts[current_font_index])

# �������� �������� ����
root = tk.Tk()
root.title("quest 1")

# ��������� ������ ����
root.geometry("552x228")  # ������������� ��������� ������ ����
root.resizable(True, False)  # ��������� ��������� ������� ����

# ������ �������
fonts = [
    ("Helvetica", 16),
    ("Arial", 20),
    ("Times New Roman", 24),
    ("Courier New", 18),
    ("Comic Sans MS", 22),
]

current_font_index = 0
label = tk.Label(root, text="Dont compare yourself with anyone in this world...\n"
        "if you do so, you are insulting yourself.", font=fonts[current_font_index])
label.pack(pady=20)

button = tk.Button(root, text="change", command=change_font)
button.pack(pady=10)

console_button = tk.Button(root, text="open cmd", command=open_console)
console_button.pack(pady=10)


# ������ ��������� �����
root.mainloop()

