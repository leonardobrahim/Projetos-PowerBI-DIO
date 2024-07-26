numeros = list(map(float, input().split(',')))
numeros_ordenados = sorted(numeros)
n = len(numeros_ordenados)
ponto_medio = n // 2

if n % 2 == 1:
    mediana = numeros_ordenados[ponto_medio]
else:
    mediana = (numeros_ordenados[ponto_medio - 1] + numeros_ordenados[ponto_medio]) / 2

print(mediana)
