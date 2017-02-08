#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==========================================
# Find and print the best movie per category
# ==========================================

with open('250.imdb', 'r', encoding='utf-8') as f:

    # For each category, I keep the best rating
    # Mapping { key: value } where   key = string
    #                              value = (int,string,string)
    categories = {} # Nothing at the start

    for line in f:
        
        if line.startswith('#'): # Not interested
            continue 

        # Get the fields as a list of strings
        fields = line.split('|')

        # Rename the fields, cuz I prefer, and convert them
        rating = float(fields[1])
        title = fields[-1].strip() # Clean the title
        genres = fields[-2].lower().split(',') # List of strings also
        
        for genre in genres:
            key = genre[:6]
            old_rating,old_title,old_genre = categories.get(key, (0.0,'','') ) # No KeyError

            if rating > old_rating: # found a better one
                categories[key] = (rating, title, genre.capitalize())
        
        
    # Print the categories
    for (rating,title,category) in categories.values():
        print("The best movie for",category,'\n\tis "',title,'"\n\tand has rating:',rating)
