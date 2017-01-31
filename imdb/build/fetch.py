#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from imdbpie import Imdb

imdb = Imdb(verify_ssl=False,exclude_episodes=True,anonymize=True)
top250 = imdb.top_250()

# Output a list with little information
output = '250-short.imdb'
with open(output,'w',encoding="utf-8") as f:
    f.write(u"# Votes Rating Year URL Title\n")
    for movie in top250:
        f.write(u"{0:>10}\t{1:>6}\t{2}\t{4}\t{3!s}\n".format(movie['num_votes'], movie['rating'],movie['year'], movie['title'], movie['image']['url']))

# Output a list with all information. Fetching movies one at a time
output = '250.imdb'
with open(output,'w',encoding="utf-8") as f:
    f.write(u"# Votes Rating Year Runtime URL Genres Title\n")
    for movie in top250:
        #print('Fetching ({}): {} '.format(counter,movie['tconst']))
        title = imdb.get_title_by_id(movie['tconst'])
        f.write(u"{0:>10}|{1:>6}|{2}|{5}|{4}|{6}|{3!s}\n".format(
            movie['num_votes'],
            movie['rating'],
            movie['year'],
            movie['title'],
            movie['image']['url'],
            title.runtime,
            ','.join(title.genres)
        ))
