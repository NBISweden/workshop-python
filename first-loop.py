#!/usr/bin/env python3
# -*- coding: utf-8 -*-


remember_todo = ['Get the kids from school',
                 'Buy groceries',
                 'Fill up the car tank',
                 'Call mum',
                 'Pay the electricity bill',
                 'Read a swedish book with å,ä,ö',
                 r'escape the special character like \n and \t',
                 'Call mum again',  # Look...an extra comma...
                                    # No problem for Python
]

fake_line = '=' * 20

print( fake_line )

for item in remember_todo:
    print( 'Remember to', item.lower() ) 

print( fake_line )

