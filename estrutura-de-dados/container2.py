locais = [[] for _ in range(4)]
option = 0

while option != 4:
    print(f"\033[1;37;44m{" Containers ":=^50}\33[m \n\n 1 - Empilhar \n 2 - Desimpilhar \n 3 - Mostrar locais \n 4 - Sair do programa")

    option = int(input("Escolha uma opção: "))