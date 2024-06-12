""" 
Este código implementa um algoritmo genético simples para resolver o problema de otimização proposto. 
Ele começa com uma população inicial de indivíduos gerados aleatoriamente. Em cada geração, ele seleciona pais por torneio, 
realiza crossover aritmético para gerar a prole e aplica mutação. A população é então substituída pela nova geração. 
O algoritmo retorna o melhor indivíduo da última geração.
"""

import random

# Função objetivo
def f(x):
    return x**2 - 10*x + 25

# Gera um indivíduo aleatório
def generate_individual():
    return random.uniform(-5, 10)

# Calcula a aptidão de um indivíduo
def fitness(x):
    return f(x)

# Realiza o crossover aritmético
def crossover(x, y):
    return (x + y) / 2

# Realiza a mutação
def mutate(x):
    return x + random.uniform(-0.5, 0.5)

# Algoritmo genético
def genetic_algorithm():
    # Gera a população inicial
    population = [generate_individual() for _ in range(10000)]
    
    for _ in range(1000):  # 1000 gerações
        # Avalia a aptidão da população
        fitnesses = [fitness(x) for x in population] # Calcula a aptidão de cada indivíduo na população atual
        # Seleciona os pais por torneio
        parents = random.choices(population, weights=fitnesses, k=20) # A função random.choices é usada para selecionar aleatoriamente 20 pais da população atual. A probabilidade de um indivíduo ser escolhido como pai é proporcional à sua aptidão. Isso significa que os indivíduos com maior aptidão têm uma maior probabilidade de serem escolhidos como pais.
        
        # Gera a próxima geração por crossover e mutação
        next_generation = [mutate(crossover(random.choice(parents), random.choice(parents))) for _ in range(100)]
        
        # Substitui a população atual pela próxima geração
        population = next_generation
    
    # Retorna o melhor indivíduo da última geração
    return min(population, key=fitness)

best_individual = genetic_algorithm()
print(f'O melhor indivíduo encontrado foi x = {best_individual} com f(x) = {f(best_individual)}')