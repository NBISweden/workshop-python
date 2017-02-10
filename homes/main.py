#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db import HomeDB
from db import haversine as get_distance
from db import plot
import argparse

default_lat=59.83732598851705
default_lng=17.64549846959149 
default_radius=5000 # in m

def work(args):
    """
    The main job: Connect to database, fetch rows with given criteria, outputs results in map file
    """

    db = HomeDB(args.db)
    db.connect()
    homes = db.select(args.query)
    db.disconnect()

    selected = []
    special = None

    for home in homes:
        latitude,longitude = home.get_location()
        d = get_distance(latitude, longitude, args.lat, args.lng)
        if d < args.radius:
            if not (special and home.get_price() >= special.get_price()):
                special = home
                
        selected.append(home)

    plot(selected,
         output = args.output,
         special = special,
         zoom = args.zoom,
         latitude=args.lat,
         longitude=args.lng,
         radius=args.radius, # in m
         google_key = 'AIzaSyC21XWgUbILZro3IfijyFTMwV3DUsLONGg'
    )
    # https://developers.google.com/maps/documentation/javascript/get-api-key



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
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=('''
\n
For example:
  %(prog)s -r 2000 \ 
          -q 'rooms > 1 and rooms < 3 and area > 58 and rent < 3000' \ 
          -l 59.865795990339876 -L 17.64583576202392 \ 
          -o me.html 
\n
'''))
    # parser = argparse.ArgumentParser()
    #parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-db',dest='db',     action='store', help='SQLite Database to read',                           default='uppsala.sqlite' )
    parser.add_argument('-l', dest='lat',    action='store', help='Latitude',                              type=float, default=default_lat      )
    parser.add_argument('-L', dest='lng',    action='store', help='Longitude',                             type=float, default=default_lng      )
    parser.add_argument('-z', dest='zoom',   action='store', help='Initial Zoom',                          type=int,   default=14               )
    parser.add_argument('-r', dest='radius', action='store', help='Distance from the center point, in m',  type=float, default=default_radius   )
    parser.add_argument('-q', dest='query',  action='store', help='Query [Eg: \'location = "Uppsala"\' ]',             default=''               )
    parser.add_argument('-o', dest='output', action='store', help='Output file [Default: %(default)s]',                default='map.html'       )

    args = parser.parse_args()
    work(args)

