import sqlite3
import pandas as pd


class LoadPopulacao:
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
    data = LoadPopulacao('database.db')

    df = pd.read_excel('datasets/populacao.xls', sheet_name='municipios')

    for i in df.values:
        result = data.select(i[1])

        data.insert(i[2], i[3], result)

    data.close()