import sqlite3

class Database:
    def connect(self):
        self.con = sqlite3.connect('items_sc.bd')
        self.mouse = self.con.cursor()

    def disconnect(self):
        self.con.close()

