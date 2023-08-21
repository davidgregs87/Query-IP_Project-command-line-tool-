#!/usr/bin/python3
# Tool Name :- Query-IP
# Author :- David Gregs
# Date :- 23/08/2023
# My first portfolio project @alx_africa

import sys
import os

def query_own_ip():
    os.system("python3 model/querym.py")

def query_target_ip(ip):
    if len(ip) == 1:
        os.system(f"python3 model/queryip.py {ip[0]}")
    else:
        print("error: invalid arguments !!")
        print("use: query -t <target_ip>")

def update_query_ip():
    os.system("python3 model/update.py")
    sys.exit()

def start_query_ip():
    os.system("python3 model/Query_IP.py")
    sys.exit()

def uninstall_query_ip():
    os.system("python3 model/uninstall.py")
    sys.exit()

def show_usage():
    print("Usage: query [command]... [arguments]...")
    print(" Commands:")
    print(" -t <target_ip>      to query target ip.")
    print(" -m                  to query your own ip.")
    print(" -h                  to show help.")
    print(" -u                  to update Query-IP.")
    print(" help                to show help.")
    print(" update              to update Query-IP.")
    print(" start               to start Query-IP menu.")
    sys.exit()

def main():
    if len(sys.argv) < 2:
        show_usage()

    command = sys.argv[1]

    if command == "-m":
        query_own_ip()
    elif command == "-t":
        query_target_ip(sys.argv[2:])
    elif command == "-u" or command == "update":
        update_query_ip()
    elif command == "start":
        start_query_ip()
    elif command == "-rm":
        uninstall_query_ip()
    else:
        show_usage()

if __name__ == "__main__":
    main()
