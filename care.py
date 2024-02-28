import tkinter as tk
import subprocess
import os
from tkinter import messagebox

os.system("choco install wget -y");
os.system("md C:\CW");
os.system("wget https://raw.githubusercontent.com/VPeti1/CWAcces/main/CWCare-I.bat -O C:\CW\care.bat")
os.system("cmd /c C:\CW\care.bat")
subprocess.call(['python', 'finish.py'])