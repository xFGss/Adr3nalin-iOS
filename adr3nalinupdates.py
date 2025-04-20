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

# Verificar se o dispositivo tem jailbreak usando ideviceinstaller
def check_jailbreak():
    print(Fore.MAGENTA + "[+] Verificando Jailbreak..." + Fore.RESET)
    
    # Verificar por Cydia ou Sileo usando ideviceinstaller
    try:
        result = subprocess.run(["ideviceinstaller", "--list-apps"], capture_output=True, text=True)
        if result.returncode == 0:
            # Verificar se Cydia ou Sileo estão na lista de aplicativos instalados
            if "Cydia" in result.stdout or "Sileo" in result.stdout:
                print(Fore.RED + "[!] Cydia ou Sileo encontrado! Dispositivo com Jailbreak." + Fore.RESET)
                return True
            else:
                print(Fore.GREEN + "[+] Nenhum sinal de Jailbreak detectado." + Fore.RESET)
                return False
        else:
            print(Fore.RED + "[!] Erro ao verificar Jailbreak. O dispositivo pode não estar corretamente conectado." + Fore.RESET)
            return False
    except FileNotFoundError:
        print(Fore.RED + "[!] Erro ao executar ideviceinstaller. Certifique-se de que a ferramenta está instalada." + Fore.RESET)
        return False

# Caminho para libimobiledevice embutido
LIBIMOBILE_PATH = os.path.join(os.getcwd(), "imobiledevice")
IDEVICEINFO = os.path.join(LIBIMOBILE_PATH, "ideviceinfo.exe")
IDEVICEINSTALLER = os.path.join(LIBIMOBILE_PATH, "ideviceinstaller.exe")
IDEVICEID = os.path.join(LIBIMOBILE_PATH, "idevice_id.exe")
IDEVICEBACKUP = os.path.join(LIBIMOBILE_PATH, "idevicebackup2.exe")

# Campos principais que queremos mostrar
RELEVANT_FIELDS = [
    "DeviceName",
    "ProductName",
    "ProductType",
    "ProductVersion"
]

EXTRA_FIELDS = [
    "ModelNumber",
    "SerialNumber",
    "PasswordProtected"
]

# Função para verificar se o dispositivo está conectado
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

# Mostrar informações simplificadas
def display_relevant_info(device_info):
    print(Fore.CYAN + "\n[+] Informações principais:" + Fore.RESET)
    for field in RELEVANT_FIELDS:
        for line in device_info.splitlines():
            if line.startswith(field):
                print(Fore.LIGHTGREEN_EX + f"[+] {line}" + Fore.RESET)

    print(Fore.CYAN + "\n[+] Outras informações:" + Fore.RESET)
    for field in EXTRA_FIELDS:
        for line in device_info.splitlines():
            if line.startswith(field):
                print(Fore.LIGHTBLUE_EX + f"[+] {line}" + Fore.RESET)

# Função para listar apps instaladas
def list_installed_apps():
    try:
        result = subprocess.run([IDEVICEINSTALLER, "-l"], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "\n[+] Apps instaladas no dispositivo:" + Fore.RESET)
            print(result.stdout)
        else:
            print(Fore.RED + "Erro ao listar apps instaladas." + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + "\nErro: 'ideviceinstaller.exe' não encontrado." + Fore.RESET)

# Função para fazer backup
def backup_device():
    try:
        print(Fore.YELLOW + "\nIniciando backup..." + Fore.RESET)
        result = subprocess.run([IDEVICEBACKUP, "backup", "backups/"], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "[+] Backup concluído com sucesso!" + Fore.RESET)
        else:
            print(Fore.RED + "Erro ao realizar backup." + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + "\nErro: 'idevicebackup2.exe' não encontrado." + Fore.RESET)

