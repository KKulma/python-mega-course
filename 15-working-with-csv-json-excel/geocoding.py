
# original code
from geopy.geocoders import ArcGIS
import pandas as pd
# from geopy.geocoders import Nominatim
# nom = Nominatim()

# import file
pd_csv = pd.read_csv("15-working-with-csv-json-excel/supermarkets.csv")
pd_csv

# plan B
nom = ArcGIS()
geoloc = nom.geocode(
    f"{pd_csv.iloc[0, 1]}, {pd_csv.iloc[0, 3]}, {pd_csv.iloc[0, 2]}")  # geocoding!
type(geoloc)
geoloc[0]  # address that I passed
geoloc[1]  # geocoordinates
geoloc[1][0]

# data prep
pd_csv["full_address"] = pd_csv['Address'] + ", " + \
    pd_csv['City'] + ", " + pd_csv['State'] + ", " + pd_csv['Country']
pd_csv["coordinates"] = pd_csv["full_address"].apply(nom.geocode)
pd_csv["latitude"] = pd_csv["coordinates"].apply(
    lambda x: x.latitude if x != None else None)
pd_csv["longitude"] = pd_csv["coordinates"].apply(
    lambda x: x.longitude if x != None else None)
