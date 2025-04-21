import subprocess
import time
import os
from colorama import Fore, Style

# Clear the screen
os.system("cls" if os.name == "nt" else "clear")

print("Welcome to " + Fore.LIGHTGREEN_EX + " Adr3nalin Software!" + Fore.RESET)
print("This tool was made by fGs.")

# Animated text effect
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

# Jailbreak checker using ideviceinstaller
def check_jailbreak():
    print(Fore.MAGENTA + "[+] Checking for Jailbreak..." + Fore.RESET)

    jailbreak_tools = {
        "Cydia": "Cydia",
        "Sileo": "Sileo",
        "Zebra": "Zebra",
        "Dopamine": "Dopamine",
        "Palera1n": "Palera1n",
        "Checkra1n": "Checkra1n",
        "NekoJB": "NekoJB",
        "unc0ver": "unc0ver",
        "Electra": "Electra",
        "Taurine": "Taurine",
        "Odyssey": "Odyssey",
        "Pangu": "Pangu",
        "Yalu": "Yalu",
        "Checkm8": "Checkm8",
        "RootlessJB": "RootlessJB",
        "Discord": "Discord",
    }

    try:
        result = subprocess.run(["ideviceinstaller", "--list-apps"], capture_output=True, text=True)
        if result.returncode == 0:
            found_tools = []

            for name in jailbreak_tools:
                if name.lower() in result.stdout.lower():
                    found_tools.append(jailbreak_tools[name])

            if found_tools:
                print(Fore.RED + "\n[!] Jailbroken device detected!\n" + Fore.RESET)
                for tool in found_tools:
                    print(Fore.YELLOW + "[+] " + Fore.LIGHTRED_EX + tool + Fore.RESET)
                return True
            else:
                print(Fore.GREEN + "[+] No signs of Jailbreak detected." + Fore.RESET)
                return False
        else:
            print(Fore.RED + "[!] Error checking Jailbreak. The device might not be properly connected." + Fore.RESET)
            return False
    except FileNotFoundError:
        print(Fore.RED + "[!] Error: 'ideviceinstaller' not found. Make sure it's in the script directory or PATH." + Fore.RESET)
        return False

# Embedded libimobiledevice path
LIBIMOBILE_PATH = os.path.join(os.getcwd(), "imobiledevice")
IDEVICEINFO = os.path.join(LIBIMOBILE_PATH, "ideviceinfo.exe")
IDEVICEINSTALLER = os.path.join(LIBIMOBILE_PATH, "ideviceinstaller.exe")
IDEVICEID = os.path.join(LIBIMOBILE_PATH, "idevice_id.exe")
IDEVICEBACKUP = os.path.join(LIBIMOBILE_PATH, "idevicebackup2.exe")

# Relevant fields to display
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

# Check if device is connected
def get_device_info():
    try:
        result = subprocess.run([IDEVICEINFO], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return None
    except FileNotFoundError:
        print(Fore.RED + "\nError: 'ideviceinfo.exe' not found.\nPlace the 'imobiledevice' folder next to this script." + Fore.RESET)
        return None

# Display basic info
def display_relevant_info(device_info):
    print(Fore.CYAN + "\n[+] Basic Information:" + Fore.RESET)
    for field in RELEVANT_FIELDS:
        for line in device_info.splitlines():
            if line.startswith(field):
                print(Fore.LIGHTGREEN_EX + f"[+] {line}" + Fore.RESET)

    print(Fore.CYAN + "\n[+] Extra Information:" + Fore.RESET)
    for field in EXTRA_FIELDS:
        for line in device_info.splitlines():
            if line.startswith(field):
                print(Fore.LIGHTBLUE_EX + f"[+] {line}" + Fore.RESET)

# List installed apps
def list_installed_apps():
    try:
        result = subprocess.run([IDEVICEINSTALLER, "-l"], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "\n[+] Installed apps:" + Fore.RESET)
            print(result.stdout)
        else:
            print(Fore.RED + "Error listing installed apps." + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + "\nError: 'ideviceinstaller.exe' not found." + Fore.RESET)

# Perform device backup
def backup_device():
    try:
        print(Fore.YELLOW + "\nStarting backup..." + Fore.RESET)
        result = subprocess.run([IDEVICEBACKUP, "backup", "backups/"], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "[+] Backup completed successfully!" + Fore.RESET)
        else:
            print(Fore.RED + "Error performing backup." + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + "\nError: 'idevicebackup2.exe' not found." + Fore.RESET)

# Display device UUID
def display_uuid():
    try:
        result = subprocess.run([IDEVICEID, "-l"], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "\n[+] Device UUID:" + Fore.RESET)
            print(Fore.LIGHTCYAN_EX + result.stdout + Fore.RESET)
        else:
            print(Fore.RED + "Error retrieving UUID." + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + "\nError: 'idevice_id.exe' not found." + Fore.RESET)

# Monitor connection status in real time
def monitor_connection():
    last_status = None
    device_connected = False
    while True:
        device_info = get_device_info()
        if device_info:
            status = Fore.GREEN + "[+] Device Connected" + Fore.RESET
            device_connected = True
        else:
            status = Fore.RED + "[!] No device connected" + Fore.RESET
            device_connected = False

        if status != last_status:
            last_status = status
            os.system("cls" if os.name == "nt" else "clear")
            print(status)

        if device_connected:
            menu()

        time.sleep(1)

# Show menu
def show_menu():
    print(Fore.GREEN + "\n[+] Main Menu:" + Fore.RESET)
    print(Fore.CYAN + "[1] Show ALL device info" + Fore.RESET)
    print(Fore.CYAN + "[2] Show basic info" + Fore.RESET)
    print(Fore.CYAN + "[3] Show device UUID" + Fore.RESET)
    print(Fore.CYAN + "[4] List installed apps" + Fore.RESET)
    print(Fore.CYAN + "[5] Backup device" + Fore.RESET)
    print(Fore.CYAN + "[6] Check Jailbreak" + Fore.RESET)
    print(Fore.RED + "[7] Exit" + Fore.RESET)

# Menu controller
def menu():
    while True:
        show_menu()
        choice = input(Fore.YELLOW + "\nChoose an option: " + Fore.RESET)

        if choice == "1":
            device_info = get_device_info()
            if device_info:
                print(Fore.RESET + "Device Info:\n" + device_info)
                time.sleep(5)
                os.system("cls" if os.name == "nt" else "clear")
        elif choice == "2":
            device_info = get_device_info()
            if device_info:
                display_relevant_info(device_info)
                time.sleep(5)
                os.system("cls" if os.name == "nt" else "clear")
        elif choice == "3":
            display_uuid()
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "4":
            list_installed_apps()
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "5":
            backup_device()
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "6":
            check_jailbreak()
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "7":
            print(Fore.RED + "Exiting... See you!" + Fore.RESET)
            break
        else:
            print(Fore.RED + "Invalid option, please try again." + Fore.RESET)

# Start connection monitoring
if __name__ == "__main__":
    monitor_connection()