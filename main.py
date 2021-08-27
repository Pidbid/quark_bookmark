# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2021/08/27 14:04:07
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
from modules import quark_bookmark
import os, sys

if __name__ == "__main__":
    quark = quark_bookmark.QUARK_BOOKMARK()
    try:
        file_path = sys.argv[1]
        quark.bookmark(file_path, os.getcwd())
    except:
        quark.bookmark("bookmark.db", os.getcwd())

