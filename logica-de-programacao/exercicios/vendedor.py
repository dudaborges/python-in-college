nome = input("Nome: ")
salarioFixo = float(input("Salário fixo: "))
totalVendas = float(input("Total de vendas: "))
salarioFinal = (totalVendas * 0.15) + salarioFixo
print("TOTAL = ", round(salarioFinal, 2))
