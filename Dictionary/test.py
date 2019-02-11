import pandas
from geopy.geocoders import ArcGIS

nom=ArcGIS()

df=pandas.read_csv("supermarkets.csv")
df["Address"]=df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]

df["Coordinates"]=df["Address"].apply(nom.geocode)
df["latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)
