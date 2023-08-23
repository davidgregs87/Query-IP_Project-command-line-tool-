#!/usr/bin/python3
"""Main script"""

import requests
import sys
from colorama import Fore, Style
import os
from center import center_text

def query(ip):
    """A function that takes one argument(ip-address) and query it using an IP Geolocation Api
    endpoint and returns it result"""
    try:
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url)
        data = res.json()
        if data['status'] == 'success':
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
            print("                  " + Fore.CYAN + "------------------" + Fore.YELLOW +  "A more intuitive way to lookup your IP adresses" + Fore.CYAN +   "-----------------------------")
            print("                                  " + Fore.CYAN + "------------------" + Fore.YELLOW +  "<IP Information>" + Fore.CYAN +   "--------------")
            print("                                  " + Fore.CYAN + "------------------------------------------------")
            print("\n\n")

            lines = [
            Fore.YELLOW + "IP Address" +" "+ Fore.CYAN + f"{data['query']}\n",
            Fore.YELLOW + "Country" + " "+ Fore.CYAN + f"{data['country']}\n",
            Fore.YELLOW + "CountryCode" + " " + Fore.CYAN + f"{data['countryCode']}\n",
            Fore.YELLOW + "Region" + " " + Fore.CYAN + f"{data['region']}\n",
            Fore.YELLOW + "RegionName" + " " + Fore.CYAN + f"{data['regionName']}\n",
            Fore.YELLOW + "City"+ " " + Fore.CYAN + f"{data['city']}\n",
            Fore.YELLOW + "ZipCode" + " " +Fore.CYAN + f"{data['zip']}\n",
            Fore.YELLOW + "Lattitude" + " " + Fore.CYAN + f"{data['lat']}\n",
            Fore.YELLOW + "Longitude" + " " + Fore.CYAN + f"{data['lon']}\n",
            Fore.YELLOW + "TimeZone" + " " + Fore.CYAN + f"{data['timezone']}\n",
            Fore.YELLOW + "ISP" + " " + Fore.CYAN + f"{data['isp']}\n",
            Fore.YELLOW + "Organization" + " " + Fore.CYAN + f"{data['org']}\n",
            Fore.YELLOW + "ASN" + " " + Fore.CYAN + f"{data['as']}\n"
            ]
            centered_logo = "\n".join(center_text(line) for line in lines)
            print(centered_logo)
    except requests.exceptions.ConnectionError:
        print("Connection error. Check your network.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

if __name__ == '__main__':
    if len (sys.argv) != 2:
        print(Fore.CYAN + "Check the Usage on how to use this tool.")
    else:
        ip_addr = sys.argv[1]
        query(ip_addr)