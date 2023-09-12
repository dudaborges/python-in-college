locais = [[] for _ in range(4)]  
container_codes = set() 

def empilhar_container(codigo):
    if codigo in container_codes:
        print("Código inválido!")
    else:
        pilha_mais_baixa = min(locais, key=len)
        if len(pilha_mais_baixa) < 3:
            pilha_mais_baixa.append(codigo)
            container_codes.add(codigo)
            print(f"Container com código {codigo} empilhado com sucesso.")
        else:
            print("Impossível empilhar!")

def desempilhar_container(codigo):
    if codigo not in container_codes:
        print("Código inválido! O código não existe.")
    else:
        for pilha in locais:
            if pilha[-1] == codigo:
                pilha.pop()
                container_codes.remove(codigo)
                print(f"Container com código {codigo} removido com sucesso.")
                return
        print("Impossível desempilhar!")

def mostrar_estado():
    print("Estado atual das pilhas:")
    for i, pilha in enumerate(locais):
        print(f"Local {i + 1}: {pilha}")
    print("Códigos de containers existentes:", container_codes)

while True:
    print(f" {'/'*30} \n * GERENCIAMENTO DE CONTAINERS: * \n Opções: \n 1 - Empilhar container \n 2 - Desempilhar container \n 3 - Mostrar estado das pilhas \n 4 - Sair. \n {'/'*25}")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        codigo = input("Digite o código do container a empilhar: ")
        empilhar_container(codigo)
    elif escolha == "2":
        codigo = input("Digite o código do container a desempilhar: ")
        desempilhar_container(codigo)
    elif escolha == "3":
        mostrar_estado()
    elif escolha == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")