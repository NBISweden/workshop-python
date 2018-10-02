from db import HomeDB
from db import haversine as get_distance
from db import plot

lat=59.865795990339876
lng=17.64583576202392
radius=2000 # in m


db = HomeDB('uppsala.sqlite')
db.connect()
homes = db.select()
#homes = db.select('rooms > 1 and rooms < 3 and area > 58 and rent < 3000')
db.disconnect()
print(len(homes))

homes.sort(key=lambda x: x.get_price())
central = [home for home in homes if get_distance(*home.get_location(), lat, lng)<=2000]

# selected_homes = homes[:10] #cheating       #  ################
selected_homes = central #[:10]
 

plot(selected_homes,
     output = 'selection.html',
     special = selected_homes[0],
     zoom = 14,
     latitude=lat,
     longitude=lng,
     radius=radius, # in m
     google_key = 'key'
)
# https://developers.google.com/maps/documentation/javascript/get-api-key

# print('Check the results in selection.html.')
# for special in selected_homes:
#     print('Special home: {}'.format(special))
