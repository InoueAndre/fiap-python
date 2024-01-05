from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
resultado = Geocoder('AIzaSyAIY0cogqbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco)
print(resultado)