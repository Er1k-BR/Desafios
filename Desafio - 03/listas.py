"""Criando Listas"""

times = ["Flamengo", "Corinthians", "São Paulo", "Real Madrid", "Bayer", "PSG"]
print(f"Lista de Times: {times}")

titulos = [100, 70, 85, 95, 95, 67]
print(f"Lista de Títulos: {titulos}")

"""Acessando elementos"""
print("\n- Acessando Listas - ")
print("Primeiro time:", times[0])
print("Último Time:", times[-1])
print("Sublista de Títulos:", titulos[0:4])


"""Interando com for"""
print("\n- Interando com for - ")
for time in times:
    print(f"O time atual é: {time}")


"""Interando com while"""
print("\n- Interando com while - ")
indice = 0
while indice < len(titulos):
    print(f"Titulo no indice {indice + 1}: {titulos[indice]}")
    indice += 1


"""Operações com listas"""
print("\n- Operações com Listas -")  # adiciona um novo item a lista
times.append("Santos")
print(f"\nApós uso do append: {times}")


times.remove("Bayer")  # remove um item da lista
print(f"\nApós o uso do remove: {times}")


times[1] = "UberLÂNDIA"  # altera um item da lista
print(f"\nApós o uso moficação: {times}")


nova_lista = times + ["Manchester United", "Manchester City"]  # concatena
print(f"\nApós concatenação: {nova_lista}")


print("\nExemplo de pilha:")  # implementando uma
times = []
times.append("Flamengo")  # Empilhar
times.append("Corinthians")
times.append("São Paulo")
print("Pilha após empilhar:", times)


ultimo = times.pop()  # Desempilhar
print("\nElemento desempilhado:", ultimo)
print("Pilha após desempilhar:", times)


print("\nOutras operações:")  # outras operações
titulos = [100, 120, 95, 50]
print("Tamanho da lista:", len(titulos))
print("Contém 8?", 8 in titulos)
titulos.sort()
print("Lista ordenada:", titulos)
titulos.reverse()
print("Lista invertida:", titulos)


print("\nLista aninhada:")  # lista aninehada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matriz)
print("Elemento [1][2]:", matriz[1][2])


print("\nList comprehension:")  # cria uma lista atráves de interações
quadrados = [x**2 for x in range(1, 6)]
print("Quadrados de 1 a 5:", quadrados)
