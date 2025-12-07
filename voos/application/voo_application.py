from repository.voo_repository import buscar_voos


def buscar_voos_domain(origem, destino, data):
    """Regra de negócio: apenas retorna voos filtrados."""
    return buscar_voos(origem, destino, data)
