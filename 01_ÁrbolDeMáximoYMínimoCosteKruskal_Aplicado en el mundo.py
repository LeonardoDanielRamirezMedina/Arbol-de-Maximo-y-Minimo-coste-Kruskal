# Árbol de Máximo y Mínimo coste Kruskal  #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Simulador de Árbol de Máximo y Mínimo coste Kruskal - Aplicado en el mundo
# el arbol de maximo y minimo coste Kruskal es un algoritmo que se utiliza para encontrar un árbol de expansión mínima en un grafo conectado y ponderado.

import networkx as nx       # Librería para grafos
import matplotlib.pyplot as plt # Librería para graficar

class UnionFind:    # Clase para estructura de datos de conjuntos disjuntos
    def __init__(self, n):      # Inicializar la estructura con n elementos
        self.parent = list(range(n))    # Lista de padres de cada elemento
        self.rank = [1] * n            # Rango de cada conjunto

    def find(self, u):    # Encontrar el representante del conjunto de u
        if self.parent[u] != u:    # Si u no es el representante
            self.parent[u] = self.find(self.parent[u])  # Comprimir el camino
        return self.parent[u]   # Retornar el representante

    def union(self, u, v):  # Unir los conjuntos de u y v
        root_u = self.find(u)   # Encontrar el representante de u
        root_v = self.find(v)   # Encontrar el representante de v

        if root_u != root_v:    # Si no están en el mismo conjunto
            if self.rank[root_u] > self.rank[root_v]:   # Unir por rango
                self.parent[root_v] = root_u    # V se une a U
            elif self.rank[root_u] < self.rank[root_v]: # Unir por rango
                self.parent[root_u] = root_v    # U se une a V
            else:       
                self.parent[root_v] = root_u        # Unir por rango
                self.rank[root_u] += 1            # Incrementar el rango
            return True             # Se unieron los conjuntos
        return False            # Ya estaban en el mismo conjunto

def kruskal(n, edges):  # Algoritmo de Kruskal para MST
    # Ordenar aristas por peso
    edges.sort(key=lambda x: x[2])  # Ordenar por peso
    
    uf = UnionFind(n)   # Estructura de conjuntos disjuntos
    mst = []            # Aristas del MST
    mst_cost = 0    # Costo total del MST
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            mst_cost += weight
            # Si ya hemos incluido n-1 aristas, podemos salir
            if len(mst) == n - 1:
                break
    
    return mst, mst_cost

# Ejemplo de aplicación en la planificación de una red de carreteras entre ciudades
# Lista de aristas: (ciudad1, ciudad2, costo)
edges = [
    (0, 1, 10),  # Ciudad 0 a Ciudad 1 con costo 10
    (0, 2, 20),  # Ciudad 0 a Ciudad 2 con costo 20
    (1, 2, 30),  # Ciudad 1 a Ciudad 2 con costo 30
    (1, 3, 5),   # Ciudad 1 a Ciudad 3 con costo 5
    (2, 3, 15),  # Ciudad 2 a Ciudad 3 con costo 15
]

num_cities = 4  # Número total de ciudades
mst, mst_cost = kruskal(num_cities, edges)

# Creación del grafo usando networkx
G = nx.Graph()

# Añadir nodos (ciudades)
cities = ["Ciudad 0", "Ciudad 1", "Ciudad 2", "Ciudad 3"]   # Nombres de las ciudades
G.add_nodes_from(cities)    # Añadir nodos al grafo

# Añadir aristas del MST
for u, v, weight in mst:    # Recorrer las aristas del MST
    city_u = cities[u]    # Ciudad u
    city_v = cities[v]  # Ciudad v
    G.add_edge(city_u, city_v, weight=weight)   # Añadir arista con peso

# Obtener posiciones de los nodos para graficar
pos = nx.spring_layout(G)

# Dibujar el grafo
plt.figure(figsize=(10, 6)) # Tamaño del gráfico
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')       # Dibujar el grafo
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()}, font_color='red', font_size=10) # Etiquetas de las aristas

plt.title("Árbol de Expansión Mínima (MST) de una Red de Carreteras")   # Título del gráfico
plt.show()  # Mostrar el gráfico

print(f"Árbol de Expansión Mínima (MST) encontrado:")   # Imprimir el MST
print("Aristas en el MST:") # Imprimir las aristas del MST
for u, v, weight in mst:    # Recorrer las aristas del MST
    print(f"Ciudad {u} a Ciudad {v} con costo {weight}")    # Imprimir la arista
print(f"Costo total del MST: {mst_cost}")   # Imprimir el costo total del MST
