import pandas as pd
import networkx as nx
import folium

data = pd.read_csv('crimenes_febrero_2024.csv')

G = nx.Graph() # Grafo vacio para LOCATION
A = nx.Graph() # Grafo vacio para AREA-NAME

for index, row in data.iterrows():
    G.add_node(row['LOCATION'], pos=(row['LAT'], row['LON']), data=row.to_dict())
    A.add_node(row['AREA-NAME'], pos=(row['LAT'], row['LON']), data=row.to_dict())

mapa = folium.Map(location=[34.0522, -118.2437], zoom_start = 10) #Visualización

for node in G.nodes:
    lat, lon = G.nodes[node]['pos']
    data = G.nodes[node]['data']
    popup_text = (f"""
            <h5>----  DELLATE DEL CRIMEN  ----</h5>
            <p> Area: {data['AREA-NAME']}</p>
            <p> Descripción: {data['Crm Cd Desc']}</p>
            <p> Fecha del crimen: {data['DATE OCC']}</p>
            <p> Hora del crimen: {data['TIME OCC']}</p>
            <p> Ubicación: {data['LOCATION']}</p>
            <h5> ----  DATOS DEL VICTIMA  ----</h5>
            <p> Edad: {data['Vict Age']} años</p>
            <p> Sexo: {data['Vict Sex']}</p>
            <p> Estado del caso: {data['Status']}</p>
    """)
    folium.CircleMarker(
        location=[lat, lon],
        radius=5, color='blue', fill_color='blue',
        fill=True,
        fill_opacity=1,  # Opacidad del relleno (0-1) 0 trasn, 1 opaco
        popup=folium.Popup(popup_text, max_width=220),
    ).add_to(mapa)

for areas in A.nodes:
    lat, lon = A.nodes[areas]['pos']
    data = A.nodes[areas]['data']
    popup_text = (f"""
            <h5> ----  NOMBRE DE LA AREA  ---- </h5>
            <p> Area: {data['AREA-NAME']} </p>
            <p> NUMBER: {data['AREA']} </p>
    """)
    folium.CircleMarker(
        location=[lat, lon],
        radius=5, color='red', fill_color='red',
        fill=True,
        fill_opacity=1,  # Opacidad del relleno (0-1) 0 trasn, 1 opaco
        popup=areas
    ).add_to(mapa)
mapa.save('mapas.html')