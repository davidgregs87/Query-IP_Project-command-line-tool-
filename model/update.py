#!/usr/bin/python3
"""A module for updating our tool(Query-IP)"""
import os
from colorama import Fore
import time
from center import center_text 


def get_logo():
    """Pulling up our logo"""
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

def update():
    """A function that will help us in updating our tool when there is update"""
    try:
        get_logo()
        new = [Fore.CYAN + "----------------------" + Fore.YELLOW + "Updating Query-IP...." + Fore.CYAN + "------------------"]
        centered_logo = "\n".join(center_text(line) for line in new)
        print(centered_logo)
        time.sleep(1)
        clone_status = os.system("cd ~/ && git clone https://github.com/davidgregs87/Query-IP_Project.git")
        sudo_clone_status = os.system("cd ~/ && sudo git clone https://github.com/davidgregs87/Query-IP_Project.git")
        install_status = os.system("cd ~/Query-IP_Project && sh install")
        if clone_status != 0 or sudo_clone_status != 0 or install_status != 0:
            get_logo()
            print(Fore.YELLOW + "Couldn't update Query-IP tool, because you already have the latest version")
        else:
            get_logo()
            new_line = [Fore.CYAN + "----------------------" + Fore.YELLOW + "Query-IP updated successfully!" + Fore.CYAN + "------------------"]
            centered = "\n".join(center_text(line) for line in new_line)
            print(centered)
        time.sleep(1)
    except KeyboardInterrupt:
        print(Fore.RED + "Process interrupted by user")

update()
