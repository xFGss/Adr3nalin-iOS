import subprocess
import time
import os
from colorama import Fore, Style

# Limpa o ecrã
os.system("cls" if os.name == "nt" else "clear")

print("Welcome to Adr3nalin Software!")
print("This tool was made by fGs.")

# Texto animado
def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ASCII ART
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

typewriter_effect(ascii_art, delay=0.003)
time.sleep(0.2)
print(Fore.GREEN + "Loading...")
time.sleep(2)
print(Fore.RESET)
os.system("cls" if os.name == "nt" else "clear")
print(Fore.RED + "Please connect the device by USB Cable..." + Fore.RESET)

# Caminho para libimobiledevice embutido
LIBIMOBILE_PATH = os.path.join(os.getcwd(), "imobiledevice")
IDEVICEINFO = os.path.join(LIBIMOBILE_PATH, "ideviceinfo.exe")

# Obtém a info do dispositivo
def get_device_info():
    try:
        result = subprocess.run([IDEVICEINFO], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return None
    except FileNotFoundError:
        print(Fore.RED + "\nErro: 'ideviceinfo.exe' não encontrado.\nColoca a pasta 'imobiledevice' na mesma pasta que este script." + Fore.RESET)
        return None

# Mostra apenas info simplificada
def display_relevant_info(device_info):
    main_fields = [
        "DeviceName",
        "ProductName",
        "ProductType",
        "ProductVersion"
    ]
    
    extra_fields = [
        "ModelNumber",
        "SerialNumber",
        "PasswordProtected"
    ]

    print(Fore.CYAN + "\n[+] Informações principais:" + Fore.RESET)
    for field in main_fields:
        for line in device_info.splitlines():
            if line.startswith(field):
                print(Fore.LIGHTGREEN_EX + f"[+] {line}" + Fore.RESET)

    print(Fore.CYAN + "\n[+] Outras informações:" + Fore.RESET)
    for field in extra_fields:
        for line in device_info.splitlines():
            if line.startswith(field):
                print(Fore.LIGHTBLUE_EX + f"[+] {line}" + Fore.RESET)


# Espera até o iPhone ser ligado
timeout = 120
start_time = time.time()

while time.time() - start_time < timeout:
    device_info = get_device_info()
    if device_info:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + "Device Found!")
        print(Fore.YELLOW + "[1] - ALL INFO\n[2] - MAIN INFO" + Fore.RESET)
        choice = input(Fore.YELLOW + "-> " + Fore.RESET)
        if choice == "1":
            print(Fore.RESET + "Device Info:\n" + device_info)
        elif choice == "2":
            display_relevant_info(device_info)
        else:
            print(Fore.RED + "Opção inválida. A sair..." + Fore.RESET)
        break
    else:
        print(Fore.YELLOW + "Waiting for device connection..." + Fore.RESET, end="\r")
        time.sleep(5)
else:
    print(Fore.RED + "\nTimeout: No device connected within 2 minutes." + Fore.RESET)

time.sleep(60)
