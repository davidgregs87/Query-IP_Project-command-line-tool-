#!/usr/bin/python3
"""Main script"""
from help import help
from querym import queryM
from queryip import query
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

def About():
    get_logo()
    print("                                  " + Fore.CYAN + "------------------" + Fore.YELLOW +  "Tool name" + Fore.CYAN +   "----" + Fore.YELLOW +  "Query-IP")
    print("                                  " + Fore.CYAN + "------------------" + Fore.YELLOW +  "Author" + Fore.CYAN +   "----" + Fore.YELLOW +  "David Gregs")
    print("                                  " + Fore.CYAN + "------------------" + Fore.YELLOW +  "Date" + Fore.CYAN +   "----" + Fore.YELLOW +  "23-08-2023")
    getact = input(' Query-ip >> ')
    menu()

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

def menu():
    get_logo()
    print("   " + Fore.CYAN + "Query IP Address.")
    print("   " + Fore.CYAN + "Query Your IP Address.")
    print("   " + Fore.CYAN + "About us.")
    print("   " + Fore.CYAN + "Help.")
    print("   " + Fore.CYAN + "Update Query-IP.")
    print("   " + Fore.CYAN + "Exit \n\n")
    val = input('  Query-IP >> ')
    
    if val == "x" or val == "exit":
        print(Fore.CYAN + "Exiting .......\n")
        time.sleep(1)
        print(Fore.CYAN + "Bye ....... \n\n")
        exit()
    elif val == "1":
        query()
    elif val == "2":
        queryM()
    elif val == "3":
        About()
    elif val == "4":
        help()
    elif val == "5":
        update()
    else:
        print(Fore.CYAN + f"[Err : Invalid Command {val}")
        time.sleep(1)
        menu()
menu()
