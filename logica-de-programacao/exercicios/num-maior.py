valorA = int(input("Insira o valor A"))
valorB = int(input("Insira o valor B"))
valorC = int(input("Insira o valor C"))
maiorAB = (valorA + valorB + abs(valorA - valorB)) / 2
maiorABC = (maiorAB + valorC + abs(maiorAB - valorC)) / 2 
print("eh maior ", maiorABC)

