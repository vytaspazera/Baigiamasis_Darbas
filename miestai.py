from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim
import pickle


source = requests.get('https://lietuvai.lt/wiki/Lietuvos_miestai').text
soup = BeautifulSoup(source, 'html.parser')
tags = soup.find('table', class_='grazi')
a_tags = tags.find_all('a')

miestai = []
count = 1
for tag in a_tags:
    if count % 2 == 0 and len(tag.text) > 3:
        miestai.append(tag.text)
    count += 1

miestai.sort()
koordinates = []

for miestas in miestai:
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(miestas)
    koordinate_tuple = (location.latitude, location.longitude)
    koordinates.append(koordinate_tuple)

print(miestai)
print(koordinates)

issaugoti_sarasai = [miestai, koordinates]

with open("miestai_ir_koordinates.pkl", "wb") as pkl_out:
    pickle.dump(issaugoti_sarasai, pkl_out)

