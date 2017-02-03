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

    def query(self,args=''):
        q = DEFAULT_QUERY
        if args:
            q = q + ' WHERE ' + args
        return self.raw_query(q)

