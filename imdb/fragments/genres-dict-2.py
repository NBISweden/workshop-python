#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
dbfile = os.path.dirname(os.path.realpath(__file__)) + '/../250.imdb'

genres = dict()
with open(dbfile,'r',encoding="utf-8") as db:

    first_line = db.readline()
    for line in db:
        blocks = line.split('|')
        for genre in blocks[5].split(','):
            key = genre[:6].upper()
            entry = genres.get(key,0)
            genres[key]= entry + 1


print('I found %d genres' % (len(genres)))
print('Those ones:\n', sorted(genres))
            
print('Sum Keys: ', len(genres.keys()))
print('Sum Values: ', sum(genres.values()))
