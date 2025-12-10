from spyne import ComplexModel, Unicode, Integer

class Reserva(ComplexModel):
    data_reserva = Unicode
    numero_voo = Unicode 
    cpf = Integer        
    id = Integer
    status = Unicode
