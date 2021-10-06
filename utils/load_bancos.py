import sqlite3
import pandas as pd


class LoadBancos:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def select(self, municipio):
        consult = 'select id_municipio from municipios where municipio like ?'
        self.cursor.execute(consult, (f'%{municipio}%',))
        result = self.cursor.fetchall()
        
        return result
        
    def insert_bancos_agencias(self, nome_instituicao ,qtde_agencias, result):
        consult = '''INSERT OR IGNORE INTO bancos (nome_instituicao, qtde_agencias, qtde_postos,      qtde_postosele, fk_municipio) VALUES (?, ?, ?, ?, ?)'''
        self.cursor.execute(consult, (nome_instituicao, qtde_agencias, 0, 0, result[0][0]))
        self.conn.commit()

    def insert_or_update_postos(self, nome_instituicao ,qtde_postos, result):
        if result == []:
            consult = '''INSERT OR IGNORE INTO bancos (nome_instituicao, qtde_agencias, qtde_postos,      qtde_postosele, fk_municipio) VALUES (?, ?, ?, ?, ?)'''
            self.cursor.execute(consult, (nome_instituicao, 0, qtde_postos, 0, result[0][0]))
        else:
            update = f'''
                UPDATE OR IGNORE bancos
                    SET qtde_postos = {qtde_postos}
                    WHERE fk_municipio = {result[0][0]}
            '''
            self.cursor.execute(update)

        self.conn.commit()

    def insert_or_update_postos_e(self, nome_instituicao ,qtde_postosele, result):
        if result == []:
            consult = '''INSERT OR IGNORE INTO bancos (nome_instituicao, qtde_agencias, qtde_postos,      qtde_postosele, fk_municipio) VALUES (?, ?, ?, ?, ?)'''
            self.cursor.execute(consult, (nome_instituicao, 0, 0, qtde_postosele, result[0][0]))
        else:
            update = f'''
                UPDATE OR IGNORE bancos
                    SET qtde_postosele = {qtde_postosele}
                    WHERE fk_municipio = {result[0][0]}
            '''
            self.cursor.execute(update)

        self.conn.commit()

        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# Tests
if __name__ == '__main__':
    data = LoadBancos('database.db')
 
    agencia = pd.read_sql('SELECT nome_instituicao, municipio,  count(id_agencia) FROM agencias GROUP BY nome_instituicao, municipio ORDER BY municipio', con=data.conn)

    # for i in agencia.values:
    #     result = data.select(i[1])

    #     data.insert_bancos_agencias(i[0], i[2], result)

    # postos = pd.read_sql('SELECT nome_instituicao, municipio, count(id_postos) FROM postos GROUP BY nome_instituicao, municipio ORDER BY municipio', con=data.conn)
    
    # for i in postos.values:
    #     result = data.select(i[1])

    #     data.insert_or_update_postos_e(i[0], i[2], result)

    postose = pd.read_sql('SELECT nome_instituicao, municipio, count(id_postose) FROM postos_eletronicos GROUP BY nome_instituicao, municipio ORDER BY municipio', con=data.conn)
    
    for i in postose.values:
        result = data.select(i[1])

        data.insert_or_update_postos_e(i[0], i[2], result)
   
        
    

    data.close()