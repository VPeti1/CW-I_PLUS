import tkinter as tk
import subprocess
import os
from tkinter import messagebox




def basic():
    result = messagebox.askyesno("Question","Do you want to continue?")
    if result:
        subprocess.call(['python', 'basic.py'])
        
        
    else:
        quit()
    
def gamer():
    result = messagebox.askyesno("Question","Do you want to continue?")
    if result:
        subprocess.call(['python', 'gamer.py'])
    else:
        quit()

def dev():
    result = messagebox.askyesno("Question","Do you want to continue?")
    if result:
        subprocess.call(['python', 'dev.py'])
    else:
        quit()

def debloat():
    result = messagebox.askyesno("Question","Do you want to continue?")
    if result:
        subprocess.call(['python', 'deb.py'])
    else:
        quit()

def care():
    result = messagebox.askyesno("Question","Do you want to continue?")
    if result:
        subprocess.call(['python', 'care.py'])
    else:
        quit()

def about():
    subprocess.call(['python', 'about.py'])

def Exit():
    quit()

def create_gui():
    subprocess.run('chococ.exe', shell=True)
    subprocess.call(['python', 'splash.py'])
    root = tk.Tk()
    root.title("CW-I PLUS")

    ## Adds textbox
    text_box = tk.Text(root, height=2, width=40)
    text_box.pack()
    initial_text = "        Welcome to CW-I PLUS! \n        Choose an install type"
    text_box.insert(tk.END, initial_text)

    ## Dark mode button
    

    # Creates buttons
    button1 = tk.Button(root, text="Basic", command=lambda: [root.destroy(),basic()])
    button2 = tk.Button(root, text="Gamer", command=lambda: [root.destroy(),gamer()])
    button3 = tk.Button(root, text="Developer", command=lambda: [root.destroy(),dev()])
    button4 = tk.Button(root, text="About", command=lambda: [root.destroy(),about()])
    button6 = tk.Button(root, text="Debloat", command=lambda: [root.destroy(),debloat()])
    button7 = tk.Button(root, text="Care", command=lambda: [root.destroy(),care()])
    button8 = tk.Button(root, text="Exit", command=lambda: [root.destroy(),exit()])

    # Pack buttons into the window
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button6.pack()
    button7.pack()
    button8.pack()


    root.mainloop()


if __name__ == "__main__":
    create_gui()
