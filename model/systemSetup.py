#!/usr/bin/python3
"""A module for system setup"""
import os

def detect_system() -> str:
    """a function that detects a system and returns the system name"""
    if os.path.exists("/usr/bin/apt"):
        if any(os.path.exists(path) for path in ["/usr/lib/sudo", "/usr/bin/sudo", "/usr/sbin/sudo"]):
            return "ubuntu"
        else:
            return "debian"
    elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
        return "termux"
    elif os.path.exists('C:\\Program Files\\'):
        return "windows"
    elif os.path.exists('/Applications'):
        return "macOS"
    
detect_system()
