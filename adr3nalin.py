import subprocess
import time
import os
import colorama
from colorama import Fore, Back, Style
from os import system

os.system("cls" if os.name == "nt" else "clear")
print("Welcome to Adr3nalin Software!")
print("This tool was made by fGs.")

# Função para exibir texto gradualmente
def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Quebra de linha ao final

# Desenho ASCII
ascii_art = r"""
                           /|      __  
                          / |   ,-~ /  
                         Y :|  //  /    
                         | jj /( .^  
                         >-"~"-v"  
                        /       Y    
                       jo  o    |  
                      ( ~T~     j   
                       >._-' _./   
                      /   "~"  |    
                     Y     _,  |      
                    /| ;-"~ _  l    
                   / l/ ,-"~    \  
                   \//\/      .- \  
                    Y        /    Y*  
                    l       I     ! 
                    ]\      _\    /"\ 
                   (" ~----( ~   Y.  )
"""

# Exibir o desenho com o efeito de digitação
typewriter_effect(ascii_art, delay=0.003)
time.sleep(0.2)
print(Fore.GREEN + "Loading...")
time.sleep(2)
print(Fore.RESET)
os.system("cls" if os.name == "nt" else "clear")
print("" + Fore.RED + "Please connect the device by USB Cable..." + Fore.RESET)

# Função para verificar se o dispositivo está conectado
def get_device_info():
    try:
        result = subprocess.run(["ideviceinfo"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return None
    except FileNotFoundError:
        print("You need to install libimobiledevice to use this script.")
        print("https://github.com/libimobiledevice-win32/libimobiledevice/releases/tag/v1.3.17")
        return None

# Loop para aguardar a conexão do dispositivo
timeout = 120  # 2 minutos
start_time = time.time()

while time.time() - start_time < timeout:
    device_info = get_device_info()
    if device_info:
        print(Fore.GREEN + "Device Found!")
        print(device_info)
        break
    else:
        print(Fore.YELLOW + "Waiting for device connection..." + Fore.RESET, end="\r")
        time.sleep(5)  # Espera 5 segundos antes de tentar novamente

else:
    print(Fore.RED + "\nTimeout: No device connected within 2 minutes." + Fore.RESET)