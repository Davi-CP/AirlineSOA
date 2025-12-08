from repository.voo_repository import buscar_voos
from spyne import srpc, ServiceBase, Unicode, Iterable
from models.voo_model import Voo


#service de voos usando Spyne
class VooService(ServiceBase):
    @srpc(Unicode, Unicode, Unicode, _returns=Iterable(Voo))
    def voos(origem, destino, data):
        """Busca voos disponíveis por origem, destino e data."""
        return buscar_voos(origem, destino, data)