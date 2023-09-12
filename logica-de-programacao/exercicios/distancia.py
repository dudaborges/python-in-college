x1 = float(input("Insira o x1: "))
y1 = float(input("Insira o y1: "))
x2 = float(input("Insira o x2: "))
y2 = float(input("Insira o y2: "))
x = (x2 - x1) ** 2
y = (y2 - y1) ** 2
distancia = (x + y) ** (1/2)
print(round(distancia, 2))

