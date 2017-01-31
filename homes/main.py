#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.db import HomeDB, HomeEntry
import argparse
from math import radians, cos, sin, asin, sqrt

default_lat=59.83732598851705
default_lng=17.64549846959149 
default_radius=5000 # in m

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


def marker(entry, cheapest=False):
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


def work(args):
    """
    The main job: Connect to database, fetch rows with given criteria, outputs results in map file
    """

    db = HomeDB(args.db)
    db.connect()
    all = db.query(args.query)
    db.disconnect()

    with open(args.output,'w',encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Uppsala Homes</title>
    <style>
      #map {{ height: 100%; }}
      /* Optional: Makes the sample page fill the window. */
      html, body {{
        height: 100%;
        margin: 0;
        padding: 0;
      }}
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      function initMap() {{

      //var centerIcon = {{ path: google.maps.SymbolPath.CIRCLE, strokeColor: "black", fillColor: "red", scale: 3 }}
      var centerIcon = "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
      var greenMakerIcon = "https://mt.googleapis.com/vt/icon/name=icons/onion/61-green-dot.png"
"http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
      var circleIcon = {{
        path: google.maps.SymbolPath.CIRCLE,
        strokeColor: "red",
        scale: 2
      }}
      // var circleIcon = "https://storage.googleapis.com/support-kms-prod/SNP_2752129_en_v0"
      var map = new google.maps.Map(document.getElementById("map"),{{
  zoom: {0},
  center: {{lat: {1}, lng: {2} }}
}});
var centerWindow = new google.maps.InfoWindow();
var center = new google.maps.Marker({{
  position: {{ lat: {1}, lng: {2} }},
  map: map,
  title: "center",
  draggable:true,
  icon: centerIcon 
}})
center.addListener('click',function(){{
var p = center.getPosition();
centerWindow.setContent('Lat: '+p.lat()+' <br/> Lng: '+p.lng());
centerWindow.open(map,center);
}});



var radius = new google.maps.Circle({{
  map: map,
  radius: {3},    // in meters
  fillColor: '#f8cef9'
  //strokeWeight:'2px'
  //fillOpacity: 0.5
}});
radius.bindTo('center', center, 'position');
'''.format(args.zoom, args.lat, args.lng, args.radius))

        selected = []
        cheapest = None
        for entry in all:
            d = haversine(entry.latitude, entry.longitude, args.lat, args.lng)
            #print('{} {:>20} {} < {}'.format('+' if d < args.radius else '-', entry.id, d, args.radius))
            if d < args.radius:
                if not (cheapest and entry.price >= cheapest.price):
                    cheapest = entry
                
                selected.append(entry)

        for entry in selected:
            f.write(marker(entry, cheapest = cheapest is entry))
            f.write('\n')

        f.write('''
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC21XWgUbILZro3IfijyFTMwV3DUsLONGg&callback=initMap">
    </script>
  </body>
</html>
''')


def find_center():
    """
    Find the centroid (barycenter) of all database entries
    """
    db = HomeDB('uppsala.sqlite')
    db.connect()
    all = db.query()
    db.disconnect()
    print(' Min Lat: ', min( entry.latitude for entry in all ))
    print(' Max Lat: ', max( entry.latitude for entry in all ))
    print(' Min Lng: ', min( entry.longitude for entry in all ))
    print(' Max Lng: ', max( entry.longitude for entry in all ))
    print(' Lat centroid: ', sum( entry.latitude for entry in all ) / len(all) )
    print(' Lng centroid: ', sum( entry.longitude for entry in all ) / len(all) )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-db',dest='db',     action='store', help='SQLite Database to read', default='uppsala.sqlite' )
    parser.add_argument('-l', dest='lat',    action='store', help='Latitude', required=False, type=float, default=default_lat )
    parser.add_argument('-L', dest='lng',    action='store', help='Latitude', required=False, type=float, default=default_lng )
    parser.add_argument('-z', dest='zoom',   action='store', help='Initial Zoom', type=int, default=14)
    parser.add_argument('-r', dest='radius', action='store', help='Distance from the center point, in m', type=float, default=default_radius )
    parser.add_argument('-q', dest='query',  action='store', help='Query [Eg: \'location = "Uppsala"\' ]', default='' )
    parser.add_argument('-o', dest='output', action='store', help='Output file [Defaults to %(default)]', default='map.html' )

    args = parser.parse_args()
    work(args)

# Example: python main.py -r 2000 -q 'rooms > 4.5' -l 59.85 -L 17.63




# python main.py -r 2000 -q 'rooms > 1 and rooms < 3 and area > 58 and rent < 3000' -l 59.865795990339876 -L 17.64583576202392 -o me.html
