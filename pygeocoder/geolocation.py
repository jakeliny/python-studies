from pygeocoder import Geocoder

endereco=input("Digite um endereco com número e cidade. \nExemplo: avenida paulista, 100 São Paulo:\n")
resultado = Geocoder('YOUR_API_KEY').geocode(endereco)
if resultado.valid_address == True:
    print("Endereço completo.: ", resultado)
    print("Coordenadas.......: ", resultado.coordinates)
    print("Número............: ", resultado.street_number)
    print("CEP...............: ", resultado.postal_code)

print("Foi(ram) encontrado(s) ",resultado.count, " endereço(s).")
for r in resultado:
    print("Cidade......: ", r.state)
    print("País........: ", r.country)
    print("Logradouro..: ", r.route)
    print("###########################")