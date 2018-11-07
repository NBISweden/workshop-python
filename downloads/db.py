#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO add popups for all markers

import cgi
import sqlite3
from math import radians, cos, sin, asin, sqrt

FIELDS = [ "id", "type", "location", "address", "date", "asked_price", "price", "rooms", "area", "rent", "latitude", "longitude" ]
DEFAULT_QUERY = 'SELECT id,type,location,address,date,asked_price,price,rooms,area,rent,latitude,longitude FROM objects'


def sort_by_price(houses, reverse=False):
    """
    Sorts  a list of homes by price.
    Returns the sorted list, from cheapest to most expensived (when reverse=True)
    """
    return list(sorted(houses, key=lambda x: x.get_price(), reverse=reverse))


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
        return u'<Home {} | {} @ {}, {:,.2f}:- ({}, {})>'.format(self.id, self.type, self.location, self.price, self.longitude, self.latitude)

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
    marker = "-gold" if special else ""
    return """ var feature = new OpenLayers.Feature.Vector(
            new OpenLayers.Geometry.Point( {}, {}).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject()),
            {{description: "{}"}} ,
            {{externalGraphic: 'http://dev.openlayers.org/img/marker{}.png', graphicHeight: 25, graphicWidth: 21, graphicXOffset:-12, graphicYOffset:-25  }}
             );    
           vectorLayer.addFeatures(feature);
           """.format(entry.longitude, entry.latitude, cgi.escape(str(entry)), marker)


def plot(selection,
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

    """
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
        var controls = {
           selector: new OpenLayers.Control.SelectFeature(vectorLayer, { onSelect: createPopup, onUnselect: destroyPopup })
        };
        function createPopup(feature) {
          feature.popup = new OpenLayers.Popup.FramedCloud("pop",
            feature.geometry.getBounds().getCenterLonLat(),
            null,
            '<div class="markerContent">'+feature.attributes.description+'</div>',
            null,
            true,
            function() { controls['selector'].unselectAll(); }
          );
          map.addPopup(feature.popup);
        }

        function destroyPopup(feature) {
          feature.popup.destroy();
          feature.popup = null;
        }
        
        map.addControl(controls['selector']);
        controls['selector'].activate();
        map.addLayer(markers);
        </script>
      </body>
    </html>
    '''

    with open(output,'w',encoding='utf-8') as f:
        f.write(start_html)
        for entry in selection:
            f.write(_marker(entry, special = special is entry))
            f.write('\n')

        f.write( end_html )
