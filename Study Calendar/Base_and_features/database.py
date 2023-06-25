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
        self.mouse.execute('CREATE TABLE IF NOT EXISTS category('
                           'id_cat integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'name TEXT UNIQUE,'
                           'color VARCHAR(255)'
                           ');')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS dayOff('
                           'id_day integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'month INT NOT NULL,'
                           'day INT NOT NULL,'
                           'year INT NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS commentary('
                           'id_com integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'description VARCHAR(255),'
                           'day INT NOT NULL,'
                           'month INT NOT NULL,'
                           'year INT NOT NULL);')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS calendar('
                           'id_cal integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'time INT NOT NULL,'
                           'day INT NOT NULL,'
                           'month INT NOT NULL,'
                           'year INT NOT NULL,'
                           'cat_ref INT,'
                           'offd_ref INT,'
                           'com_ref INT,'
                           'FOREIGN KEY(cat_ref) REFERENCES category(id_cat),'
                           'FOREIGN KEY(offd_ref) REFERENCES dayOff(id_day),'
                           'FOREIGN KEY(com_ref) REFERENCES commentary(id_com));')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS goal('
                           'id_goa integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'objective INT NOT NULL,'
                           'month INT NOT NULL,'
                           'year INT NOT NULL,'
                           'cate_ref INT NOT NULL,'
                           'FOREIGN KEY (cate_ref) REFERENCES category(id_cat));')

        self.mouse.execute('CREATE TABLE IF NOT EXISTS totalOff('
                           'id_off integer NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'day_off INT NOT NULL,'
                           'month INT NOT NULL,'
                           'YEAR INT NOT NULL);')

    def simple_select(self, table, name_col):
        sql = f'SELECT {name_col} FROM {table};'
        self.mouse.execute(sql)
        total = []
        for item in self.mouse:
            total.append(item[0])
        return len(total), total

    def choose_two(self, table, name_col, name_col2, col_search, search):
        sql = F'SELECT {name_col}, {name_col2} FROM {table} WHERE {col_search} = "{search}"'
        self.mouse.execute(sql)
        r = []
        for ids, name in self.mouse:
            r.append(ids)
            r.append(name)
        return r

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

    def insert_goal(self, objective, month, year, category):
        sql1 = f'SELECT id_goa FROM goal WHERE month = "{month}" AND year = "{year}" AND cate_ref = {category};'
        self.mouse.execute(sql1)
        unique = []
        for item in self.mouse:
            unique.append(item)
        if len(unique) == 0:
            sql = 'INSERT INTO goal(objective, month, year, cate_ref) VALUES("{}", "{}", "{}", "{}")' \
                .format(objective, month, year, category)
            try:
                self.mouse.execute(sql)
                self.con.commit()
            except:
                pass
            else:
                return 1
        else:
            sql = 'UPDATE goal SET objective = "{}" WHERE month = "{}" AND year = "{}" AND cate_ref = "{}"'\
                .format(objective, month, year, category)
            self.mouse.execute(sql)
            self.con.commit()
            return 1

    def insert_comment(self, content, day, month, year):
        sql = f'INSERT INTO commentary (description, day, month, year) VALUES ("{content}", "{day}", "{month}", "{year}");'
        self.mouse.execute(sql)
        self.con.commit()