import sqlite3 as s

#criar conexao
conexao = s.connect('banco_airline.db')
#criar cursor
cursor = conexao.cursor()

#criar tabela voos
sql = "CREATE TABLE IF NOT EXISTS voos (id INTEGER PRIMARY KEY, numero_voo TEXT, origem TEXT, destino TEXT, data TEXT, hora_saida TEXT, hora_chegada TEXT, preco REAL, capacidade_total INTEGER, capacidade_disponivel INTEGER, companhia_aerea TEXT)"
cursor.execute(sql)
#criar tabela reservas
sql = "CREATE TABLE IF NOT EXISTS reservas (id INTEGER PRIMARY KEY, numero_voo INTEGER, cpf INTEGER, data_reserva TEXT, status TEXT, criado_em TEXT,FOREIGN KEY (numero_voo) REFERENCES voos (id))"
cursor.execute(sql)
conexao.commit()

#verifica se as tabelas foram criadas
res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(res.fetchall())
#fechar conexao
conexao.close()
