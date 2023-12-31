#!/usr/bin/python3
"""setup module"""
import os
import colorama
from colorama import Fore
from model.systemSetup import detect_system

class setUp():
    """An setup class"""
    def set_up(self):
    # Removing old files
        system = detect_system()
        if system == "ubuntu":
            os.system("sudo rm -rf /usr/bin/query_ip /usr/bin/query /usr/share/Query-IP")
        elif system == "termux":
            os.system("rm -rf /data/data/com.termux/files/usr/share/Query-IP /data/data/com.termux/files/usr/bin/query /data/data/com.termux/files/usr/bin/query_ip")
        else:
            os.system("sudo rm -rf /usr/bin/query /usr/bin/query_ip /usr/share/Query-IP")
    
        # Adding bin file
        if system == "ubuntu":
            os.system("sudo mv -v model/query_ip /usr/bin/")
            os.system("sudo mv -v model/query /usr/bin/")
            os.system("sudo chmod +x /usr/bin/query /usr/bin/query_ip")
        elif system == "termux":
            os.system("mv -v model/query_ip /data/data/com.termux/files/usr/bin/")
            os.system("mv -v model/query /data/data/com.termux/files/usr/bin/")
            os.system("chmod +x /data/data/com.termux/files/usr/bin/query_ip /data/data/com.termux/files/usr/bin/query")
        else:
            os.system("mv -v model/query_ip /usr/bin/")
            os.system("mv -v model/query /usr/bin/")
            os.system("chmod +x /usr/bin/query_ip /usr/bin/query")
    
        # Copy files from Query-IP to target directory
        if system == "ubuntu":
            os.system("sudo mkdir /usr/share/Query-IP/")
            os.system("chmod +x * *.* .*.*")
            os.system("sudo mv -v * *.* .*.* /usr/share/Query-IP/")
        elif system == "termux":
            os.system("mkdir /data/data/com.termux/files/usr/share/Query-IP")
            os.system("chmod +x * *.* .*.*")
            os.system("mv -v * *.* .*.* /data/data/com.termux/files/usr/share/Query-IP/")
        else:
            os.system("mkdir /usr/share/Query-IP")
            os.system("chmod +x * *.* .*.*")
            os.system("mv -v * *.* .*.* /usr/share/Query-IP/")
    
        # Removing Query-IP directory
        os.system("cd .. && rm -rf Query-IP")

    def center_text(text):
        terminal_width = os.get_terminal_size().columns
        centered_text = text.center(terminal_width)
        return centered_text
    
    def logo(self):
        os.system("clear")
        logo_lines = [
        Fore.CYAN + "\n\n",
        Fore.YELLOW + "    ----------------------------------------------------------------",
        Fore.CYAN + "    " + " ____   _   _   ____   ____  __   __       _   ____ ",
        Fore.CYAN + "     " + "/ __ \\ | | | | / __ \\ |  __| \\ \_/ /      | | |  __ \ ",
        Fore.CYAN + "     " + "| |  | || | | || |__| || |     \\___/       | | | |__| |",
        Fore.CYAN + "                " + "| |  | || | | ||  ____|| |      | |" + Fore.YELLOW + "   ~~" + Fore.CYAN + "   | | |  ____| ",
        Fore.CYAN +  "" + "| |__| |\ \_/ /| |____ | |      | |        | | | |",
        Fore.CYAN +  " " + "\\___\\ \\ \\___/  \\_____||_|      |_|        |_| |_|",
        Fore.YELLOW + "    ----------------------------------------------------------------",
        Fore.CYAN +  "             " +  "----------" + Fore.YELLOW +  "A more intuitive way to lookup your IP adresses" + Fore.CYAN +   "-------------",
        Fore.CYAN + "                " +  "---------------" + Fore.YELLOW +  "<Query your IP address>" + Fore.CYAN +   "-------------------",
        Fore.CYAN + "                " +  "---------------" + Fore.YELLOW +  "Tool Name"  + "    " + Fore.CYAN + "Query-IP ----------------",
        Fore.CYAN + "                 " +  "---------------" + Fore.YELLOW +  "Author"  + "    " + Fore.CYAN + "David Gregs ---------------",
        Fore.CYAN + "                " +  "--------------" + Fore.YELLOW +  "Project"  + "    " + Fore.CYAN + "@alx Portfolio Project ----",
        "\n\n",
        ]
        centered_logo = "\n".join(setUp.center_text(line) for line in logo_lines)
        print(centered_logo)

        if os.path.exists("/usr/bin/query") or os.path.exists("/data/data/com.termux/files/usr/bin/query"):
            logo_line = [
            Fore.YELLOW + "Query-IP successfully installed!\n",
            Fore.YELLOW + "Help/Usage",
            Fore.YELLOW + "_________________________________________________________________",
            Fore.YELLOW + "                     |" + Fore.CYAN + "           Command" + Fore.YELLOW + "        |" + Fore.CYAN + "           Use" + Fore.YELLOW + "                        |",      
            Fore.YELLOW + "|__________________________|______________________________________|",
            Fore.YELLOW + "                     |" + Fore.CYAN + "      Query -m" + Fore.YELLOW + "     |" + Fore.CYAN + "  Query the IP address of the local machine" + Fore.YELLOW + "  |", 
            Fore.YELLOW + "|___________________|_____________________________________________|",
            Fore.YELLOW + "                     |" + Fore.CYAN + "         Query -t <target_ip>" + Fore.YELLOW + "  |" + Fore.CYAN + " Query the IP of a target machine" + Fore.YELLOW + "|",
            Fore.YELLOW + "|_______________________________|_________________________________|",
            Fore.YELLOW + "                     |" + Fore.CYAN + "         Query --help" + Fore.YELLOW + "     |" + Fore.CYAN + "     Quick help" + Fore.YELLOW + "                       |",
            Fore.YELLOW + " |__________________________|______________________________________|\n",
            Fore.YELLOW + "Note: Dont try to make query for over 150 times, you could get banned",
            ]
            centered_logo = "\n".join(setUp.center_text(line) for line in logo_line)
            print(centered_logo)       
        else:
            lines = [
            Fore.RED + "Sorry Query-IP could not be installed",
            ]
            centered_logo = "\n".join(setUp.center_text(line) for line in lines)
            print(centered_logo)
    



setUP = setUp()
setUP.set_up()
setUP.logo()
