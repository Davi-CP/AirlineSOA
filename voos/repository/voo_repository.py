from db import get_db_connection


def buscar_voos(origem, destino, data):
    con = get_db_connection()
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
