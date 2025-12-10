
## Padrões Estruturais

### 1. **Adapter Pattern**
**Localização:** `frontend/app.py` (linhas 18-40)

**Descrição:** O Zeep Client atua como adapter, convertendo chamadas Python em requisições SOAP.

```python
voos_client = Client(wsdl=VOOS_WSDL)  # Adapter entre Python e SOAP
resultado = voos_client.service.voos(origem, destino, data_voo)
```

**Utilidade:**
- Permite ao frontend trabalhar com objetos Python em vez de XML SOAP bruto
- Abstrai complexidade do protocolo SOAP
- Facilita integração entre diferentes sistemas

---

### 2. **Facade Pattern**
**Localização:** `voos/server.py` e `reservas/server.py`

**Descrição:** Spyne atua como fachada simplificando a exposição de serviços complexos.

```python
Application = Application(
    [VooService],
    tns="http://AirlineSOA.com/airline/voos",
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
```

**Utilidade:**
- Fornece interface SOAP unificada
- Gera WSDL automaticamente
- Valida requisições (lxml)

---

### 3. **Proxy/Wrapper Pattern**
**Localização:** `reservas/services/reserva_service.py`

**Descrição:** Métodos de serviço atuam como proxies para lógica de domínio.

```python
@srpc(Unicode, Unicode, Integer, Unicode, _returns=Unicode)
def criar_reserva(data_reserva, numero_voo, cpf, nome_passageiro):
    return criar_reserva_domain(...)  # Proxy para a lógica real
```

**Utilidade:**
- Controla acesso à lógica de negócio
- Adiciona validação antes de chamar domínio

---

## Padrões Criacionais

### 1. **Factory Pattern**
**Localização:** `db/seed.py` e `db/db.py`

**Descrição:** Funções de seed criam/populam dados de forma padronizada.

```python
def seed_voos(con):
    # Factory que cria estrutura de voos
    voos = [
        ("AZ1001", "POA", "GRU", "2025-12-10", ...),
        ("G31002", "GRU", "RIO", "2025-12-10", ...),
    ]
    cur.executemany(...)
```

**Utilidade:**
- Encapsula lógica de criação de dados
- Reutilizável

---

### 2. **Singleton Pattern**
**Localização:** `frontend/app.py`

**Descrição:** Instâncias únicas dos clientes SOAP durante a vida da aplicação.

```python
voos_client = None
reservas_client = None

# Inicializados uma única vez
voos_client = Client(wsdl=VOOS_WSDL)
reservas_client = Client(wsdl=RESERVAS_WSDL)
```

**Utilidade:**
- Garante uma única conexão com cada serviço
- Economiza recursos
- Evita múltiplas inicializações

---

### 3. **Data Transfer Object (DTO) / Value Object**
**Localização:** `voos/models/voo_model.py` e `reservas/models/reserva_model.py`

**Descrição:** Spyne ComplexModel atua como padrão criacional de estruturas de dados.

```python
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
```

**Utilidade:**
- Encapsula criação de objetos de dados
- Garante tipagem
- Facilita serialização/desserialização

---

## Padrões Comportamentais

### 1. **Strategy Pattern**
**Localização:** `reservas/services/reserva_service.py`

**Descrição:** Diferentes estratégias de operação (criar, listar, deletar) encapsuladas.

```python
@srpc(Unicode, Unicode, Integer, Unicode, _returns=Unicode)
def criar_reserva(...):
    return criar_reserva_domain(...)

@srpc(Integer, _returns=Iterable(Reserva))
def listar_reservas(cpf):
    return listar_reservas_domain(cpf)

@srpc(Integer, _returns=Unicode)
def deletar_reserva(reserva_id):
    return deletar_reserva_domain(reserva_id)
```

**Utilidade:**
- Cada operação é uma estratégia independente
- Facilita adicionar novas estratégias (ex: atualizar_reserva)
- Separa algoritmos diferentes

---

