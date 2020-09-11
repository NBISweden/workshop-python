#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zero= ["  ***  ",
       " *   * ",
       "*     *",
       "*     *",
       "*     *",
       " *   * ",
       "  ***  " ]

one=  ["   *   ",
       "  **   ",
       " * *   ",
       "   *   ",
       "   *   ",
       "   *   ",
       "  ***  " ]

two=  ["  ***  ",
       " *   * ",
       " *   * ",
       "    *  ",
       "   *   ",
       "  *    ",
       " ***** " ]

three=["  ***  ",
       " *   * ",
       "    *  ",
       "   *   ",
       "    *  ",
       " *   * ",
       "  ***  " ]

four= ["    *  ",
       "   **  ",
       "  * *  ",
       " ****  ",
       "    *  ",
       "    *  ",
       "    *  " ]

five= [" ***** ",
       " *     ",
       " *     ",
       " ***** ",
       "     * ",
       "     * ",
       " ***** " ]

six=  [" ***** ",
       " *     ",
       " *     ",
       " ***** ",
       " *   * ",
       " *   * ",
       " ***** " ]

seven=[" ***** ",
       "     * ",
       "     * ",
       "    *  ",
       "   *   ",
       "  *    ",
       " *     " ]

eight=[" ***** ",
       " *   * ",
       " *   * ",
       " ***** ",
       " *   * ",
       " *   * ",
       " ***** " ]

nine= [" ***** ",
       " *   * ",
       " *   * ",
       " ***** ",
       "     * ",
       "     * ",
       " ***** " ]

digits = [zero,one,two,three,four,five,six,seven,eight,nine] # nested lists

colon=["", "", "", "*", "", "*", "" ]


from time import localtime as get_time

now = get_time()

h1 = now.tm_hour // 10 # floor division
h2 = now.tm_hour % 10
m1 = now.tm_min // 10 # floor division
m2 = now.tm_min % 10


width = '=' * len(zero)
print( '{}'.format(width * 5) )

for i in range(len(colon)):
    print( '{}{}{:^6}{}{}'.format(digits[h1][i],
                                  digits[h2][i],
                                  colon[i],
                                  digits[m1][i],
                                  digits[m2][i])) 

print( '{}'.format(width * 5) )
