# Plataforma para reserva de passagens de companhia aérea usando a arquitetura SOA

## Pré-requisitos

- Python 3.10 instalado (confira com `python --version`).
- Git instalado.

## Passos para rodar o projeto

### 1. Clone o repositório
```
git clone https://github.com/Davi-CP/AirlineSOA.git
cd AirlineSOA
```
### 2. Crie o ambiente virtual

#### macOS / Linux
```
python3.10 -m venv venv
source venv/bin/activate
```


### 3. Instale as dependências

No terminal (com o venv ativo), rode:

```
pip install -r requirements.txt
```


### 4. Prepare o banco de dados

> Se já existir um arquivo de banco, pode pular este passo.  
Para popular dados de teste, execute o seed:

### 5. Inicie o servidor SOAP
```
python server.py
```
O serviço ficará disponível em:  
http://localhost:8000/  
O WSDL estará em:  
http://localhost:8000/?wsdl

### 6. Teste da aplicação

Use o client Zeep fornecido ou ferramentas como SoapUI/Postman para consumir os serviços expostos.

### Dicas

- O ambiente virtual (venv) **não** deve ser versionado.  
- Sempre use o ambiente virtual antes de rodar scripts Python do projeto.  
- Se mudar o sistema operacional, só repita o passo de criação/ativação do venv.

---

### Problemas comuns

- Se não conseguir ativar o venv no Windows, tente `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` no PowerShell.
- Caso uma dependência falhe na instalação, confira se está mesmo no Python 3.10.

---

### Exemplos de curl 

- Dentro da pasta reservas

* Verificar se o servidor está de pé

```
curl http://localhost:8001\?wsdl
```
* Criar nova reserva (vai dar erro por enquanto, pois não está salvando no banco)

```
curl -X POST http://0.0.0.0:8001/ -H 'Content-Type: text/xml; charset=utf-8' --data '
<soap11:Envelope xmlns:soap11="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="http://examplo.com/airline/reservas">
    <soap11:Body>
        <tns:criar_reserva>
            <tns:data_reserva>2026-04-20</tns:data_reserva>
            <tns:numero_voo>101</tns:numero_voo>
            <tns:cpf>12345678901</tns:cpf>
            <tns:nome_passageiro>João Teste Curl</tns:nome_passageiro>
        </tns:criar_reserva>
    </soap11:Body>
</soap11:Envelope>'

```

- Dentro da pasta voos

* Verificar se o servidor está de pé

```
curl http://localhost:8001\?wsdl
```

### Estrutura de um projeto SOA

```
flight-service/
│
├── src/
│   ├── server.py              # Ponto de entrada (expõe o serviço Voo, usando Spyne)
│   ├── business_logic/
│   │   └── voo_service.py     # Lógica de negócio de Voos (consultar_voos)
│   ├── models/
│   │   └── voo_model.py       # Modelo Spyne/Estrutura de dados de Voo
│   ├── persistence/
│   │   ├── db.py              # Conexão com a DB do Voo
│   │   └── voo_repository.py  # Lógica de acesso a dados (CRUD)
│
├── db/
│   └── seed.py                # Dados iniciais para a DB do Voo
│
└── config/
    └── settings.py            # Configurações de porta, DB, etc.
```
```
reservation-service/
│
├── src/
│   ├── server.py              # Ponto de entrada (expõe o serviço Reserva, usando Spyne)
│   ├── business_logic/
│   │   └── reserva_service.py # Lógica de negócio de Reservas (fazer_reserva)
│   ├── models/
│   │   └── reserva_model.py   # Modelo Spyne/Estrutura de dados de Reserva
│   ├── persistence/
│   │   ├── db.py              # Conexão com a DB da Reserva
│   │   └── reserva_repository.py # Lógica de acesso a dados (CRUD)
│
├── db/
│   └── seed.py                # Dados iniciais para a DB da Reserva
│
└── config/
    └── settings.py            # Configurações de porta, DB, etc.
```
```
client-application/
│
├── src/
│   ├── frontend/              # Interface do utilizador (UI)
│   └── logic/
│       └── travel_manager.py  # Orquestra as chamadas
│                              # - Chama 'FlightService' para obter voos
│                              # - Chama 'ReservationService' para reservar
│
└── config/
    └── service_urls.py        # Guarda os endereços (URLs) dos serviços externos
```
