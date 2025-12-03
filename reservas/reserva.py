import sqlite3 as s
from datetime import datetime
from spyne import srpc, ServiceBase, Unicode, Integer, Iterable, ComplexModel

DB_NAME = "banco_airline.db"

class Reserva(ComplexModel):
    data_reserva = Unicode
    numero_voo = Integer 
    cpf = Integer        
    id = Integer
    status = Unicode


def get_db_connection():
    """Conecta ao banco de dados SQLite."""
    return s.connect(DB_NAME) 

class ReservationService(ServiceBase):
    
    @srpc(_returns=Unicode)
    def ping():
        """Verifica se o serviço está ativo."""
        return "Pong"

    @srpc(Unicode, Integer, Integer, Unicode, _returns=Unicode)
    def criar_reserva(data_reserva, numero_voo, cpf, nome_passageiro):
        """Cria uma nova reserva e retorna o ID de confirmação."""
        con = get_db_connection()
        try:
            cursor = con.cursor()
            agora = datetime.now().isoformat(timespec="seconds")
            status_inicial = "CONFIRMADA"

            cursor.execute(
                """
                INSERT INTO reservas (
                    numero_voo, cpf, data_reserva, status, criado_em
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (numero_voo, cpf, data_reserva, status_inicial, agora)
            )
            con.commit()
            reserva_id = cursor.lastrowid
            
            return f"Reserva {reserva_id} criada com sucesso para o CPF {cpf}."
        
        except s.Error as e:
            con.rollback()
            return f"Erro ao criar reserva: {e}"
        finally:
            con.close()


    @srpc(Integer, _returns=Iterable(Reserva))
    def listar_reserva_by_cpf(cpf):
        """Lista todas as reservas associadas a um CPF específico."""
        con = get_db_connection()
        try:
            cursor = con.cursor()
            cursor.execute(
                "SELECT id, numero_voo, cpf, data_reserva, status FROM reservas WHERE cpf = ?", 
                (cpf,)
            )
            reservas_raw = cursor.fetchall()
            
            reservas_list = []
            for row in reservas_raw:
                reservas_list.append(
                    Reserva(
                        id=row[0],
                        numero_voo=row[1],
                        cpf=row[2],
                        data_reserva=row[3],
                        status=row[4]
                    )
                )
            return reservas_list
        
        finally:
            con.close()

    @srpc(Integer, _returns=Unicode)
    def deletar_reserva(reserva_id):
        """Deleta (ou cancela) uma reserva usando o seu ID."""
        con = get_db_connection()
        try:
            cursor = con.cursor()
            
            cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
            
            if cursor.rowcount == 0:
                return f"Erro: Reserva {reserva_id} não encontrada para exclusão."
            
            con.commit()
            
            return f"Reserva {reserva_id} excluída com sucesso."
            
        except s.Error as e:
            con.rollback()
            return f"Erro ao deletar reserva: {e}"
        finally:
            con.close()