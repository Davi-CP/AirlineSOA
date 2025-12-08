from datetime import datetime
from repository.reserva_repository import (
    inserir_reserva,
    listar_reservas_por_cpf,
    deletar_reserva
)
from spyne import srpc, ServiceBase, Unicode, Iterable
from models.reserva_model import Reserva

#service de reservas usando Spyne
class ReservaService(ServiceBase):
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def criar_reserva(data_reserva, numero_voo, cpf, nome_passageiro):
        """Regra de negócio: cria uma nova reserva."""
        return criar_reserva_domain(data_reserva, numero_voo, cpf, nome_passageiro)

    @srpc(Unicode, _returns=Iterable(Reserva))
    def listar_reservas(cpf):
        """Regra de negócio: lista reservas por CPF."""
        return listar_reservas_domain(cpf)

    @srpc(Unicode, _returns=Unicode)
    def deletar_reserva(reserva_id):
        """Regra de negócio: deleta uma reserva por ID."""
        return deletar_reserva_domain(reserva_id)



# Lógica de negócio separada dos serviços
def criar_reserva_domain(data_reserva, numero_voo, cpf, nome_passageiro):
    agora = datetime.now().isoformat(timespec="seconds")
    status = "CONFIRMADA"

    reserva_id = inserir_reserva(numero_voo, cpf, data_reserva, status, agora)
    return f"Reserva {reserva_id} criada com sucesso para o CPF {cpf}."


def listar_reservas_domain(cpf):
    return listar_reservas_por_cpf(cpf)


def deletar_reserva_domain(reserva_id):
    linhas = deletar_reserva(reserva_id)
    if linhas == 0:
        return f"Erro: Reserva {reserva_id} não encontrada para exclusão."
    
    return f"Reserva {reserva_id} excluída com sucesso."
