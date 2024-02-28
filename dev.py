import tkinter as tk
import subprocess
import os
from tkinter import messagebox

os.system("choco install vlc imgburn notepadplusplus phyton winrar jre8 vscode visualstudio2022community wget msys2 -y")
subprocess.call(['python', 'browserselect.py'])