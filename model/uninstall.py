#!/usr/bin/python3
"""Uninstaller module"""
from systemSetup import detect_system

import os
from colorama import Fore

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
        print(Fore.CYAN + "\n\n")
        print(Fore.YELLOW + "                             ----------------------------------------------------------------")
        print("                                  " + Fore.CYAN + " ____   _   _   ____   ____  __   __       _   ____ ")
        print("                                  " + Fore.CYAN + "/ __ \\ | | | | / __ \\ |  __| \\ \_/ /      | | |  __ \ ")
        print("                                 " + Fore.CYAN + "| |  | || | | || |__| || |     \\___/       | | | |__| |")
        print("                                 " + Fore.CYAN + "| |  | || | | ||  ____|| |      | |" + Fore.YELLOW + "   ~~" + Fore.CYAN + "   | | |  ____| ")
        print("                                 " + Fore.CYAN + "| |__| |\ \_/ /| |____ | |      | |        | | | |")
        print("                                  " + Fore.CYAN + "\\___\\ \\ \\___/  \\_____||_|      |_|        |_| |_|")
        print("                                  " + Fore.CYAN + "     \\_\\")
        print(Fore.YELLOW + "                             ----------------------------------------------------------------")
        print("                                  " + Fore.CYAN + "-------------------------------------------------------")
        print("                                  " + Fore.CYAN + "------------------" + Fore.YELLOW +  "<Query your IP address>" + Fore.CYAN +   "--------------")
        print("                                  " + Fore.CYAN + "------------------------------------------------")
        print("\n\n")

        if os.path.exists("/usr/bin/query") or os.path.exists("/data/data/com.termux/files/usr/bin/query"):
            print("Sorry Query-IP couldn't uninstall!")
        else:
            print("Query-IP unistalled succussfully!")

uninstall = Uninstaller()
uninstall.uninstaller()
uninstall.display_logo()