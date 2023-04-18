nome = input("Insira seu nome")
senha = input("Insira sua senha")

def validate(nome, senha):
    try:
        print(nome, senha)
    except:
        print("ERROR")    
        