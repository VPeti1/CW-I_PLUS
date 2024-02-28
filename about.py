import tkinter as tk
import time
import subprocess

def close_window():
    root.destroy()
    subprocess.call(['python', 'main.py'])
    quit()

root = tk.Tk()
root.title("Installation Status")

# Create a label with the message
message_label = tk.Label(root, text="CW-I PLUS\n Made by VPeti\n Now with blast processing included")
message_label.pack()

# Schedule the window to close after 2 seconds
root.after(7000, close_window)


root.mainloop()