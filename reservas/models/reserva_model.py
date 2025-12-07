from spyne import ComplexModel, Unicode, Integer

class Reserva(ComplexModel):
    data_reserva = Unicode
    numero_voo = Integer 
    cpf = Integer        
    id = Integer
    status = Unicode
