### Estimativa de cálculo de ponto cego dos radares de aeroportos

# Assumindo que o cone de detecção tem uma altura de 2000 metros e raio de 500 metros
volumeCone = 523598776

# Assumindo um cilindro de detecção imaginário que tem uma altura de 2000 metros e raio de 500 metros
volumeCilindro = 1570796327

PontoCego = volumeCone/volumeCilindro

# Com isso notamos que o cone representa 1/3 do volume de um cilindro de mesmo raio e altura. Dessa forma 2/3 do volume de detecção nesse volume passariam desapercebidos

print(1-PontoCego)