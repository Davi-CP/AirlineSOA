import sqlite3
from datetime import datetime

DB_NAME = "banco_airline.db"

def seed_reservas(con):
    cur = con.cursor()

    # pega alguns ids de voos existentes
    cur.execute("SELECT id FROM voos ORDER BY id LIMIT 3")
    voos = cur.fetchall()
    if not voos:
        print("Nenhum voo encontrado; execute primeiro o seed de voos.")
        return

    agora = datetime.now().isoformat(timespec="seconds")  # string ISO simples [web:46][web:52][web:55]

    reservas = [
        # numero_voo (id da tabela voos), cpf, data_reserva, status, criado_em
        (voos[0][0], 11111111111, "2025-12-01", "CONFIRMADA", agora),
        (voos[1][0], 22222222222, "2025-12-02", "CONFIRMADA", agora),
        (voos[2][0], 33333333333, "2025-12-03", "CANCELADA", agora),
    ]

    cur.executemany(
        """
        INSERT INTO reservas (
            numero_voo, cpf, data_reserva, status, criado_em
        ) VALUES (?, ?, ?, ?, ?)
        """,
        reservas,
    )

    con.commit()


def main():
    con = sqlite3.connect(DB_NAME)
    try:
        seed_reservas(con)
        print("Seed concluído com sucesso.")
    finally:
        con.close()


if __name__ == "__main__":
    main()
