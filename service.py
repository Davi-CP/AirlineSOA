from spyne import Application, srpc, ServiceBase, Unicode, Integer, Double, Iterable, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class Voo(ComplexModel):
    id = Integer
    numero_voo = Unicode
    origem = Unicode
    destino = Unicode
    data = Unicode
    hora_saida = Unicode
    hora_chegada = Unicode
    preco = Double
    capacidade_disponivel = Integer
    companhia_aerea = Unicode

class Reserva(ComplexModel):
    id = Integer
    numero_voo = Unicode
    cpf = Unicode
    data_reserva = Unicode
    status = Unicode

class AirlineService(ServiceBase):

    @srpc(_returns=Unicode)
    def ping():
        return "Pong"
    
    @srpc(Unicode, Unicode, Unicode, _returns=Iterable(Voo))
    def consultar_voos(origem, destino, data):
        # acessar o banco de dados e retornar a lista de voos correspondentes
        pass

    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def reservar_passagem(nome, cpf, numero_voo, data):
        # realizar a reserva e retornar um número de confirmação
        pass

    @srpc(Unicode, Unicode, _returns=Iterable(Reserva))
    def consultar_reservas(cpf, data):
        # acessar o banco de dados e retornar a lista de reservas correspondentes
        pass

