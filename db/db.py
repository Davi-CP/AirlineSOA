import sqlite3 as s
from pathlib import Path

# Caminho do banco de dados na raiz do projeto
DB_PATH = Path(__file__).parent.parent / 'banco_airline.db'

#criar conexao
conexao = s.connect(str(DB_PATH))
#criar cursor
cursor = conexao.cursor()


#criar tabela voos
sql = "CREATE TABLE IF NOT EXISTS voos (id INTEGER PRIMARY KEY, numero_voo INTEGER, origem TEXT, destino TEXT, data_voo TEXT, horario_partida TEXT, horario_chegada TEXT, capacidade INTEGER, criado_em TEXT)"
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
