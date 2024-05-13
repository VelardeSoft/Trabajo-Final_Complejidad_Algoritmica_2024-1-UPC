import pandas as pd
import networkx as nx
import folium

data = pd.read_csv('crimenes_febrero_2024.csv')

G = nx.Graph() # Grafo vacio

for index, row in data.iterrows():
    G.add_node(row['LOCATION'], pos=(row['LAT'], row['LON']))

mapa = folium.Map(location=[34.0522, -118.2437], zoom_start=11) #Visualización

for node in G.nodes:
    lat, lon = G.nodes[node]['pos']
    folium.CircleMarker(
        location=[lat, lon],
        radius=5, color='blue', fill_color='blue',
        fill=True,
        fill_opacity=1,  # Opacidad del relleno (0-1) 0 trasn, 1 opaco
        popup=node  # Muestra el nombre del área como popup
    ).add_to(mapa)

mapa.save('mapas.html')

def dfs (G, start, visited=None):  # Depth First Search aplicamos para analisis a profundidad
    if visited is None:
        visited = set()  # Visitar a cada nodo
    visited.add(start)

    print(start)
    for next in G[start]:
        if next not in visited:
            dfs(G, next, visited)
    return visited

