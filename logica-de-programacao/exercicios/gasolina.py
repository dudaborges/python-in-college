tempoViagem = int(input("Tempo gasto de viagem (em horas): "))
velocidadeMedia = int(input("Velocidade média (em km/h): "))
# 12 km/l
distancia = velocidadeMedia * tempoViagem
litros = distancia / 12
print("Quantidade de litros necessária: ", round(litros, 3), "KM/L")