#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===================================
# Reformat 250.imdb into other format
# ===================================

def format_category( category, movies):
    '''Formats the category and movies
       like we were told to do in class'''

    c = '> ' + category + '\n'
    m = '\n'.join(movies)

    return c + m




with open('250.imdb', 'r', encoding='utf-8') as f_input,    \
     open('output.txt', 'w', encoding='utf-8') as f_output:

    f_output.write('# FORMAT:\n')
    f_output.write('# > CATEGORY\n')
    f_output.write('# Movie: Rating \t Name (Year)\n')


    # Main data structure
    categories = {}
    # Mapping: category => list of movies (already formatted)

    for line in f_input:
        
        if line.startswith('#'): # Not interested
            continue 

        # Get some info about that line
        fields = line.split('|')

        genres = fields[-2].upper().split(',') # List of strings (uppercase)
        title  = fields[-1].strip()            # clean it
        year   = fields[2].strip()             # it too
        rating = fields[1].strip()             # and it too, who knows...

        new_line = rating + '\t' + title + ' (' + year +')'

        for genre in genres: # uppercase already
            
            # Get the list of movies for that genre
            movies = categories.get(genre)
            if movies is None:
                categories[genre] = [new_line] # one item
            else:
                movies.append(new_line)


    # Done constructing the intermediate data structure
    # Can dump it into the output file now
    for cat,movies in categories.items():
        fc = format_category(cat,movies)
        f_output.write( fc )
        f_output.write('\n')
            

