import sqlite3


class Database:
    def __init__(self):
        self.con = None
        self.mouse = None

    def connect(self):
        self.con = sqlite3.connect('items_sc.bd')
        self.mouse = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def table_create(self):
        self.mouse.execute('CREATE TABLE IF NOT EXISTS CATEGORY('
                           'id_cat integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'name TEXT UNIQUE,'
                           'color VARCHAR(255)'
                           ');')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS CALENDAR ('
                           'id_cal integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'time INT NOT NULL,'
                           'day INT NOT NULL,'
                           'month INT NOT NULL,'
                           'year INT NOT NULL,'
                           'cat_ref INT,'
                           'FOREIGN KEY(cat_ref) REFERENCES CATEGORY(id_cat));')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS COMENTARY('
                           'id_com integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'description VARCHAR(255),'
                           'cal_ref INT,'
                           'FOREIGN KEY (cal_ref) REFERENCES CALENDAR(id_cal));')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS GOAL('
                           'id_goa integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'objective INT NOT NULL,'
                           'month INT NOT NULL,'
                           'year INT NOT NULL,'
                           'cate_ref INT NOT NULL,'
                           'FOREIGN KEY (cate_ref) REFERENCES CATEGORY(id_cat));')

    def simple_select(self, table, name_col):
        sql = f'SELECT {name_col} FROM {table};'
        self.mouse.execute(sql)
        total = []
        for item in self.mouse:
            total.append(item[0])
        return len(total)

    def insert_cat(self, name, color):
        sql = 'INSERT INTO category(name, color) VALUES ("{}", "{}");'.format(name, color)
        self.mouse.execute(sql)
        self.con.commit()

    def show_cat(self):
        sql = f'SELECT name, color FROM category;'
        self.mouse.execute(sql)
        cats = []
        for cat in self.mouse:
            cats.append(cat)
        return cats

    def delete_cat(self, choose):
        sql = f'SELECT name, color FROM category;'
        self.mouse.execute(sql)
        cats = []
        total = []
        for cat in self.mouse:
            cats.append(cat)
            total.append(cat[0])
        choose = int(choose[1:]) - 1
        sql1 = f'DELETE FROM category WHERE name = "{cats[choose][0]}";'
        self.mouse.execute(sql1)
        self.con.commit()