pilha = []

def empilhar():
    dado = input("Insira o dado a ser empilhado: ")
    pilha.append(dado)
    return pilha

def desimpilhar():
    if len(pilha) != 0:
        pilha.pop()
        return pilha
    else:
        print("A pilha está vazia!")

def limpar():
    pilha.clear()
    return

def mostrar():
    return pilha

option = 0
def options(option):

    if option == 1:
        print('\n\033[1;30;46mEmpilhar:\33[m\n')
        print(empilhar())

    elif option == 2:
        print('\n\033[1;30;41mDesimpilhar:\33[m\n')
        print(desimpilhar())
    elif option == 3:
        print('\n\033[1;30;42mLimpar:\33[m\n')
        print(limpar())
    elif option == 4:
        print('\n\033[1;30;42mPilha:\33[m\n')
        print(mostrar())
    elif option == 5:
        print('Saindo do programa...')
    else:
        print('\033[1;31;40m[ERROR] Option not found.\33[m')


while option != 5:
    print(f'\033[1;37;44m{" Pilhas ":=^50}\33[m')
    print('''
    [1] Empilhar
    [2] Desimpilhar
    [3] Limpar
    [4] Mostrar
    [5] Sair
    ''')
    option = int(input('insira a sua opção: '))
    options(option)
