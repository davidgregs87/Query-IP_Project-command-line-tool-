#!/usr/bin/python3
# Tool Name :- Query-IP
# Author :- David Gregs
# Date :- 23/08/2023
# My first portfolio project @alx_africa
import os
import sys


if os.path.isdir("/data/data/com.termux/files/usr/share"):
    os.chdir("/data/data/com.termux/files/usr/share/Query-IP")
    os.system("python3 query.py " + " ".join(sys.argv[1:]))
elif os.path.isdir("/usr/share"):
    os.chdir("/usr/share/Query-IP")
    os.system("python3 query.py " + " ".join(sys.argv[1:]))