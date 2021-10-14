### Estimativa de cálculo de ponto cego dos radares de aeroportos

# Assumindo que o cone de detecção tem uma altura de 2000 metros e raio de 500 metros
volumeCone = 348454985161

# Assumindo um cilindro de detecção imaginário que tem uma altura de 11 km e raio de 5.5 km
volumeCilindro = 1393819940643

volumeCubo = 1331000000000 # metros cubicos

PontoCego = volumeCone/volumeCubo

# Com isso notamos que o cone representa 1/3 do volume de um cilindro de mesmo raio e altura. Dessa forma 2/3 do volume de detecção nesse volume passariam desapercebidos

print(1-PontoCego)