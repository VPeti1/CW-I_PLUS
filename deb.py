import tkinter as tk
import subprocess
import os
from tkinter import messagebox

os.system("md C:\CW")
os.system("choco install wget -y")
os.system("wget https://raw.githubusercontent.com/VPeti1/CWAcces/main/deb.ps1 -O C:\CW\CWI.ps1")
os.system("powershell C:\CW\CWI.ps1")
subprocess.call(['python', 'finish.py'])