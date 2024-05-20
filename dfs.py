import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
import pandas as pd
import webbrowser

def mapas_1():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    url = 'D://Python//Trabajo-Final_Complejidad_Algoritmica_2024-1-UPC\\mapas.html'
    webbrowser.get(chrome_path).open(url)

data = pd.read_csv('crimenes_febrero_2024.csv')
cant_crimenes = data['AREA'].value_counts().to_dict()

grafo = { # Grafo con los nodos y sus conexiones con nodos vecinos
    1: [4, 2, 13, 3, 11],
    2: [1, 11, 6, 20, 7, 3],
    3: [14, 20, 7, 2, 1, 13, 12],
    4: [1, 13, 11],
    5: [18, 12],
    6: [7, 11, 2, 20, 15],
    7: [6, 20, 11, 2, 15],
    8: [14, 10],
    9: [10, 19, 16, 15],
    10: [9, 19, 8, 15, 17, 21],
    11: [2, 6, 1, 4, 7],
    12: [18, 3, 13, 14, 5],
    13: [3, 12, 18, 1, 4],
    14: [8, 7, 3, 12],
    15: [6, 7, 10, 9, 16],
    16: [15, 9, 19],
    17: [21, 19, 10],
    18: [12, 13, 5],
    19: [9, 10, 16, 15, 17],
    20: [7, 2, 6, 1, 3, 14],
    21: [17, 10]
}

G = nx.DiGraph(grafo)  # Creamos un grafo vacio

"""
for i in range(1, 22):
    print(f'Nodo {i}: {G.nodes[i]}')
"""
######################################################################

###################################  FINALY ###################################
def dfs(grafo, nodo_inicial, visitado):  # Función de recorrido en profundidad, visitado lista que almacena
    visitado.append(nodo_inicial)  # agrega como nodo visitado, print(nodo_inicial)
    for nodo_vecino in grafo[nodo_inicial]:
        if nodo_vecino not in visitado:
            dfs(grafo, nodo_vecino, visitado) # funcion recursiva

def start_dfs():
    visitados = []  #Lista vacia
    nodo_inicio = int(area.get())  # dato obtenido del formulario
    if 1 <= nodo_inicio <= 21:

        dfs(grafo, nodo_inicio, visitados)
        ########################
        # Asignar valores de crímenes a cada nodo en el grafo
        for node in G.nodes():
            G.nodes[node]['crimenes'] = cant_crimenes.get(node,0)  # Asignar el valor de crímenes del diccionario, con 0 como valor predeterminado si no existe

        # Crear lista de colores para los nodos
        nodo_colors = []
        for node in G.nodes():
            if node in visitados:
                if G.nodes[node]['crimenes'] >= 100:
                    nodo_colors.append('red')
                elif G.nodes[node]['crimenes'] >= 70:
                    nodo_colors.append('orange')
                else:
                    nodo_colors.append('green')
            else:
                nodo_colors.append('blue')

        ########################

        # Creamos una lista de aristas recorridas
        arista_resaltada = []
        for i in range(len(visitados) - 1):
            arista = (visitados[i], visitados[i + 1])
            arista_resaltada.append(arista)

        # Dibujamos el grafo
        pos = nx.spring_layout(G)  # Layout para posicionar los nodos
        nx.draw(G, pos, with_labels=True, node_color=nodo_colors, node_size=500)  # Nodos
        nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5) # Aristas
        nx.draw_networkx_edges(G, pos, edgelist=arista_resaltada, edge_color='green', width=3) # Aristas recorridas
        plt.show() # Mostrar el grafo en pantalla
    else:
        print("El area no existe")

#########################  FORMULARIO #######################
root = tk.Tk()  #ventana de formulario
root.title("My Formulario DFS")

label = tk.Label(root, text="Ingresa el nodo de inicio:")
label.pack() # Empaquetar o mostrar

root.geometry("400x150") #tamaño del formulario

area = tk.Entry(root)
area.pack()  # Toma el dato o numero ingresado

button = tk.Button(root, text="Iniciar", command = start_dfs)
button.pack()

button = tk.Button(root, text="Ver mapa", command = mapas_1)
button.pack()
#################################################################

G = nx.Graph(grafo)
root.mainloop()  # permitir que la interfaz gráfica responda a las acciones del usuario y se ejecute el programa
