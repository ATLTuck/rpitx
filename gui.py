import tkinter as tk
from tkinter import filedialog
import subprocess

def transmit_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        subprocess.run(["rpitx", "-i", file_path])

def transmit_text():
    text = text_entry.get("1.0", "end-1c")
    if text:
        subprocess.run(["rpitx", "-m", text])

root = tk.Tk()
root.title("RPiTX GUI")

# Transmit File Button
file_button = tk.Button(root, text="Transmit File", command=transmit_file)
file_button.pack()

# Transmit Text Entry
text_entry = tk.Text(root, height=5, width=30)
text_entry.pack()

# Transmit Text Button
text_button = tk.Button(root, text="Transmit Text", command=transmit_text)
text_button.pack()

root.mainloop()
