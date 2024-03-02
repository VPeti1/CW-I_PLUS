import os


# Define the path to check
file_path = r"C:\ProgramData\chocolatey\bin\choco.exe"

# Check if the file exists
if os.path.exists(file_path):
    print("Choco found")
else:
    powershell_command = r'''
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    '''
    os.system(f'powershell -Command "{powershell_command}"')

    



