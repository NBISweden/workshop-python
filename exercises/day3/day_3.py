"""Day 3 IMDb helper script.

Small utility functions used in the Day 3 exercises.
"""


def get_imdb_filename():
    """Get the path to the IMDb file.
    
    Does not yet check if there exists a file at that path.

    Use copy of 250.imdb, as ../downloads/250.imdb does not work
    """
    return "250.imdb"

assert len(get_imdb_filename()) > 0

def get_imdb_file():
    """Get a file handle to the IMDb file.
    
    Don't forget to use `close` on it!

    ```
    imdb_file = get_imdb_file()
    # [Do things with `imdb_file`]
    imdb_file.close() # Don't forget!
    ```
    
    """
    return open(get_imdb_filename(), "r", encoding="utf-8")


def get_imbd_filename():
    """Backward-compatible alias for typo in old teaching material."""
    return get_imdb_filename()


def get_imbd_file():
    """Backward-compatible alias for typo in old teaching material."""
    return get_imdb_file()


def get_nth_column(column_index):
    """Return one column from all non-comment IMDb rows."""
    values = []
    with get_imdb_file() as imdb_file:
        for line in imdb_file:
            if line.startswith("#"):
                continue
            columns = line.split("|")
            values.append(columns[column_index])
    return values


def get_nth_col(col_index):
    """Backward-compatible alias used in older notes."""
    return get_nth_column(col_index)

assert len(get_nth_col(5)) > 0

def get_raw_unique_genres():
    """Get all unique genres in the IMDb.

    Does not clean, nor sort the resulting unique genres.

    Cannot use `get_nth_col(5)`, because movies
    can be put into multiple genres.
    """    
    # E.g. 'Crime,Drama,Horror,Mystery,Thriller'
    comma_separated_genres = get_nth_col(5)
    unique_genres = set()
    for comma_separated_genre in comma_separated_genres:
        genres = comma_separated_genre.split(",")
        for genre in genres:
            unique_genres.add(genre)
    return unique_genres

assert len(get_raw_unique_genres()) > 0
assert len(get_raw_unique_genres()) == 24
assert not " Genres " in get_raw_unique_genres()


def get_unique_genres():
    """Get all unique genres in the IMDb.

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

