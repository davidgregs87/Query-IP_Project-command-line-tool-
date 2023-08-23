#!/usr/bin/python3
"""A module for updating our tool(Query-IP)"""
import os
from colorama import Fore
import time

def get_logo():
    """Pulling up our logo"""
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

def update():
    """A function that will help us in updating our tool when there is update"""
    get_logo()
    print(Fore.CYAN + "                             ----------------------" + Fore.YELLOW + "Updating Query-IP...." + Fore.CYAN + "------------------")
    time.sleep(1)
    os.system("cd ~/ && git clone https://github.com/davidgregs87/Query-IP_Project.git")
    os.system("cd ~/ && sudo git clone https://github.com/davidgregs87/Query-IP_Project.git")
    os.system("cd ~/Query-IP && sh install")
    get_logo()
    print(Fore.CYAN + "                             ----------------------" + Fore.YELLOW + "Query-IP updated successfully!" + Fore.CYAN + "------------------")
    time.sleep(1)

update()
