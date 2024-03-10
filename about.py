import tkinter as tk
import subprocess
import platform

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"


def close_window():
    root.destroy()
    subprocess.call(['python', 'main.py'])
    quit()

root = tk.Tk()
root.title("About")

os = detect_os()
name = ""
if os == "linux":
    message_label = tk.Label(root, text="OpenCW PLUS\n Made by VPeti\n Now with blast processing included")
else:
    message_label = tk.Label(root, text="CW-I PLUS\n Made by VPeti\n Now with blast processing included"

# Create a label with the message
)
message_label.pack()

# Schedule the window to close after 2 seconds
root.after(7000, close_window)


root.mainloop()