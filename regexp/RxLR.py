#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

def RxLR_search(filename):

    with open(filename, 'r', encoding='utf-8') as f:


        # ======================================
        print('First search: RxLR')
    
        p = re.compile('R.LR')

        for line in f:
            if line.startswith( ('>','\n') ):
                continue

            m = p.search(line)
            if m:
                print('\tMatch found: {} at position {}'.format(m.group(), m.span()) )


        # ======================================
        f.seek(0) # rewind first
        print('Second search: RxLR.*ERR')
    
        p = re.compile('R.LR.*ERR')

        for line in f:
            if line.startswith( ('>','\n') ):
                continue

            m = p.search(line)
            if m:
                print('Match found: {} at position {}'.format(m.group(), m.span()) )

        # ======================================
        f.seek(0) # rewind
        print('Third search: RxLR and then ERR')
    
        p1 = re.compile('R.LR')
        p2 = re.compile('ERR')

        for line in f:
            if line.startswith( ('>','\n') ):
                continue

            m1 = p1.search(line)
            if m1:
                print('\tMatch found: {} at position {}'.format(m1.group(), m1.span()) )

                for m2 in p2.finditer(line):

                    print('ERR found at position {}'.format( m1.span() ) )
                    if m1.end() < m2.start():
                        print('Gotcha!')

                else: # Note the else is for the for loop
                    print('\t\tbut not ERR')

    
if __name__ == "__main__":
    
    import sys
    try:
        RxLR_search(filename = sys.argv[1])
    except:
        print("I need a file to work on")
