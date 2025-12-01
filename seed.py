import sqlite3
from datetime import datetime

DB_NAME = "banco_airline.db"


def seed_voos(con):
    cur = con.cursor()

    voos = [
        # numero_voo, origem, destino, data, hora_saida, hora_chegada,
        # preco, capacidade_total, capacidade_disponivel, companhia_aerea
        ("AZ1001", "POA", "GRU", "2025-12-10", "08:00", "10:00", 450.0, 180, 180, "Azul"),
        ("G31002", "GRU", "RIO", "2025-12-10", "11:00", "12:00", 320.0, 180, 180, "Gol"),
        ("LA2003", "RIO", "SSA", "2025-12-11", "09:30", "11:30", 600.0, 150, 150, "LATAM"),
        ("AZ2004", "POA", "RIO", "2025-12-11", "14:00", "16:00", 500.0, 150, 150, "Azul"),
        ("G31005", "GRU", "POA", "2025-12-12", "07:15", "09:00", 400.0, 180, 180, "Gol"),
    ]

    cur.executemany(
        """
        INSERT INTO voos (
            numero_voo, origem, destino, data,
            hora_saida, hora_chegada, preco,
            capacidade_total, capacidade_disponivel, companhia_aerea
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        voos,
    )

    con.commit()


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
        seed_voos(con)
        seed_reservas(con)
        print("Seed concluído com sucesso.")
    finally:
        con.close()


if __name__ == "__main__":
    main()
