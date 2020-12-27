from getpass import getuser
from os import system, chdir
from sys import stdout

# installing wifi
def wifi():
    try:
        if getuser() == 'root':
            system("clear")
            print("Configuring extentions...\n")
            system("apt update; apt upgrade; apt install -y bc dkms module-assistant build-essential git")
            system("clear")
            stdout.write("Downloading Wifi Driver...\n")
            system("git clone https://github.com/tomaspinho/rtl8821ce.git")
            chdir("rtl8821ce")
            system("./dkms-install.sh; clear")
            stdout.write("Done!\nAfter this reboot system!!!\n")
        else:
            stdout.write("Run as root\n")
    except Exception as e:
        stdout.write("Something went wrong...\n")

if __name__ == "__main__":
    wifi()
