#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:50:13 2023

@author: camillesaint-picq
"""
import pandas as pd
import folium
import os

df = pd.read_excel('/Users/camillesaint-picq/Desktop/Master/Geospatial/ARCTOX/Kap Hoegh .xlsx')

# Colonne qui prend en compte la date + time
df['DateTime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
df = df.sort_values(by='DateTime')

# Spécifiez l'ID souhaité
desired_bird_id = 148

# Filtrer les données pour l'oiseau avec l'ID souhaité
bird_data = df[df['ID'] == desired_bird_id]

# Créez une carte Folium centrée sur les limites calculées
m = folium.Map(location=[bird_data['Lat_compensate'].mean(), bird_data['Long'].mean()], zoom_start=12)

# Ajoutez une ligne reliant les points GPS
folium.PolyLine(locations=bird_data[['Lat_compensate', 'Long']].values, color='blue', weight=2.5, opacity=1).add_to(m)

# Ajoutez des points bleus aux points GPS
for _, row in bird_data.iterrows():
    folium.CircleMarker(location=[row['Lat_compensate'], row['Long']], radius=5, color='blue', fill=True, fill_color='blue').add_to(m)

# Affichez la carte Folium
m.save(f"carte_oiseau_{desired_bird_id}.html")

# Imprimez le répertoire de travail actuel
print("Répertoire de travail actuel:", os.getcwd())
