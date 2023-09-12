pilha = [1, 1, 2, 3, 5]
print("Pilha: ", pilha)

pilha.append(8)
print("Inserindo um elemento: ", pilha)

# pilha.clear()
# print("Limpando pilha: ", pilha)

pilha.append(13)
print("Inserindo outro elemento: ", pilha)

pilha.pop()
print("Removendo o elemento do topo: ", pilha)

print("Elemento do topo: ", pilha[-1])
print("Elemento do fundo: ", pilha[0])

print(pilha.top())

pilha.insert(0, 10)