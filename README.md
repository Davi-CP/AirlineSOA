# Plataforma para reserva de passagens de companhia aérea usando a arquitetura SOA

## Pré-requisitos

- Python 3.10 instalado (confira com `python --version`).
- Git instalado.

## Passos para rodar o projeto

### 1. Clone o repositório
```
git clone [text](https://github.com/Davi-CP/AirlineSOA.git)
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