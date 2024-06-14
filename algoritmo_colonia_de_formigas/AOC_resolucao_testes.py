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
dimensao = 5
valor_min = 1
valor_max = 50

# Distâncias entre as cidades 
distances = matriz_espelhada_aleatoria(dimensao, valor_min, valor_max)

# distances = np.loadtxt('matriz_adjacencia.txt', dtype=int)

# Parâmetros do ACO
num_cities = 5  # Número de cidades
num_ants = 2  # Número de formigas, definindo o número de soluções construídas por iteração
num_iterations = 100 # Número de iterações, quanto maior, mais tempo o algoritmo tem para explorar o espaço de soluções, mas também mais tempo para convergir
alpha = 1.0  # Importância dos feromônios
beta = 5.0  # Importância da visibilidade (inverso da distância)
evaporation_rate = 0.4  # Taxa de evaporação dos feromônios
initial_pheromone = 25.0  # Valor inicial dos feromônios
# Inicialização da matriz de feromônios
pheromones = np.full((num_cities, num_cities), initial_pheromone) # Inicializa a matriz de feromônios com o valor inicial

# Função para calcular a visibilidade (inverso da distância)
def calculate_visibility(distances):
    visibility = 1 / distances
    visibility[distances == 0] = 0  # Evitar divisão por zero, definindo visibilidade para distâncias iguais a zero como zero. Para cidade i, visibilidade[i, i] = 0
    return visibility

# Função para escolher a próxima cidade com base nas probabilidades
def choose_next_city(pheromones, visibility, current_city, visited):    
    probabilities = []
    for city in range(num_cities):
        if city not in visited:
            pheromone = pheromones[current_city, city] ** alpha
            vis = visibility[current_city, city] ** beta
            probabilities.append(pheromone * vis)
        else:
            probabilities.append(0)
    probabilities = probabilities / np.sum(probabilities)
    next_city = np.random.choice(range(num_cities), p=probabilities)
    return next_city

# Função principal do ACO para o TSP
def ant_colony_optimization(distances, num_ants, num_iterations, evaporation_rate):
    num_cities = distances.shape[0] # número de cidades
    pheromones = np.full((num_cities, num_cities), initial_pheromone)
    visibility = calculate_visibility(distances) # calcula a visibilidade 

    best_path = None
    best_path_length = float('inf')

    for iteration in range(num_iterations):
        all_paths = []
        for ant in range(num_ants):
            path = [np.random.randint(num_cities)] # cidade aleatória a percorrer
            while len(path) < num_cities:
                next_city = choose_next_city(pheromones, visibility, path[-1], path)
                path.append(next_city)
            path.append(path[0])  # Retornar à cidade de origem
            all_paths.append(path)

        for path in all_paths:
            path_length = sum(distances[path[i], path[i+1]] for i in range(num_cities))
            if path_length < best_path_length:
                best_path_length = path_length
                best_path = path

            for i in range(num_cities):
                pheromones[path[i], path[i+1]] += 1.0 / path_length

        pheromones *= (1 - evaporation_rate)

    return best_path, best_path_length


best_path, best_path_length = ant_colony_optimization(distances, num_ants, num_iterations, evaporation_rate)

print(best_path)