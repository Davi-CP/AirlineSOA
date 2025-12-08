import sqlite3
from pathlib import Path

# Caminho do banco de dados na raiz do projeto
DB_PATH = Path(__file__).parent.parent.parent / 'banco_airline.db'

def inserir_reserva(numero_voo, cpf, data_reserva, status, criado_em):
    con = sqlite3.connect(str(DB_PATH))
    try:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO reservas (
                numero_voo, cpf, data_reserva, status, criado_em
            ) VALUES (?, ?, ?, ?, ?)
        """, (numero_voo, cpf, data_reserva, status, criado_em))
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()


def listar_reservas_por_cpf(cpf):
    con = sqlite3.connect(str(DB_PATH))
    try:
        cursor = con.cursor()
        cursor.execute(
            "SELECT id, numero_voo, cpf, data_reserva, status FROM reservas WHERE cpf = ?", 
            (cpf,)
        )
        return cursor.fetchall()
    finally:
        con.close()


def deletar_reserva(reserva_id):
    con = sqlite3.connect(str(DB_PATH))
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
        afetadas = cursor.rowcount
        con.commit()
        return afetadas
    finally:
        con.close()
