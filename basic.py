import tkinter as tk
import subprocess
import os
from tkinter import messagebox

def ask_question():
    result = messagebox.askyesno("Question", "Do want libreoffice?")
    if result:
        root.destroy()
        os.system("choco install vlc imgburn notepadplusplus phyton winrar jre8 libreoffice-fresh -y")
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

# Ask the QUESTION
ask_question()


# Start the Tkinter event loop
root.mainloop()
