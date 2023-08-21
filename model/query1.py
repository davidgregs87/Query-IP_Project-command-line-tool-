#!/usr/bin/python3
# Tool Name :- Query-IP
# Author :- David Gregs
# Date :- 23/08/2023
# My first portfolio project @alx_africa

import os
import sys

if os.path.exists("/data/data/com.termux/files/usr/share"):
    os.chdir("/data/data/com.termux/files/usr/share/Query-IP")
    os.execvp("bash", ["bash", "query"] + sys.argv[1:])

elif os.path.exists("/usr/share"):
    os.chdir("/usr/share/Query-IP")
    os.execvp("bash", ["bash", "query"] + sys.argv[1:])
