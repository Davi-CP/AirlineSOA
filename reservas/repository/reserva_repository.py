from .db import get_db_connection

def inserir_reserva(numero_voo, cpf, data_reserva, status, criado_em):
    con = get_db_connection()
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
    con = get_db_connection()
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
    con = get_db_connection()
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
        afetadas = cursor.rowcount
        con.commit()
        return afetadas
    finally:
        con.close()
