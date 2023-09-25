# Scribbles by Richel.

if 1 == 2:
    import os
    print("Working directory: ", os.getcwd())


def get_imbd_filename():
    """Get the path to the IMDB file.
    
    Does not yet check if there exists a file at that path.

    Use copy of 250.imdb, as ../downloads/250.imdb does not work
    """
    return '250.imdb'

assert len(get_imbd_filename()) > 0

def get_imbd_file():
    """Get a file handle to the IMDB file
    
    Don't forget to use `close` on it!

    ```
    imbd_file = get_imbd_file()
    # [Do things with `imbd_file`]
    imbd_file.close() # Don't forget!
    ```
    
    """
    return open(get_imbd_filename(), 'r', encoding = 'utf-8')


def get_nth_col(col_index):
    fh = get_imbd_file()

    values = []
    for line in fh:
        # Ignore comments
        if line.startswith('#'): 
            continue
        cols = line.split('|')
        values.append(cols[col_index])
    fh.close()
    return values

assert len(get_nth_col(5)) > 0

def get_raw_unique_genres():
    """Get all unique genres in the IMDB

    Does not clean, nor sort the resulting unique genres.

    Cannot use `get_nth_col(5)`, because movies
    can be put into multiple genres.
    """    
    # E.g. 'Crime,Drama,Horror,Mystery,Thriller'
    comma_seperated_genres = get_nth_col(5)
    unique_genres = set()
    for comma_seperated_genre in comma_seperated_genres:
        genres = comma_seperated_genre.split(',')
        for genre in genres:

            unique_genres.add(genre)
    return unique_genres

assert len(get_raw_unique_genres()) > 0
assert len(get_raw_unique_genres()) == 24
assert not " Genres " in get_raw_unique_genres()


def get_unique_genres():
    """Get all unique genres in the IMDB

    Cannot use `get_nth_col(5)`, because movies
    can be put into multiple genres.
    """
    raw_genres = get_raw_unique_genres()
    unique_genres = set()
    for raw_genre in raw_genres:
        unique_genres.add(raw_genre.lower())    
    return unique_genres



assert len(get_unique_genres()) == 22

print(sorted(get_unique_genres()))

print("ALL WORKS")

