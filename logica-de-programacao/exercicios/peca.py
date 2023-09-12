numPeca1 = int(input("[Peça 1] Código: "))
uniPeca1 = int(input("[Peça 1] Número de peças: "))
valorPeca1 = float(input("[Peça 1] Valor unitário: "))
numPeca2 = int(input("[Peça 2] Código: "))
uniPeca2 = int(input("[Peça 2] Número de peças: "))
valorPeca2 = float(input("[Peça 2] Valor unitário: "))
peca1 = uniPeca1 * valorPeca1
peca2 = uniPeca2 * valorPeca2
print("[PEÇA 1] VALOR A PAGAR: R$", round(peca1, 2))
print("[PEÇA 2] VALOR A PAGAR: R$", round(peca2, 2))