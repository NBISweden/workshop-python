#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==========================================
# Find and print the best movie per category
# ==========================================

with open('250.imdb', 'r', encoding='utf-8') as f:

    for line in f:
        
        if line.startswith('#'): # Not interested
            continue 

        # Get the fields as a list of strings
        fields = line.split('|')

        # Rename the fields, cuz I prefer, and convert them
        rating = float(fields[1])
        genres = fields[-2].lower().split(',') # List of strings also

        # Now what?
        # I need a global data structure to remember those values

        
        
        
