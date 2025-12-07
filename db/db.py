import sqlite3 as s

#criar conexao
conexao = s.connect('banco_airline.db')
#criar cursor
cursor = conexao.cursor()

#criar tabela reservas
sql = "CREATE TABLE IF NOT EXISTS reservas (id INTEGER PRIMARY KEY, numero_voo INTEGER, cpf INTEGER, data_reserva TEXT, status TEXT, criado_em TEXT,FOREIGN KEY (numero_voo) REFERENCES voos (id))"
cursor.execute(sql)
conexao.commit()

#verifica se as tabelas foram criadas
res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(res.fetchall())
#fechar conexao
conexao.close()
