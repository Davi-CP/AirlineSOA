import sqlite3
from pathlib import Path

# Caminho do banco de dados na raiz do projeto
DB_PATH = Path(__file__).parent.parent.parent / 'banco_airline.db'

def buscar_voos(origem, destino, data):
    con = sqlite3.connect(str(DB_PATH))
    try:
        cursor = con.cursor()

        cursor.execute("""
            SELECT id, numero_voo, origem, destino, data,
                   hora_saida, hora_chegada, preco,
                   capacidade_disponivel, companhia_aerea
            FROM voos
            WHERE origem = ? AND destino = ? AND data = ?
        """, (origem, destino, data))

        return cursor.fetchall()

    finally:
        con.close()
