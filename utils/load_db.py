import sqlite3
import pandas as pd


class LoadDb:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def select(self, municipio):
        consult = 'select id_municipio from municipios where municipio like ?'
        self.cursor.execute(consult, (f'%{municipio}%',))
        result = self.cursor.fetchall()
        
        return result
        
    def insert(self, populacao, coeficiente_populacional, fk_municipio):
        if fk_municipio != []:
            consult = '''INSERT OR IGNORE INTO populacao_municipal (populacao, coeficiente_populacional, fk_municipio) VALUES (?, ?, ?)'''
            self.cursor.execute(consult, (populacao, coeficiente_populacional, fk_municipio[0][0]))
            self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# Tests
if __name__ == '__main__':
    data = LoadDb('database.db')
    cont = 1
    df = pd.read_excel('datasets/postosEletronicos.xlsx')

    for i in df.values:
        data.insert_postosEletronicos(i[0], i[1], i[2])

    data.close()
