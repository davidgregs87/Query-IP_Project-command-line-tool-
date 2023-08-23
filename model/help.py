"""A module for quick help(Query-IP)"""

from colorama import Fore
import os
from center import center_text

def help():
    """A quick start help with Query-IP"""
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

    logo_line = [
    Fore.YELLOW + "Quick Guide to using Query-IP tool\n",
    Fore.YELLOW + "Help/Usage",
    Fore.YELLOW + "_________________________________________________________________",
    Fore.YELLOW + "                     |" + Fore.CYAN + "           Command" + Fore.YELLOW + "        |" + Fore.CYAN + "           Use" + Fore.YELLOW + "                        |",      
    Fore.YELLOW + "|__________________________|______________________________________|",
    Fore.YELLOW + "                     |" + Fore.CYAN + "      Query -l" + Fore.YELLOW + "     |" + Fore.CYAN + "  Query the IP address of the local machine" + Fore.YELLOW + "  |", 
    Fore.YELLOW + "|___________________|_____________________________________________|",
    Fore.YELLOW + "                     |" + Fore.CYAN + "         Query -t <target_ip>" + Fore.YELLOW + "  |" + Fore.CYAN + " Query the IP of a target machine" + Fore.YELLOW + "|",
    Fore.YELLOW + "|_______________________________|_________________________________|",
    Fore.YELLOW + "                     |" + Fore.CYAN + "         Query --help" + Fore.YELLOW + "     |" + Fore.CYAN + "     Quick help" + Fore.YELLOW + "                       |",
    Fore.YELLOW + " |__________________________|______________________________________|\n",
    Fore.YELLOW + "Note: Dont try to make query for over 150 times, you could get banned",
    ]
    centered_logo = "\n".join(center_text(line) for line in logo_line)
    print(centered_logo)

help()

