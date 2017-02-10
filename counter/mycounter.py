#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys


def work(filename,option):

    with open(filename, 'rt', encoding='utf-8') as f:

        lines_counter,words_counter,chars_counter = 0,0,0

        for line in f:
            lines_counter += 1
            line = line.strip()

            if line == '' or line.startswith(('#','/')):
                continue # skip

            words = line.split(' ')
            #print(words)
            words_counter += len(words)

            for word in words:
                chars_counter += len(word)
            
    # Now outside the loop
    # The file is now closed

    if option == '--lines':
        s = '{0} contains {1} lines'.format(
            filename,
            lines_counter)
        print(s)

    if option == '--words':
        s = '{0} contains {1} words'.format(
            filename,
            words_counter)
        print(s)

    if option == '--characters':
        s = '{0} contains {1} characters'.format(
            filename,
            chars_counter)
        print(s)

    if option is None:
        longline = '-' * 64
        print("Filename: ",filename.split('/')[-1]) # safe here
        #print(longline)
        #print('|  Lines  | Words  | Characters |')
        print( '|{:-^20}|{:-^20}|{:-^20}|'.format('Lines','Words','Characters') )
        #print(longline)
        print( '|{:^20}|{:^20}|{:^20}|'.format(lines_counter, words_counter, chars_counter) )
        #print('|  ',lines_counter,'  | ',words_counter,'  | ',chars_counter,' |')
        print(longline)




def print_usage():
    print('''\
Usage: mycounter <filename> [options]

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

    if not filename or option not in (
            '--lines',
            '--words',
            '--characters',
            None
    ):
        print_usage()
    else:
        work(filename,option) # option here might be None
