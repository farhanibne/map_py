import folium
my_map4 = folium.Map(location=[28.5011226,77.4099794],
                     zoom_start=12)
folium.Marker([28.5011226,77.4099794],
              popup='Delhi').add_to(my_map4)
folium.Marker([28.5011226,77.4099794],
              popup='dz').add_to(my_map4)

folium.PolyLine(locations=[(28.5011226,77.4099794),(28.5011226,77.4099794)],
                line_opacity= 0.5).add_to(my_map4)

my_map4.save("my_map4.html")
my_map4