# Função para ver UUID
def display_uuid():
    try:
        result = subprocess.run([IDEVICEID, "-l"], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "\n[+] UUID do dispositivo:" + Fore.RESET)
            print(Fore.LIGHTCYAN_EX + result.stdout + Fore.RESET)
        else:
            print(Fore.RED + "Erro ao obter UUID." + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + "\nErro: 'idevice_id.exe' não encontrado." + Fore.RESET)

# Função para monitorar status da conexão em tempo real
def monitor_connection():
    last_status = None
    device_connected = False  # Estado de conexão
    while True:
        device_info = get_device_info()
        if device_info:
            status = Fore.GREEN + "[+] Dispositivo Conectado" + Fore.RESET
            device_connected = True
        else:
            status = Fore.RED + "[!] Nenhum dispositivo conectado" + Fore.RESET
            device_connected = False

        # Atualiza a tela apenas quando há alteração no status de conexão
        if status != last_status:
            last_status = status
            os.system("cls" if os.name == "nt" else "clear")
            print(status)

        # Se o dispositivo for conectado, mostra o menu
        if device_connected:
            menu()  # Só chama o menu quando o dispositivo for detectado

        time.sleep(1)

# Função para mostrar o menu
def show_menu():
    print(Fore.GREEN + "\n[+] Menu de Opções:" + Fore.RESET)
    print(Fore.CYAN + "[1] Ver TODAS as informações" + Fore.RESET)
    print(Fore.CYAN + "[2] Ver informações principais" + Fore.RESET)
    print(Fore.CYAN + "[3] Ver UUID do dispositivo" + Fore.RESET)
    print(Fore.CYAN + "[4] Ver lista de apps instaladas" + Fore.RESET)
    print(Fore.CYAN + "[5] Fazer backup" + Fore.RESET)
    print(Fore.YELLOW + "[6] Verificar Jailbreak" + Fore.RESET)  # Nova opção no menu
    print(Fore.RED + "[7] Sair" + Fore.RESET)

# Função para controlar o loop do menu
def menu():
    while True:
        show_menu()
        choice = input(Fore.YELLOW + "Escolha uma opção: " + Fore.RESET)

        if choice == "1":
                device_info = get_device_info()
                if device_info:
                    print(Fore.RESET + "Device Info:\n" + device_info)
                    time.sleep(5)  # Exibir informações por 5 segundos
                    os.system("cls" if os.name == "nt" else "clear")  # Limpar a tela e voltar ao menu
        elif choice == "2":
                device_info = get_device_info()
                if device_info:
                    display_relevant_info(device_info)
                    time.sleep(5)  # Exibir informações por 5 segundos
                    os.system("cls" if os.name == "nt" else "clear")  # Limpar a tela e voltar ao menu
        elif choice == "3":
                display_uuid()
                time.sleep(5)  # Exibir informações por 5 segundos
                os.system("cls" if os.name == "nt" else "clear")  # Limpar a tela e voltar ao menu
        elif choice == "4":
                list_installed_apps()
                time.sleep(5)  # Exibir informações por 5 segundos
                os.system("cls" if os.name == "nt" else "clear")  # Limpar a tela e voltar ao menu
        elif choice == "5":
                backup_device()
                time.sleep(5)  # Exibir informações por 5 segundos
                os.system("cls" if os.name == "nt" else "clear")  # Limpar a tela e voltar ao menu
        elif choice == "6":
                print(Fore.MAGENTA + "[+] Verificando Jailbreak..." + Fore.RESET)
                check_jailbreak()
                time.sleep(5)  # Exibir a verificação de jailbreak por 5 segundos
                os.system("cls" if os.name == "nt" else "clear")  # Limpar a tela e voltar ao menu
        elif choice == "7":
                print(Fore.RED + "Saindo... Até mais!" + Fore.RESET)
                break
        else:
                print(Fore.RED + "Opção inválida, tente novamente" + Fore.RESET)

# Inicia o monitoramento da conexão e menu
if __name__ == "__main__":
    monitor_connection()
