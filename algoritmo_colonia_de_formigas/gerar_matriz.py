import numpy as np

def matriz_espelhada_aleatoria(dimensao, valor_min, valor_max):
    # Cria uma matriz com valores aleatórios
    matriz = np.random.randint(valor_min, valor_max/2, size=(dimensao, dimensao))
    
    # Define a diagonal principal como zero
    np.fill_diagonal(matriz, 0)

    # Espelha a matriz
    matriz_simetrica = (matriz + matriz.T)
    
    return matriz_simetrica

# Dimensão da matriz distancia entre as cidades, com o valor mínimo e máximo das distancias
dimensao = 10
valor_min = 1
valor_max = 50

# Distâncias entre as cidades 
distances = matriz_espelhada_aleatoria(dimensao, valor_min, valor_max)

print(distances)