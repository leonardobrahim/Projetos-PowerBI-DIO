entrada = input()
lista = [float(x.strip()) for x in entrada.split(',')]

soma = sum(lista)
qtd = len(lista)
media = soma / qtd

print(f'{media:.1f}')


