from zeep import Client

wsdl = 'http://localhost:8000/?wsdl'
client = Client(wsdl=wsdl)

response = client.service.ping()
print(response)