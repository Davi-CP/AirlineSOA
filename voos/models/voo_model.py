from spyne import ComplexModel, Unicode, Integer, Double

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