from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from zeep import Client
from zeep.exceptions import Fault
import os

app = Flask(__name__)
CORS(app)

# Configuração dos clientes SOAP
VOOS_WSDL = 'http://localhost:8000/?wsdl'
RESERVAS_WSDL = 'http://localhost:8001/?wsdl'

voos_client = None
reservas_client = None

# Conectar ao serviço de voos
try:
    print(f"[INFO] Tentando conectar ao serviço de voos em {VOOS_WSDL}...")
    voos_client = Client(wsdl=VOOS_WSDL)
    print("[INFO] ✅ Serviço de voos conectado com sucesso!")
except Exception as e:
    print(f"[ERRO] ❌ Falha ao conectar ao serviço de voos: {type(e).__name__}: {e}")
    print("[INFO] Certifique-se de que o servidor está rodando: python3.10 voos/server.py")

# Conectar ao serviço de reservas
try:
    print(f"[INFO] Tentando conectar ao serviço de reservas em {RESERVAS_WSDL}...")
    reservas_client = Client(wsdl=RESERVAS_WSDL)
    print("[INFO] ✅ Serviço de reservas conectado com sucesso!")
except Exception as e:
    print(f"[ERRO] ❌ Falha ao conectar ao serviço de reservas: {type(e).__name__}: {e}")
    print("[INFO] Certifique-se de que o servidor está rodando: python3.10 reservas/server.py")


@app.route('/')
def index():
    """Página inicial."""
    return render_template('index.html')


@app.route('/api/voos', methods=['POST'])
def buscar_voos():
    """Busca voos disponíveis."""
    try:
        data = request.json
        origem = data.get('origem', '')
        destino = data.get('destino', '')
        data_voo = data.get('data', '')

        if not voos_client:
            return jsonify({'erro': 'Serviço de voos indisponível'}), 503

        # Chamada ao serviço SOAP
        resultado = voos_client.service.voos(origem, destino, data_voo)
        
        # Converter resultado para formato JSON
        voos_list = []
        if resultado:
            if isinstance(resultado, list):
                voos_list = [dict(voo) for voo in resultado]
            else:
                voos_list = [dict(resultado)]

        return jsonify({'voos': voos_list})

    except Fault as f:
        return jsonify({'erro': f'Erro no serviço SOAP: {f}'}), 400
    except Exception as e:
        return jsonify({'erro': f'Erro ao buscar voos: {str(e)}'}), 500


@app.route('/api/minhas-reservas', methods=['POST'])
def minhas_reservas():
    """Lista reservas de um CPF específico."""
    try:
        data = request.json
        cpf = data.get('cpf', '')

        if not cpf:
            return jsonify({'erro': 'CPF é obrigatório'}), 400

        if not reservas_client:
            return jsonify({'erro': 'Serviço de reservas indisponível'}), 503

        # Chamada ao serviço SOAP
        resultado = reservas_client.service.listar_reserva_by_cpf(int(cpf))
        
        # Converter resultado para formato JSON
        reservas_list = []
        if resultado:
            if isinstance(resultado, list):
                reservas_list = [dict(reserva) for reserva in resultado]
            else:
                reservas_list = [dict(resultado)]

        return jsonify({'reservas': reservas_list})

    except Fault as f:
        return jsonify({'erro': f'Erro no serviço SOAP: {f}'}), 400
    except Exception as e:
        return jsonify({'erro': f'Erro ao buscar reservas: {str(e)}'}), 500


@app.route('/api/criar-reserva', methods=['POST'])
def criar_reserva():
    """Cria uma nova reserva."""
    try:
        data = request.json
        data_reserva = data.get('data_reserva', '')
        numero_voo = data.get('numero_voo', '')
        cpf = data.get('cpf', '')
        nome_passageiro = data.get('nome_passageiro', '')

        # Validar campos obrigatórios
        if not all([data_reserva, numero_voo, cpf, nome_passageiro]):
            return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

        if not reservas_client:
            return jsonify({'erro': 'Serviço de reservas indisponível'}), 503

        # Chamada ao serviço SOAP
        resultado = reservas_client.service.criar_reserva(
            data_reserva, 
            int(numero_voo), 
            int(cpf), 
            nome_passageiro
        )

        return jsonify({'mensagem': resultado})

    except Fault as f:
        return jsonify({'erro': f'Erro no serviço SOAP: {f}'}), 400
    except Exception as e:
        return jsonify({'erro': f'Erro ao criar reserva: {str(e)}'}), 500


@app.route('/api/deletar-reserva', methods=['POST'])
def deletar_reserva():
    """Deleta uma reserva."""
    try:
        data = request.json
        reserva_id = data.get('reserva_id', '')

        if not reserva_id:
            return jsonify({'erro': 'ID da reserva é obrigatório'}), 400

        if not reservas_client:
            return jsonify({'erro': 'Serviço de reservas indisponível'}), 503

        # Chamada ao serviço SOAP
        resultado = reservas_client.service.deletar_reserva(int(reserva_id))

        return jsonify({'mensagem': resultado})

    except Fault as f:
        return jsonify({'erro': f'Erro no serviço SOAP: {f}'}), 400
    except Exception as e:
        return jsonify({'erro': f'Erro ao deletar reserva: {str(e)}'}), 500


@app.route('/api/status', methods=['GET'])
def status():
    """Verifica status dos serviços."""
    status_voos = False
    status_reservas = False

    try:
        if voos_client:
            voos_client.service.ping()
            status_voos = True
    except Exception:
        pass

    try:
        if reservas_client:
            reservas_client.service.ping()
            status_reservas = True
    except Exception:
        pass

    return jsonify({
        'voos': status_voos,
        'reservas': status_reservas
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
