"""A module for quick help(Query-IP)"""

from colorama import Fore
import os
from model.Query_IP import menu

def help():
    """A quick start help with Query-IP"""
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
    print("         " + Fore.YELLOW + "                    Help/Usage")
    print("         " + Fore.YELLOW + "                     _________________________________________________________________")
    print("                             " + Fore.YELLOW + "|" + Fore.CYAN + "         Command" + Fore.YELLOW + "                |" + Fore.CYAN + "                Use" + Fore.YELLOW + "             |")      
    print("         " + Fore.YELLOW + "                    |________________________________|________________________________|")
    print("                             " + Fore.YELLOW + "|" + Fore.CYAN + "         Query -l" + Fore.YELLOW + "     |" + Fore.CYAN + " Query the IP address of the local machine" + Fore.YELLOW + "|") 
    print("         " + Fore.YELLOW + "                    |______________________|__________________________________________|")
    print("                             " + Fore.YELLOW + "|" + Fore.CYAN + "    Query -t <target_ip>" + Fore.YELLOW + "     |" + Fore.CYAN + " Query the IP of a target machine" + Fore.YELLOW + "  |")
    print("         " + Fore.YELLOW + "                    |_____________________________|___________________________________|")
    print("                             " + Fore.YELLOW + "|" + Fore.CYAN + "    Query --help" + Fore.YELLOW + "                 |" + Fore.CYAN + "               Quick help" + Fore.YELLOW + "      |")
    print("         " + Fore.YELLOW + "                    |_________________________________|_______________________________|\n")
    print("         " + Fore.YELLOW + "                    Note: Dont try to make query for over 150 times, you could get banned")


prompt = "\033[00m"
print(prompt, end="")
getact = input(' Query-IP >> ')
menu()

