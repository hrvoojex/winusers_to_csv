#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor: Hrvoje T.
Created: 15.12.2017.
Last edit: 27.03.2017.
Version: 0.0.1
"""

import ctypes
import sys
import subprocess


# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
#
# if is_admin():
#     input("admin sam. prije naredbe if petlja")
#     subprocess.call(['wmic', '/output:usracc.csv', 'useraccount', 'list', 'full', '/format:csv'])
#     input("admin sam. poslije naredbe if petlja")
#
# else:
#     input("nisam admin. prije naredbe else petlja")
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
#     input("nisam admin. poslije naredbe else petlja")

subprocess.call(['wmic', '/output:usracc.csv', 'useraccount', 'list', 'full', '/format:csv'])