A = float(round(input("Insira o valor A"), 1))
B = float(round(input("Insira o valor B"), 1))
C = float(round(input("Insira o valor C"), 1))

areaTriangulo = A * B
areaCirculo = (C * 2) * 3.14159
areaTrapezio = ((A + B) * C) / 2 
areaQuadrado = B * B
areaRetangulo = A * B

print("TRIANGULO: ", areaTriangulo, "CIRUCLO: ", areaCirculo, "TRAPEZIO: ", areaTrapezio, "QUADRADO: ", areaQuadrado, "RETANGULO: ", areaRetangulo)