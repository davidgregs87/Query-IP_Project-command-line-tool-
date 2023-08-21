#!/usr/bin/python3
# Tool Name :- Query-IP
# Author :- David Gregs
# Date :- 23/08/2023
# My first portfolio project @alx_africa

import os
import sys

if os.path.exists("/usr/lib/sudo"):
    if not os.path.exists("/usr/bin/python3"):
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get upgrade -y")
        os.system("sudo apt-get install python3")
else:
    if os.path.exists("/usr/bin"):
        if not os.path.exists("/usr/bin/python3"):
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt-get install python3")
if not os.path.exists("/usr/bin"):
    if not os.path.exists("/data/data/com.termux/files/usr/bin/python3"):
        os.system("pkg update -y")
        os.system("pkg upgrade -y")
        os.system("pkg install python3")

os.system("python3 model/setup.py")
sys.exit()