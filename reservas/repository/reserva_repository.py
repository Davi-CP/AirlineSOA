import sqlite3
from pathlib import Path
from models.reserva_model import Reserva

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
        #converter tuplas em objetos Reserva
        rows = cursor.fetchall()
        reservas = []
        for row in rows:
            reserva = Reserva()
            reserva.id = row[0]
            reserva.numero_voo = row[1]
            reserva.cpf = row[2]
            reserva.data_reserva = row[3]
            reserva.status = row[4]
            reservas.append(reserva)
        return reservas
    
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
