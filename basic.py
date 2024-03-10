import tkinter as tk
import subprocess
import os
from tkinter import messagebox
import platform

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "linux"
    else:
        return "windows"

def ask_question():
    result = messagebox.askyesno("Question", "Do want libreoffice?")
    if result:
        libre()
    else:
       nolibre()

def libre():
    sys = detect_os()
    if sys == "linux":
        root.destroy()
        os.system("flatpak install org.videolan.VLC io.github.peazip.PeaZip org.libreoffice.LibreOffice -y")
        subprocess.call(['python', 'browserselect.py'])
    else:
        root.destroy()
        os.system("choco install vlc imgburn notepadplusplus phyton winrar jre8 libreoffice-fresh -y")
        subprocess.call(['python', 'browserselect.py'])

def nolibre():
    sys = detect_os()
    if sys == "linux":
        root.destroy()
        os.system("flatpak install org.videolan.VLC io.github.peazip.PeaZip -y")
        subprocess.call(['python', 'browserselect.py'])
    else:
        root.destroy()
        os.system("choco install vlc imgburn notepadplusplus phyton winrar jre8 -y")
        subprocess.call(['python', 'browserselect.py'])

# Create the main application window
root = tk.Tk()
root.title("LibreOffice")

# ANSWER THE GODDAM QUESTION
text_box = tk.Text(root, height=1, width=40)
text_box.pack()
initial_text = "          Answer the question!"
text_box.insert(tk.END, initial_text)
root.destroy()

# Ask the QUESTION
ask_question()


# Start the Tkinter event loop
root.mainloop()
