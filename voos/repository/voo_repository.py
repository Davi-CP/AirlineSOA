import sqlite3
from pathlib import Path
from models.voo_model import Voo

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

        rows = cursor.fetchall()
        
        # Converter tuplas em objetos Voo
        voos = []
        for row in rows:
            voo = Voo()
            voo.id = row[0]
            voo.numero_voo = row[1]
            voo.origem = row[2]
            voo.destino = row[3]
            voo.data = row[4]
            voo.hora_saida = row[5]
            voo.hora_chegada = row[6]
            voo.preco = row[7]
            voo.capacidade_disponivel = row[8]
            voo.companhia_aerea = row[9]
            voos.append(voo)
        
        return voos

    finally:
        con.close()
