import tkinter as tk
import subprocess
import os
import platform

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"


def exit_app():
    root.destroy()
    subprocess.call(['python', 'finish.py'])

def open_firefox():
    sys = detect_os()
    if sys == "linux":
        os.system("flatpak install org.mozilla.firefox -y")
        root.destroy()
        subprocess.call(['python', 'finish.py'])
    else:
        os.system("choco install firefox -y")
        root.destroy()
        subprocess.call(['python', 'finish.py'])
    

def open_chrome():
    sys = detect_os()
    if sys == "linux":
        os.system("flatpak install com.google.chrome -y")
        root.destroy()
        subprocess.call(['python', 'finish.py'])
    else:
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