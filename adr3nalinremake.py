import subprocess
import os
from colorama import Fore, Style

# Diretório onde está o libimobiledevice embutido
LIBIMOBILE_PATH = os.path.join(os.getcwd(), "libimobiledevice")
IDEVICEINFO = os.path.join(LIBIMOBILE_PATH, "ideviceinfo.exe")

def print_intro():
    print(Fore.MAGENTA + r"""
         /\_/\
        ( o.o )  Adr3nalin iOS Tool
         > ^ <   by Gonçalo
    """ + Fore.RESET)
    print(Fore.CYAN + "Modo autônomo com libimobiledevice embutido!" + Fore.RESET)
    print(Fore.YELLOW + "Certifique-se de que o iPhone está conectado e desbloqueado." + Fore.RESET)

def get_device_info():
    try:
        # Chama o ideviceinfo.exe sem depender de PATH
        result = subprocess.run([IDEVICEINFO, "-s"], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(Fore.RED + "Erro ao executar ideviceinfo:" + Fore.RESET)
            print(result.stderr)
            return
        
        print(Fore.GREEN + "Informações do dispositivo:\n" + Fore.RESET + result.stdout)
    
    except FileNotFoundError:
        print(Fore.RED + "Erro: 'ideviceinfo.exe' não foi encontrado. Verifique se a pasta 'libimobiledevice' está na mesma pasta que este script." + Fore.RESET)

def main():
    print_intro()
    get_device_info()

if __name__ == "__main__":
    main()
