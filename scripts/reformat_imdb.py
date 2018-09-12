import sys

"""
Script that reformats an imdb file and writes it to another file
"""


def FormatSec(seconds):    # formats seconds to hours and minutes
    hours     = seconds/3600
    minutes   = (seconds - (3600*int(hours)))/60   
    return str(int(hours))+'h'+str(round(minutes))+'min'

def FormatMovie(movie):    # returns a string with the correct format for writing to file
    formMovie = str(movie[0])+'\t'+movie[1]+' ('+str(movie[2])+') ['+movie[3]+']\n'
    return formMovie


if len(sys.argv) == 3:
    fh        = open(sys.argv[1], 'r', encoding = 'utf-8')
    genreDict = {}  

    for line in fh:
        if not line.startswith('#'):
            cols   = line.strip().split('|')
            rating = float(cols[1].strip())
            year   = int(cols[2].strip())
            length = int(cols[3].strip())
            movie  = cols[6].strip()
            genre  = cols[5].strip()
            glist  = genre.split(',')
            for entry in glist:
                if not entry.lower() in genreDict:              # if genre in dictionary, add first movie
                    genreDict[entry.lower()] = []
                genreDict[entry.lower()].append([rating, movie, year, FormatSec(length)])
    fh.close()


    out = open(sys.argv[2], 'w', encoding = 'utf-8')
    for genre in genreDict:
        out.write('> '+genre.capitalize()+'\n')
        for movie in genreDict[genre]:
            out.write(FormatMovie(movie))
    out.close()

else:
    print('Number of arguments does not match')


