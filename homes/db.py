#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from math import radians, cos, sin, asin, sqrt

FIELDS = [ "id", "type", "location", "address", "date", "asked_price", "price", "rooms", "area", "rent", "latitude", "longitude" ]
DEFAULT_QUERY = 'SELECT id,type,location,address,date,asked_price,price,rooms,area,rent,latitude,longitude FROM objects'


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance (in m) between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r * 1000 # in m

class HomeEntry():

    def __init__(self, row):
        for i in range(len(FIELDS)):
            setattr(self,FIELDS[i],row[i])

    def __repr__(self):
        return u'<Home {} | {} @ {}>'.format(self.id, self.type, self.location)

    def __str__(self):
        return self.__repr__()

    def to_html(self):
        return '<section><p>{}</p></section>'.format( '</p><p>'.join('{}: {}'.format(f,getattr(self,f)) for f in FIELDS) )

    def get_location(self):
        return (self.latitude,self.longitude)

    def get_price(self):
        return self.price

    def get_area(self):
        return self.area



class HomeDB():

    def __init__(self, db='' ):
        if not db:
            raise ValueError('Eh... No database?')
            
        self.__db = db
        self.__conn = None
        self.__cur = None

    def connect(self):
        self.__conn = sqlite3.connect(self.__db)
        self.__cur = self.__conn.cursor()

    def disconnect(self):
        if self.__conn:
            self.__conn.close()
        self.__conn = None
        self.__cur = None


    def raw_query(self, sql=DEFAULT_QUERY):
        if not sql:
            raise ValueError('Empty query')
        if self.__cur is None:
            raise ValueError('No db connection')

        try:
            return [HomeEntry(row) for row in self.__cur.execute(sql)]
        except sqlite3.Error as e:
            print("Error: {}".format(e.args[0]))
        return []

    def select(self,criteria=''):
        '''\
criteria can be about:
[ "id", "type", "location", "address", "date", "asked_price", "price", "rooms", "area", "rent", "latitude", "longitude" ]

For example:
"rooms > 1 and rooms < 3 and area > 58 and rent < 3000"

'''
        q = DEFAULT_QUERY
        if criteria:
            q = q + ' WHERE ' + criteria
        return self.raw_query(q)



def _marker(entry, cheapest=False):
    """
    Creates the javascript code for a Google Maps Marker
    """
    if isinstance(entry,HomeEntry):
        return '''var marker_{2} = new google.maps.Marker({{
 position: {{ lat: {0}, lng: {1} }},
 map: map,
 title: "id: {2}",
 icon: {4}
}});
var infowindow_{2} = new google.maps.InfoWindow({{ content: "{3}" }});
google.maps.event.addListener(marker_{2}, 'click', function() {{ infowindow_{2}.open(map,marker_{2}); }});
'''.format(entry.latitude, entry.longitude,entry.id,entry.to_html(),
           'greenMakerIcon' if cheapest else 'circleIcon')
    raise ValueError("Not a good entry")


def plot(selection,
         google_key,
         output = 'selection.html',
         cheapest = None,
         zoom = 12,
         latitude=59.83732598851705,
         longitude=17.64549846959149,
         radius=5000 # in m
):
    """
    Outputs the selection to map file.
    The center is given by latitude and longitude and marked on the map with a blue marker.
    The map draws a radius around the center.
    When the cheapest is used, an extra green marker is ploted in the map.

    Note: this requires you to pass a Google Maps API key.
    You can fetch one here: https://developers.google.com/maps/documentation/javascript/get-api-key

    """

    start_html = '''\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Uppsala Homes</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <style>
      #map { height: 100%; }
      html, body { height: 100%; margin: 0; padding: 0; }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      function initMap() {

      //var centerIcon = { path: google.maps.SymbolPath.CIRCLE, strokeColor: "black", fillColor: "red", scale: 3 }
      var centerIcon = "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
      var greenMakerIcon = "https://mt.googleapis.com/vt/icon/name=icons/onion/61-green-dot.png"
      var circleIcon = { path: google.maps.SymbolPath.CIRCLE, strokeColor: "red", scale: 2 }
      // var circleIcon = "https://storage.googleapis.com/support-kms-prod/SNP_2752129_en_v0"
      var map = new google.maps.Map(document.getElementById("map"),{ zoom: 12, center: {lat: 0, lng: 0 }});
      var centerWindow = new google.maps.InfoWindow();
      var center = new google.maps.Marker({ position: { lat: 0, lng: 0 }, map: map, title: "center", draggable:true, icon: centerIcon });
      center.addListener('click',function(){ 
          var p = center.getPosition();
          centerWindow.setContent('Lat: '+p.lat()+' <br/> Lng: '+p.lng());
          centerWindow.open(map,center);
      });
      var radius = new google.maps.Circle({ map: map, fillColor: '#f8cef9'});
      radius.bindTo('center', center, 'position');
'''

    end_html = '''
      }} // end initMap
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key={}&callback=initMap">
    </script>
  </body>
</html>
'''.format(google_key)

    with open(output,'w',encoding='utf-8') as f:
        f.write( start_html)
        f.write('''\
map.setCenter({{lat: {1}, lng: {2} }});
center.setPosition({{lat: {1}, lng: {2} }});
radius.setRadius({3});
map.setZoom({0});
'''.format(zoom, latitude, longitude, radius))

        for entry in selection:
            f.write(_marker(entry, cheapest = cheapest is entry))
            f.write('\n')

        f.write( end_html )
