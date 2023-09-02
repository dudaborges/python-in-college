local1 =  []
local2 = []
local3 = []
local4 = []
# 4 locais (pilhas)
# máximo 3 containers (elementos) cada local (pilha)
#o container deve ser inserido na pilha (local) com menos elementos. len menos valor
def empilhar(local):
    for i in range(3):
        container = input("Insira o código do container: ")
        local1.append(container)
        print(local)

menorTamanho = min(len(local1), len(local2), len(local3), len(local4))

if len(local1) == menorTamanho:
    empilhar(local1)
    print(local1)
elif len(local2) == menorTamanho:
    print(local2)
elif len(local3) == menorTamanho:
    print(local3)
else:
    print(local4)