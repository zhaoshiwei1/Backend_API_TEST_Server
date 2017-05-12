import os
import sqlite3

class db:
    def __init__(self):
        if os.path.exists("backend_platform_Server.db3"):
            self.conn = sqlite3.connect("backend_platform_Server.db3")
            self.cu = self.conn.cursor()
        else:
            print "DB FILE NOT FOUND, PLEASE CHECK THE PATH!"