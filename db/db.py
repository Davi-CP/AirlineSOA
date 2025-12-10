import sqlite3 as s
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'banco_airline.db'

conexao = s.connect(str(DB_PATH))
cursor = conexao.cursor()

# Tabela voos compatível com seed.py
sql = """
CREATE TABLE IF NOT EXISTS voos (
    id INTEGER PRIMARY KEY,
    numero_voo TEXT,
    origem TEXT,
    destino TEXT,
    data TEXT,
    hora_saida TEXT,
    hora_chegada TEXT,
    preco REAL,
    capacidade_total INTEGER,
    capacidade_disponivel INTEGER,
    companhia_aerea TEXT,
    criado_em TEXT
)
"""
cursor.execute(sql)

# Tabela reservas: se você quer relacionar pelo ID do voo, mantenha numero_voo como INTEGER e referencie voos(id)
sql = """
CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY,
    numero_voo INTEGER,
    cpf TEXT,
    data_reserva TEXT,
    status TEXT,
    criado_em TEXT,
    FOREIGN KEY (numero_voo) REFERENCES voos (id)
)
"""
cursor.execute(sql)

conexao.commit()

res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(res.fetchall())

conexao.close()
