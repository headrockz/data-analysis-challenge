import sqlite3
import pandas as pd


class LoadMunicipios:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def select(self, municipio):
        consult = 'select id_municipio from municipios where municipio like ?'
        self.cursor.execute(consult, (f'%{municipio}%',))
        result = self.cursor.fetchall()
        
        return result
        
    def insert_municipio(self, municipio, uf, result):
        if result == []:
            consult = '''INSERT OR IGNORE INTO municipios (municipio, uf) 
                        VALUES (?, ?)'''
            self.cursor.execute(consult, (municipio, uf))
            self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# Tests
if __name__ == '__main__':
    data = LoadMunicipios('database.db')
    
    # salvando os municipios dos datasets de agencias, postos e postos eletronicos 
    # agencia = pd.read_sql('SELECT DISTINCT municipio, uf FROM agencias', con=data.conn)
    # postos = pd.read_sql('SELECT DISTINCT municipio, uf FROM postos', con=data.conn)
    postose = pd.read_sql('SELECT DISTINCT municipio, uf FROM postos_eletronicos', con=data.conn)
    
   

    for i in postose.values:
        result = data.select(i[0])

        data.insert_municipio(i[0], i[1], result)


         

    data.close()