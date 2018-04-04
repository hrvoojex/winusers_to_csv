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


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    input("I am admin. Before if loop.")
    sp = subprocess.Popen(['wmic', '/output:usracc.csv', 'useraccount', 'list', 'full', '/format:csv'],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = sp.communicate()
    print(out, err, sp.returncode)
    input("I am admin. After if loop.")

else:
    input("I'm not admin. Before else loop.")
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
    input("I'm not admin. After else loop.")

#subprocess.call(['wmic', '/output:usracc.csv', 'useraccount', 'list', 'full', '/format:csv'])