import sqlite3 as s
from pathlib import Path
DB_PATH = Path(__file__).parent.parent / 'banco_airline.db'

con = s.connect(DB_PATH)
cur = con.cursor()
cur.execute("DELETE FROM reservas WHERE cpf = ?", ("15432098741",))
con.commit()
print("Linhas removidas:", cur.rowcount)
con.close()