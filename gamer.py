import subprocess
import os
import platform


os_name = platform.system()
if os_name == "Linux":
    os.system("flatpak install org.videolan.VLC  com.valvesoftware.Steam com.discordapp.Discord io.github.peazip.peazip -y")
    subprocess.call(['python', 'browserselect.py'])
else:
    os.system("choco install vlc notepadplusplus phyton winrar jre8 steam epicgameslaucher discord -y")
    subprocess.call(['python', 'browserselect.py'])


