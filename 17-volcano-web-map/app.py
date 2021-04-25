import folium
import pandas as pd

# check folium
dir(folium)

# IMPORT FILES
polygons = open("17-volcano-web-map/world.json", encoding="utf-8-sig").read()
points = pd.read_csv("17-volcano-web-map/Volcanoes.txt")
points.columns
lat = list(points["LAT"])
lon = list(points["LON"])
elev = list(points["ELEV"])


# lambda functions
# one-liner functions
def l(x): return x**2


l(5)

# CREATE A MAP
# Cairngorms national park :)
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return "red"


# groups together related features, like markers, polygons, etc.
fgv = folium.FeatureGroup("Volcanoes")

for ln, lt, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[ln, lt], radius=6, fill_color=color_producer(el), color="grey",
                                     popup=str(el),
                 fill_opacity=0.7))

fgp = folium.FeatureGroup("Population")
fg.add_child(folium.GeoJson(
    data=polygons, style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 100000 <= x['properties']['POP2005'] else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("17-volcano-web-map/my-map.html")


'''[HTML on Popups]

Note that if you want to have stylized text (bold, different fonts, etc) in the popup window you can use HTML. Here's an example:

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = ''' < h4 > Volcano information: < /h4 >
Height: % s m
'''

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(
        iframe), icon = folium.Icon(color = "green")))


map.add_child(fg)
map.save("Map_html_popup_simple.html")
You can even put links in the popup window. For example, the code below will produce a popup window with the name of the volcano as a link which does a Google search for that particular volcano when clicked:

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = '''
Volcano name: < br >
<a href = "https://www.google.com/search?q=%%22%s%%22" target = "_blank" > %s < /a > <br >
Height: % s m
'''

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(
        iframe), icon = folium.Icon(color = "green")))

map.add_child(fg)
map.save("Map_html_popup_advanced.html")
    '''
