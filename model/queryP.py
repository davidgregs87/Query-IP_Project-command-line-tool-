#!/usr/bin/python3
"""Main script"""

import requests
import sys
from colorama import Fore, Style
import os
 

def queryP():
    """A function that takes one argument(ip-address) and query it using an IP Geolocation Api
    endpoint and returns it result"""
    os.system("clear")
    print(Fore.CYAN + "\n")
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
    print("                                  " + Fore.CYAN + "------------------" + Fore.YELLOW +  "<IP Information>" + Fore.CYAN +   "--------------")
    print("                                  " + Fore.CYAN + "------------------------------------------------")
    print("\n\n")

    prompt = Fore.YELLOW
    print(prompt)
    ip = input(' Enter IP: ')
    url = f"http://ip-api.com/json/{ip}"
    res = requests.get(url)
    data = res.json()

    if data['status'] == 'success':
        print(Fore.YELLOW + "IP Address" +" "+ Fore.CYAN + f"{data['query']}")
        print(Fore.YELLOW + "Country" + " "+ Fore.CYAN + f"{data['country']}")
        print(Fore.YELLOW + "CountryCode" + " " + Fore.CYAN + f"{data['countryCode']}")
        print(Fore.YELLOW + "Region" + " " + Fore.CYAN + f"{data['region']}")
        print(Fore.YELLOW + "RegionName" + " " + Fore.CYAN + f"{data['regionName']}")
        print(Fore.YELLOW + "City"+ " " + Fore.CYAN + f"{data['city']}")
        print(Fore.YELLOW + "ZipCode" + " " +Fore.CYAN + f"{data['zip']}")
        print(Fore.YELLOW + "Lattitude" + " " + Fore.CYAN + f"{data['lat']}")
        print(Fore.YELLOW + "Longitude" + " " + Fore.CYAN + f"{data['lon']}")
        print(Fore.YELLOW + "TimeZone" + " " + Fore.CYAN + f"{data['timezone']}")
        print(Fore.YELLOW + "ISP" + " " + Fore.CYAN + f"{data['isp']}")
        print(Fore.YELLOW + "Organization" + " " + Fore.CYAN + f"{data['org']}")
        print(Fore.YELLOW + "ASN" + " " + Fore.CYAN + f"{data['as']}")
    else:
        print(Fore.CYAN + "Sorry unable to query your IP Address" + Fore.YELLOW + " " + f"<{data['query']}> \n")
        print(Fore.CYAN + "Check your Network connection\n")
        print(Fore.CYAN + "If you are online please check your IP Address!!")

    prompt = Fore.CYAN
    print(prompt, end="")
    getact = input(' Query-IP >> ')
    from Query_IP import menu 
    menu()