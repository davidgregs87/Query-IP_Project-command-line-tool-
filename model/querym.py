#!/usr/bin/python3
"""Main script"""

import requests
from colorama import Fore, Style
import os
from center import center_text

def queryM():
    """A function that takes no argument but returns the ip address that calls this function"""
    try:
        url = f"http://ip-api.com/json"
        res = requests.get(url)
        data = res.json()
        if data['status'] == 'success':
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
        print(Fore.RED + "Connection error. Check your network.")
    except requests.exceptions.Timeout:
        print(Fore.RED + "Request timed out. Try again later.")
    except requests.exceptions.HTTPError as http_err:
        print(Fore.RED + f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(Fore.RED + f"An error occurred: {req_err}")
    
queryM()