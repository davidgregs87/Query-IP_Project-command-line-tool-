#!/usr/bin/python3
"""setup module"""
import os
import colorama
from colorama import Fore
from systemSetup import detect_system

class setUp():
    """An setup class"""
    def set_up(self):
    # Removing old files
        system = detect_system()
        if system == "ubuntu":
            os.system("sudo rm -rf /usr/bin/query-ip.py /usr/bin/query1.py /usr/share/Query-IP")
        elif system == "termux":
            os.system("rm -rf /data/data/com.termux/files/usr/share/Query-IP /data/data/com.termux/files/usr/bin/query-ip.py /data/data/com.termux/files/usr/bin/query1.py")
        else:
            os.system("sudo rm -rf /usr/bin/query-ip.py /usr/bin/query1.py /usr/share/Query-IP")
    
        # Adding bin file
        if system == "ubuntu":
            os.system("sudo mv -v model/query-ip.py /usr/bin/")
            os.system("sudo mv -v model/query1.py /usr/bin/")
            os.system("sudo chmod +x /usr/bin/query-ip.py /usr/bin/query1.py")
        elif system == "termux":
            os.system("mv -v model/query-ip.py /data/data/com.termux/files/usr/bin/")
            os.system("mv -v model/query1.py /data/data/com.termux/files/usr/bin/")
            os.system("chmod +x /data/data/com.termux/files/usr/bin/query-ip.py /data/data/com.termux/files/usr/bin/query1.py")
        else:
            os.system("mv -v model/query-ip.py /usr/bin/")
            os.system("mv -v model/query1.py /usr/bin/")
            os.system("chmod +x /usr/bin/query-ip.py /usr/bin/query1.py")
    
        # Copy files from Query-IP to target directory
        if system == "ubuntu":
            os.system("sudo mkdir /usr/share/Query-IP/")
            os.system("sudo cp -rv model/* /usr/share/Query-IP/")
        elif system == "termux":
            os.system("mkdir /data/data/com.termux/files/usr/share/Query-IP")
            os.system("cp -rv model/* /data/data/com.termux/files/usr/share/Query-IP/")
        else:
            os.system("mkdir /usr/share/Query-IP")
            os.system("cp -rv model/* /usr/share/Query-IP/")
    
        # Removing Query-IP directory
        os.system("cd .. && rm -rf Query-IP")
    def logo(self):
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

        if os.path.exists("/usr/bin/query-ip") or os.path.exists("/data/data/com.termux/files/usr/bin/query-ip"):
            print("                                          " + Fore.YELLOW + "Query-IP successfully installed!\n")
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
        else:
            print("                                          " + Fore.YELLOW + "Sorry Query-IP could not be installed")

setUP = setUp()
setUP.set_up()
setUP.logo()