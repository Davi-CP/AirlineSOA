from wsgiref.simple_server import make_server
from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from services.reserva_service import ReservaService

Application = Application(
    [ReservaService],
    tns = "http://AirlineSOA.com/airline/reservas",
    in_protocol = Soap11(validator='lxml'),
    out_protocol = Soap11()
)


wsgi_application = WsgiApplication(Application)

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 8001
    server = make_server(host, port, wsgi_application)
    print(f"Servidor SOAP rodando em http://{host}:{port}")
    server.serve_forever()