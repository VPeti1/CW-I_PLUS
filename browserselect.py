import tkinter as tk
import subprocess
import os

def exit_app():
    root.destroy()
    subprocess.call(['python', 'finish.py'])

def open_firefox():
    os.system("choco install firefox -y")
    root.destroy()
    subprocess.call(['python', 'finish.py'])

def open_chrome():
    os.system("choco install googlechrome -y")
    root.destroy()
    subprocess.call(['python', 'finish.py'])


root = tk.Tk()
root.title("Browser Selector")

question_label = tk.Label(root, text="What browser do you want?")
question_label.pack()

firefox_button = tk.Button(root, text="Firefox", command=open_firefox)
firefox_button.pack()

chrome_button = tk.Button(root, text="Chrome", command=open_chrome)
chrome_button.pack()

none_button = tk.Button(root, text="None", command=exit_app)
none_button.pack()

root.mainloop()