import folium # Importamos la librería folium
import pandas as pd # Importamos la librería pandas

archivo = pd.read_csv("crimenes_febrero_2024.csv")

mapa = folium.Map(location=[34.0522, -118.2437], zoom_start = 11)  # Locations

for index, row in archivo.iterrows():
    popup_content = f"""
    <h5>-------  DELLATE DEL CRIMEN  -------</h5>
    <p> Area: {row['AREA-NAME']}</p>
    <p> Descripción: {row['Crm Cd Desc']}</p>
    <p> Fecha del crimen: {row['DATE OCC']}</p>
    <p> Hora del crimen: {row['TIME OCC']}</p>
    <p> Ubicación: {row['LOCATION']}</p>
    <h5> -------  DATOS DEL VICTIMA  -------</h5>
    <p> Edad: {row['Vict Age']} años</p>
    <p> Sexo: {row['Vict Sex']}</p>
    <p> Estado del caso: {row['Status']}</p>
    """
    folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=folium.Popup(html=popup_content, max_width=2650),
    ).add_to(mapa)

mapa.save('img/mapas.html')
