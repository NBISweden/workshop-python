#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
dbfile = os.path.dirname(os.path.realpath(__file__)) + '/../250.imdb'

genres = set()
with open(dbfile,'r',encoding="utf-8") as db:

    first_line = db.readline()
    for line in db:
        blocks = line.split('|')
        for genre in blocks[5].split(','):
            genres.add(genre[:6].upper())
            
print('I found %d genres' % (len(genres)))
print('Here they are:\n', sorted(genres))
