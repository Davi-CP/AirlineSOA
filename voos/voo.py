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

class FlightServices(ServiceBase):
    @srpc(_returns=Unicode)
    def ping():
        return "Pong"
    
    @srpc(Unicode, Unicode, Unicode, _returns=Iterable(Voo))
    def voos(origem, destino, data):
        # Acessa APENAS o banco de dados de voos
        pass