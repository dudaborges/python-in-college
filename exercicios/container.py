local1 =  []
local2 = []
local3 = []
local4 = []
# 4 locais (pilhas)
# máximo 3 containers (elementos) cada local (pilha)
#o container deve ser inserido na pilha (local) com menos elementos. len menos valor
menorTamanho = min(len(local1), len(local2), len(local3), len(local4))

for i in range(3):
    container = input("Insira o código do container: ")
    if len(local1) == menorTamanho:
        local1.append(container)
        print(local1)
    elif len(local2) == menorTamanho:
        local2.append(container)
        print(local2)
    elif len(local3) == menorTamanho:
        local3.append(container)
        print(local3)
    else:
        local4.append(container)
        print(local4)