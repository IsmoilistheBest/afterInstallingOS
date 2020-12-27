from os import system as cmd
from getpass import getuser as user
from sys import stdout as s

def php():
    try:
        if user() == 'root':
            s.write("Installing dependencies...\n")
            cmd("apt install -y software-properties-common; clear")
            s.write("Add new version of PHP...\n")
            cmd("add-apt-repository ppa:ondrej/php; clear")
            s.write("Updating & Installing\n")
            cmd("apt update && apt install -y php8.0 libapache2-mod-php8.0 php8.0-fpm libapache2-mod-fcgid openssl php8.0-common php-curl php-json php8.0-mbstring php8.0-bcmath gettext php8.0-cli; clear")
            s.write("Done!\n")
        else:   print("Run as the root!")
    except Exception as e:
        s.write("Something went wrong...\n")


if __name__ == "__main__":
    php()
