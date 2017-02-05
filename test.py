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

digits = [zero,one,two,three,four,five,six,seven,eight,nine]

colon=["", "", "", "*", "", "*", "" ]


from time import localtime as get_time

now = get_time()

h1 = 0 if now.tm_hour < 10 else 1
h2 = now.tm_hour - 10 if now.tm_hour >= 10 else now.tm_hour
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
