from db import HomeDB
from db import haversine as get_distance
from db import plot

lat=59.865795990339876
lng=17.64583576202392
radius=2000 # in m


db = HomeDB('uppsala.sqlite')
db.connect()
homes = db.select('rooms > 1 and rooms < 3 and area > 58 and rent < 3000')
db.disconnect()

#######################################
#                                     #     #
# THIS IS WHERE YOU INSERT YOUR CODE  #    ##
#                                     #   ###
#######################################  ################
#                                     # #################
selected = homes[:10]                 #  ################
cheapest = homes[0]                   #   ###
#                                     #    ##
#######################################     #

plot(selected,
     output = 'selection.html',
     cheapest = cheapest,
     zoom = 14,
     latitude=lat,
     longitude=lng,
     radius=radius, # in m
     google_key = 'AIzaSyDAfrqg2uOAkpem_B64PoQh8axACWGKe8U' 
)

print('Plot is in selection.html. Open that one')

# https://developers.google.com/maps/documentation/javascript/get-api-key
