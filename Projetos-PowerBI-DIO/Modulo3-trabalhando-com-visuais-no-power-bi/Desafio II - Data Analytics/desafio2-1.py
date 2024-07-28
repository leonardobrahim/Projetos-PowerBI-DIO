def remover_duplicatas(lista):
    # Cria um conjunto a partir da lista, removendo duplicatas
    conjunto_unico = set(lista)
    # Converte o conjunto de volta para uma lista
    lista_unica = list(conjunto_unico)
    return lista_unica

# Recebe a lista do usuário
entrada = input()
# Converte a string de entrada em uma lista de números
lista = [int(x.strip()) for x in entrada.split(',')]

lista_unica = remover_duplicatas(lista)
print(lista_unica)
