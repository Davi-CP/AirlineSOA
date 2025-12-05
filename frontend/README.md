# Frontend - Sistema de Reserva de Passagens Aéreas

Frontend web desenvolvido com Flask para consumir os serviços SOAP de voos e reservas.

## Características

- 🎨 Interface responsiva e moderna
- 🔍 Busca de voos por origem, destino e data
- 📋 Visualização de minhas reservas
- ➕ Criação de novas reservas
- 🗑️ Cancelamento de reservas
- 📊 Verificação de status dos serviços SOAP

## Pré-requisitos

- Python 3.10+
- Virtual Environment ativado
- Dependências instaladas (`pip install -r ../requirements.txt`)
- Serviços SOAP rodando:
  - Serviço de Voos na porta 8000
  - Serviço de Reservas na porta 8001

## Instalação

### 1. Instalar dependências (se ainda não fez)

```bash
cd ..  # Voltar à raiz do projeto
source venv/bin/activate #entrar no ambiente virtual
pip install -r requirements.txt
```

### 2. Iniciar os serviços SOAP

Em terminais diferentes:

```bash
# Terminal 1 - Serviço de Voos
source venv/bin/activate #entrar no ambiente virtual
cd voos
python3.10 server.py

# Terminal 2 - Serviço de Reservas
source venv/bin/activate #entrar no ambiente virtual
cd reservas
python3.10 server.py
```

### 3. Iniciar o Frontend Flask

```bash
source venv/bin/activate #entrar no ambiente virtual
cd frontend
python app.py
```

O frontend estará disponível em: **http://localhost:5000**

## Estrutura

```
frontend/
├── app.py                    # Aplicação Flask com rotas e integração SOAP
├── templates/
│   └── index.html           # Interface web
└── static/                  # Arquivos estáticos (CSS, JS, imagens)
```

## Rotas Disponíveis

### Frontend
- `GET /` - Página inicial

### API
- `POST /api/voos` - Buscar voos
  - Body: `{"origem": "SAO", "destino": "RIO", "data": "2026-04-20"}`
  
- `POST /api/minhas-reservas` - Listar reservas por CPF
  - Body: `{"cpf": "12345678901"}`
  
- `POST /api/criar-reserva` - Criar nova reserva
  - Body: `{"data_reserva": "2026-04-20", "numero_voo": 101, "cpf": 12345678901, "nome_passageiro": "João"}`
  
- `POST /api/deletar-reserva` - Deletar reserva
  - Body: `{"reserva_id": 1}`
  
- `GET /api/status` - Status dos serviços SOAP

## Exemplo de Uso

### 1. Buscar Voos
1. Acesse http://localhost:5000
2. Na aba "🔍 Buscar Voos":
   - Origem: SAO
   - Destino: RIO
   - Data: 2026-04-20
3. Clique em "Buscar Voos"

### 2. Criar Reserva
1. Clique na aba "📋 Minhas Reservas"
2. Na seção "➕ Criar Nova Reserva":
   - CPF: 12345678901
   - Nome: João Silva
   - Número do Voo: 101
   - Data: 2026-04-20
3. Clique em "Criar Reserva"

### 3. Visualizar Minhas Reservas
1. Na aba "📋 Minhas Reservas"
2. Digite seu CPF: 12345678901
3. Clique em "Listar Minhas Reservas"

## Tratamento de Erros

O frontend trata automaticamente:
- Serviços SOAP indisponíveis
- Erros de validação
- Erros de conexão
- Campos vazios ou inválidos

## Desenvolvimento

Para ativar modo debug com auto-reload:

```bash
python app.py
```

O Flask detectará mudanças e recarregará automaticamente.

## Troubleshooting

### Erro: "Serviço indisponível"
- Verifique se os serviços SOAP estão rodando
- Confirme as portas 8000 e 8001
- Verifique a conectividade de rede

### Erro: "Import Flask could not be resolved"
- Certifique-se que o venv está ativado
- Execute: `pip install Flask Flask-CORS`

### Frontend não carrega
- Acesse http://localhost:5000 no navegador
- Verifique se o Flask está rodando (porta 5000)
- Verifique o console do navegador para erros JS

## Tecnologias Utilizadas

- **Flask** - Framework web Python
- **Zeep** - Cliente SOAP Python
- **HTML5 + CSS3 + JavaScript** - Frontend
- **Bootstrap-like CSS** - Estilização responsiva
