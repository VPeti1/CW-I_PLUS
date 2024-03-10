import subprocess
import os
import platform


os_name = platform.system()
if os_name == "Linux":
    os.system("flatpak install org.videolan.VLC  com.visualstudio.code io.github.shiftey.Desktop io.github.peazip.PeaZip -y")
    subprocess.call(['python', 'browserselect.py'])
else:
    os.system("choco install vlc imgburn notepadplusplus phyton winrar jre8 vscode visualstudio2022community wget msys2 -y")
    subprocess.call(['python', 'browserselect.py'])

