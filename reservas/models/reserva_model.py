from spyne import ComplexModel, Unicode, Integer


class Reserva(ComplexModel):
    data_reserva = Unicode
    numero_voo = Integer  # alinhado ao tipo da coluna numero_voo (INTEGER)
    cpf = Unicode         # armazenado como TEXT no banco, retorna como string
    id = Integer
    status = Unicode
