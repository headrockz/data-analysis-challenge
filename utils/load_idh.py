import sqlite3
import pandas as pd


class LoadIDH:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def select(self, municipio):
        consult = 'select id_municipio from municipios where municipio like ?'
        self.cursor.execute(consult, (f'%{municipio}%',))
        result = self.cursor.fetchall()
        
        return result
        
    def insert(self, idh, fk_municipio):
        if fk_municipio != []:
            consult = '''INSERT OR IGNORE INTO idh (idh, fk_municipio) VALUES (?, ?)'''
            self.cursor.execute(consult, (idh, fk_municipio[0][0]))
            self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# Tests
if __name__ == '__main__':
    data = LoadIDH('database.db')

    df = pd.read_excel('../datasets/idh.xlsx')

    for i in df.values:
        result = data.select(i[0])

        data.insert(i[1], result)

    data.close()