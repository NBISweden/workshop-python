#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===================================
# Reformat 250.imdb into other format
# ===================================


with open('250.imdb', 'r', encoding='utf-8') as f_input,    \
     open('output.txt', 'w', encoding='utf-8') as f_output:

    f_output.write('# FORMAT:\n')
    f_output.write('# > CATEGORY\n')
    f_output.write('# Movie: Rating \t Name (Year)\n')


    for line in f_input:
        
        if line.startswith('#'): # Not interested
            continue 

        # Reformate that line
        # and put it somewhere to remember it with its category
