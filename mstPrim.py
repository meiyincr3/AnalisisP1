import heapq
import random

graphDemo = [
    [(1, (10, 20)), (2, (15, 25))],  # Nodo 0
    [(0, (10, 20)), (2, (30, 40)), (3, (35, 45))],  # Nodo 1
    [(0, (15, 25)), (1, (30, 40)), (3, (50, 60)), (4, (55, 65))],  # Nodo 2
    [(1, (35, 45)), (2, (50, 60)), (4, (70, 80))],  # Nodo 3
    [(2, (55, 65)), (3, (70, 80))]  # Nodo 4
]

def create_random_graph(num_vertices, min_weight, max_weight):
    graph = [[] for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            weight = (random.randint(min_weight, max_weight), random.randint(min_weight, max_weight))
            weight = tuple(sorted(weight))  # Ordenar los valores del peso de menor a mayor
            graph[i].append((j, weight))
            graph[j].append((i, weight))
    
    return graph


def print_graph(graph):
    num_vertices = len(graph)
    
    for i in range(num_vertices):
        print(f"Nodo {i}:")
        for neighbor, weight in graph[i]:
            print(f"  -> Nodo {neighbor}, Peso: {weight}")

def primMenor(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = []
    aem = []
    
    # Seleccionar un nodo inicial arbitrario
    start_vertex = 0
    visited[start_vertex] = True
    
    # Agregar todas las aristas del nodo inicial a la cola de prioridad
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(min_heap, (weight, start_vertex, neighbor))
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        
        if visited[v]:
            continue
        
        # Agregar la arista al AEM
        aem.append((u, v, weight))
        visited[v] = True
        
        # Agregar todas las aristas del nodo recién conectado a la cola de prioridad
        for neighbor, weight in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, v, neighbor))
    
    return aem







def primMayor(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = []
    aem = []
    
    # Seleccionar un nodo inicial arbitrario
    start_vertex = 0
    visited[start_vertex] = True
    
    # Agregar todas las aristas del nodo inicial a la cola de prioridad
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(min_heap, (weight[1], start_vertex, neighbor))  # Utilizar el segundo valor (máximo) del peso como prioridad
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        
        if visited[v]:
            continue
        
        # Agregar la arista al AEM
        aem.append((u, v, weight))  # Agregar el segundo valor (máximo) del peso al AEM
        visited[v] = True
        
        # Agregar todas las aristas del nodo recién conectado a la cola de prioridad
        for neighbor, weight in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight[1], v, neighbor))  # Utilizar el segundo valor (máximo) del peso como prioridad
    
    return aem




def primPromedio(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = []
    aem = []
    
    # Seleccionar un nodo inicial arbitrario
    start_vertex = 0
    visited[start_vertex] = True
    
    # Agregar todas las aristas del nodo inicial a la cola de prioridad
    for neighbor, weight in graph[start_vertex]:
        avg_weight = (weight[0] + weight[1]) / 2  # Calcular el promedio de los valores del intervalo
        heapq.heappush(min_heap, (avg_weight, start_vertex, neighbor))  # Utilizar el promedio como prioridad
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        
        if visited[v]:
            continue
        
        # Agregar la arista al AEM
        avg_weight = (weight + weight) / 2  # Calcular el promedio de los valores del intervalo
        aem.append((u, v, avg_weight))  # Agregar el promedio al AEM
        visited[v] = True
        
        # Agregar todas las aristas del nodo recién conectado a la cola de prioridad
        for neighbor, weight in graph[v]:
            if not visited[neighbor]:
                avg_weight = (weight[0] + weight[1]) / 2  # Calcular el promedio de los valores del intervalo
                heapq.heappush(min_heap, (avg_weight, v, neighbor))  # Utilizar el promedio como prioridad
    
    return aem



graph = create_random_graph(5, 10, 50)
#aem1 = primMenor(graph)
#aem2 = primMayor(graph)
aem3 = primPromedio(graph)

#IMPRIME TODOS LOS DATOS
print_graph(graph)
print("/////////////////////////////////")
print(graph)
print("/////////////////////////////////")
#print(aem1)
print("/////////////////////////////////")
#print(aem2)
print("/////////////////////////////////")
print(aem3)