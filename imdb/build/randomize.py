#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
with open('250-org.imdb','r',encoding="utf-8") as db:

    first_line = db.readline()
    lines = [ line for line in db ]
    random.shuffle(lines)
    with open('250-shuffled.imdb', 'w',encoding="utf-8") as rdb:
        rdb.write(first_line)
        rdb.writelines(lines)
