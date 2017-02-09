#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

WORD_SEPARATORS = ' ();:,?!\n\t'

def _split_words_acc(words,pos):
    if pos >= len(WORD_SEPARATORS):
        return words
    else:
        acc = []
        for w in words:
            w_list = w.split(WORD_SEPARATORS[pos])
            acc.extend(w_list)
        return _split_words_acc(acc,pos+1)

def _split_words(line):
    #return line.split()
    words = _split_words_acc([line],0)
    result = []
    for w in words: 
        if w: # filter the empty words
            result.append(w)
    #print(result)
    return result
    

def _work(filename,search = None):

    lines_counter, words_counter, chars_counter = 0,0,0

    with open(filename,'r',encoding='utf-8') as f:
        
        for line in f:
            
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue

            if search is None or search == '--lines':
                lines_counter += 1

            if search is None or search == '--words':
                words = _split_words(line)
                words_counter += len(words)

            if search is None or search == '--characters':
                chars_counter += len(line) # no leading and trailing whitespaces, no \n

    # Outside the loop, I have now the counters ready.
    # Handling the display:

    if search == '--characters':
        print('{} contains {} characters'.format(filename, chars_counter) )

    if search == '--words':
        print('{} contains {} words'.format(filename, words_counter) )

    if search == '--lines':
        print('{} contains {} lines'.format(filename, lines_counter) )

    if search is None:
        sep = '-' * 64
        print('Filename:',filename.split('/')[-1])
        print(sep)
        print('|{:^20}|{:^20}|{:^20}|'.format('Lines','Words','Characters'))
        print(sep)
        print('|{:^20}|{:^20}|{:^20}|'.format(lines_counter,words_counter,chars_counter))
        print(sep)




def usage():
    print('''\
Usage: code.py <filename> [options]

Options are:
--------
--lines         displays the number of lines only
--words         displays the number of words only
--characters    displays the number of characters only

If no option is given, it displays all in a table like:

     
     Filename: <filename>
     -------------------------------------------
     |   Lines    |    Words   |  Characters   |
     -------------------------------------------
     |    12      |     345    |    67890      |
     -------------------------------------------

''')


if __name__ == '__main__':

    filename = None
    option = None
    
    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    if len(sys.argv) >= 3:
        option = sys.argv[2]

    if not filename or option not in ('--lines','--words','--characters',None):
        usage()
    else:        
        _work(filename, search = option) # option might be None

