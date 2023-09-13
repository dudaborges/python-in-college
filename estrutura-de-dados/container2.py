locais = [[] for _ in range(4)]
option = 0

def empilhar():
    codigo_container = int(input('Insira o código do container: '))
    local_minimo = min(locais)
    if len(local_minimo) <= 3:
        local_minimo.append(codigo_container)
    print(f'\n \033[1;37;42m{" " * 10}{local_minimo}{" " * 10}\33[m \n')

def options(option):
    if option == 1:
        empilhar()

while option != 4:
    print(f'\033[1;37;44m{" Containers ":=^50}\33[m \n\n 1 - Empilhar \n 2 - Desimpilhar \n 3 - Mostrar locais \n 4 - Sair do programa\n')

    option = int(input("Escolha uma opção: "))
    options(option)
    print('-=' * 25, '\n')