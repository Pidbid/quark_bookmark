# -*- encoding: utf-8 -*-
"""
@File    :   quark_bookmark.py
@Time    :   2021/08/25 14:22:58
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib

import sqlite3


class QUARK_BOOKMARK:
    def __init__(self):
        "This is init fun"
        pass

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = "select title,url from bookmark"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def add_item(self):
        pre_data = """
        <!DOCTYPE NETSCAPE-Bookmark-file-1>
        <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
        <TITLE>Bookmarks</TITLE>
        <H1>Bookmarks</H1>
        <DL><p>
        """
        after_data = "</DL><p>"
        x = ""
        for i in self.connect():
            x += '<DT><A HREF="{}" ADD_DATE="0">{}</A> \n'.format(i[1], i[0])
        with open(self.save_path + "/bookmark.html", "w+", encoding="utf-8") as fp:
            fp.write(pre_data + x + after_data)

    def bookmark(self, db_path, save_path):
        self.save_path = save_path
        self.db_path = db_path
        self.add_item()


# a = QUARK_BOOKMARK()
# a.bookmark("a.db")