### 2. **Template Method Pattern**
**Localização:** `reservas/repository/reserva_repository.py`

**Descrição:** Estrutura comum para operações de banco de dados.

```python
def inserir_reserva(numero_voo, cpf, data_reserva, status, criado_em):
    con = sqlite3.connect(str(DB_PATH))
    try:
        cursor = con.cursor()
        cursor.execute(...)  # Passo comum
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()  # Template: sempre fechar conexão
```

**Utilidade:**
- Padrão comum: connect → execute → commit → close
- Garante consistência
- Previne vazamento de conexões

---

### 3. **Command Pattern**
**Localização:** `frontend/app.py` (rotas Flask)

**Descrição:** Requisições HTTP são encapsuladas como comandos.

```python
@app.route('/api/criar-reserva', methods=['POST'])
def criar_reserva():
    # Comando encapsulado que será executado

@app.route('/api/deletar-reserva', methods=['POST'])
def deletar_reserva():
    # Outro comando
```

**Utilidade:**
- Encapsula requisição como objeto
- Permite enfileirar, undo, redo (extensível)
- Separa invocador (rota) do executor (service)

---

### 4. **Decorator Pattern**
**Localização:** `frontend/app.py` e `reservas/services/reserva_service.py`

**Descrição:** Flask e Spyne usam decoradores para adicionar funcionalidade.

```python
@app.route('/api/voos', methods=['POST'])  # Decorator Flask
def buscar_voos():
    ...

@srpc(Unicode, Unicode, Unicode, _returns=Iterable(Voo))  # Decorator Spyne
def voos(origem, destino, data):
    ...
```

**Utilidade:**
- Adiciona metadados sem modificar código
- Roteamento automático (Flask)
- Geração de WSDL automática (Spyne)

---

### 5. **Observer Pattern**
**Localização:** `frontend/app.py` (rota `/api/status`)

**Descrição:** Frontend monitora status dos serviços.

```python
@app.route('/api/status', methods=['GET'])
def status():
    status_voos = False
    status_reservas = False
    
    try:
        if voos_client:
            voos_client.service.ping()
            status_voos = True
    except Exception:
        pass
```

**Utilidade:**
- Frontend observa saúde dos serviços
- Notifica cliente via JSON

---

### 6. **Chain of Responsibility Pattern**
**Localização:** `frontend/app.py` (tratamento de exceções)

**Descrição:** Erros são tratados em camadas.

```python
@app.route('/api/voos', methods=['POST'])
def buscar_voos():
    try:
        # ... lógica
        resultado = voos_client.service.voos(...)
    except Fault as f:
        return jsonify({'erro': f'Erro SOAP: {f}'}), 400
    except Exception as e:
        return jsonify({'erro': f'Erro genérico: {str(e)}'}), 500
```

**Utilidade:**
- Tratamento em cascata de exceções
- Primeiro trata Fault (SOAP), depois genérica

---

## Resumo

### Tabela de Padrões por Categoria

| Categoria | Padrão | Localização | Utilidade |
|-----------|--------|-------------|-----------|
| **Estrutural** | Adapter | zeep.Client | Converte Python ↔ SOAP |
| **Estrutural** | Facade | Spyne Application | Simplifica interface SOAP |
| **Estrutural** | Proxy | ReservaService | Controla acesso à lógica |
| **Criacional** | Factory | db/seed.py | Cria dados padronizados |
| **Criacional** | Singleton | frontend/app.py | Instância única de clientes |
| **Criacional** | DTO/VO | Models | Estrutura dados tipados |
| **Comportamental** | Strategy | ReservaService | Operações diferentes |
| **Comportamental** | Template Method | Repository | Padrão BD consistente |
| **Comportamental** | Command | Flask routes | Requisições como objetos |
| **Comportamental** | Decorator | Flask/Spyne | Adiciona funcionalidade |
| **Comportamental** | Observer | /api/status | Monitora serviços |
| **Comportamental** | Chain of Resp. | Exception handling | Tratamento em cascata |

