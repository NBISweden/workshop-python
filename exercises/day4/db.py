#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO add popups for all markers, change color and shape of markers

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
        return u'<Home {} | {} @ {}, {} ({}, {}):->'.format(self.id, self.type, self.location, self.price, self.longitude, self.latitude)

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



def _marker(entry, special=False):
    """
    Creates the javascript code for a Google Maps Marker
    """
    if isinstance(entry,HomeEntry) and special:
        return '''
        var lonLat = new OpenLayers.LonLat({}, {})
           .transform(
             new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
             map.getProjectionObject() // to Spherical Mercator Projection
           );
        center = new OpenLayers.Marker(lonLat);
        center.icon.url = "http://www.pngall.com/wp-content/uploads/2017/05/Map-Marker-PNG-HD.png";
        markers.addMarker(center);
        '''.format(entry.longitude, entry.latitude)

    elif isinstance(entry,HomeEntry):
        return '''
        var lonLat = new OpenLayers.LonLat({}, {})
           .transform(
             new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
             map.getProjectionObject() // to Spherical Mercator Projection
           );
        markers.addMarker(new OpenLayers.Marker(lonLat));
        '''.format(entry.longitude, entry.latitude)

#        return '''var marker_{2} = new google.maps.Marker({{
# position: {{ lat: {0}, lng: {1} }},
# map: map,
# title: "id: {2}",
# icon: {4}
#}});
#var infowindow_{2} = new google.maps.InfoWindow({{ content: "{3}" }});
#google.maps.event.addListener(marker_{2}, 'click', function() {{ infowindow_{2}.open(map,marker_{2}); }});
#'''.format(entry.latitude, entry.longitude,entry.id,entry.to_html(),
#           'greenMakerIcon' if special else 'circleIcon')
#    raise ValueError("Not a good entry")


def plot(selection,
         google_key,
         output = 'selection.html',
         special = None,
         zoom = 12,
         latitude=59.83732598851705,
         longitude=17.64549846959149,
         radius=5000 # in m
):
    """
    Outputs the selection to map file.
    The center is given by latitude and longitude and marked on the map with a blue marker.
    The map draws a radius around the center.
    When the special is used, an extra green marker is ploted in the map.

    Note: this requires you to pass a Google Maps API key.
    You can fetch one here: https://developers.google.com/maps/documentation/javascript/get-api-key

    """

    #       var circle4326 = circularPolygon([x, y], radius, 64);
    #       var circle3857 = circle4326.clone().transform('EPSG:4326', 'EPSG:3857');
    #       vectorLayer4326.getSource().addFeature(new Feature(circle4326));
    start_html = """<html>
      <head>

      </head>
      <body>
      <div id="mapdiv"></div>
      <script src="http://www.openlayers.org/api/OpenLayers.js"></script>
      <script>
        map = new OpenLayers.Map("mapdiv");
        map.addLayer(new OpenLayers.Layer.OSM());
        map.options = {{units: 'm'}};
        circle = new OpenLayers.Geometry.Polygon({0}, {1});
        var lonLat = new OpenLayers.LonLat( {0}, {1} )
              .transform(
                new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
                map.getProjectionObject() // to Spherical Mercator Projection
              );

        var zoom={2};

        var markers = new OpenLayers.Layer.Markers( "Markers" );

        center = new OpenLayers.Marker(lonLat);
        center.icon.url = "http://www.pngall.com/wp-content/uploads/2017/05/Map-Marker-Free-PNG-Image.png";
        center.html = "<html>hej</html>";
        center.events.register("click", map, function(e){{console.log(e.object.html); createPopup(e.object)}});
        markers.addMarker(center);

        map.setCenter (lonLat, zoom);

        var vectorLayer = new OpenLayers.Layer.Vector("Overlay");

        var point = new OpenLayers.Geometry.Point(lonLat.lon, lonLat.lat);

        var mycircle = OpenLayers.Geometry.Polygon.createRegularPolygon
        (
            point,
            {3},
            40,
            0
        );
        var featurecircle = new OpenLayers.Feature.Vector(mycircle);

        var featurePoint = new OpenLayers.Feature.Vector(
            point
        );
        vectorLayer.addFeatures([featurePoint, featurecircle]);
        map.addLayer(vectorLayer);
        """.format(longitude, latitude, zoom, radius*2)

    end_html = '''
        map.addLayer(markers);
        </script>
      </body>
    </html>
    '''
    # You can add further markers using markers.addMarker(new OpenLayers.Marker(newLonLat)); if you define newLonLat to be another OpenLayers.LonLat object

    with open(output,'w',encoding='utf-8') as f:
        f.write(start_html)
        # f.write('''\
        # map.setCenter({{lat: {1}, lng: {2} }});
        # center.setPosition({{lat: {1}, lng: {2} }});
        # radius.setRadius({3});
        # map.setZoom({0});
        # '''.format(zoom, latitude, longitude, radius))

        for entry in selection:
            f.write(_marker(entry, special = special is entry))
            f.write('\n')

        f.write( end_html )
