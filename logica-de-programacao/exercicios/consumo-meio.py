distanciaTotal = int(input("Distância total: "))
combustivelTotal = round(float(input("Total de combustível gasto: ")), 1)
consumoMedio =  distanciaTotal / combustivelTotal
print("Consumo médio: ", round(consumoMedio, 1))