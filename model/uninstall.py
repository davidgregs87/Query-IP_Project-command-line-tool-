#!/usr/bin/python3
"""Uninstaller module"""
from systemSetup import detect_system

import os
from colorama import Fore
from model.center import center_text

class Uninstaller():
    """An uninstaller class"""
    def uninstaller(self):
        if detect_system() == "ubuntu":
            os.system("sudo rm -rf /usr/bin/query_ip")
            os.system("sudo rm -rf /usr/bin/query")
            os.system("sudo rm -rf /usr/share/Query-IP")
        elif detect_system() == "termux":
            os.system("rm -rf /data/data/com.termux/files/usr/share/Query-IP")
            os.system("rm -rf /data/data/com.termux/files/usr/bin/query_ip")
            os.system("rm -rf /data/data/com.termux/files/usr/bin/query")
        elif detect_system() == "windows":
            os.system("wmic product where name='Query-IP' call uninstall")
            os.system("wmic product where name='query-ip' call uninstall")
            os.system("wmic product where name='query' call uninstall")
        elif detect_system() == 'macOS':
            os.system("sudo rm -rf /usr/bin/query_ip")
            os.system("sudo rm -rf /usr/bin/query")
            os.system("sudo rm -rf /usr/share/Query-IP")
    def display_logo(self):
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
        centered_logo = "\n".join(center_text(line) for line in logo_lines)
        print(centered_logo)

        if os.path.exists("/usr/bin/query") or os.path.exists("/data/data/com.termux/files/usr/bin/query"):
            print(Fore.RED + "Sorry Query-IP couldn't uninstall!")
        else:
            print(Fore.YELLOW + "Query-IP unistalled succussfully!")

uninstall = Uninstaller()
uninstall.uninstaller()
uninstall.display_logo()