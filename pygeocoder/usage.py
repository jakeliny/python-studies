from pygeocoder import Geocoder


endereco="1222, Lins de Vasconcelos, São Paulo, SP"
print(Geocoder('YOUR_API_KEY').geocode(endereco).coordinates)