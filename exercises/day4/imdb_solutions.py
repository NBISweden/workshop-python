"""
Example solutions for Exercise 1 day 4

This solution uses control statements as much as possible.
"""

imdb = "../../files/250.imdb"


def pick_movie_a(year=None, genre=None, min_rating=None, max_rating=None):
    for line in open(imdb):
        if line.startswith('#'):
            continue
        fields = line.split('|')
        # Remeber to type cast to float
        rating = float(fields[1].strip())
        title = fields[-1].strip()
        m_year = fields[2].strip()
        genres = fields[-2].strip().split(',')
        # Go through criterias. If the movie mathces an active criterion, print
        # it and break the loop
        if year and m_year == year:
            print(title)
            break
        if genre and genre in genres:
            print(title)
            break
        if min_rating and min_rating <= rating:
            print(title)
            break
        if max_rating and max_rating >= rating:
            print(title)
            break


def pick_movie_b(year=None, genre=None, min_rating=None, max_rating=None):
    for line in open(imdb):
        if line.startswith('#'):
            continue
        fields = line.split('|')
        # Remeber to type cast to float
        rating = float(fields[1].strip())
        title = fields[-1].strip()
        m_year = fields[2].strip()
        genres = fields[-2].strip().split(',')
        # Go through criterias and reject the movie if it doesn't fit
        if year and m_year != year:
            continue
        if genre and genre not in genres:
            continue
        if min_rating and min_rating > rating:
            continue
        if max_rating and max_rating < rating:
            continue
        # All criterias ok, print the movie and break the loop
        print(title)
        break


def pick_movie_b_ii(year=None, genre=None, min_rating=None, max_rating=None):
    for line in open(imdb):
        if line.startswith('#'):
            continue
        fields = line.split('|')
        # Remeber to type cast to float
        rating = float(fields[1].strip())
        title = fields[-1].strip()
        m_year = fields[2].strip()
        genres = fields[-2].strip().split(',')
        # Go through criterias and reject the movie if it doesn't fit
        ok_year = m_year == year or not year
        ok_genre = genre not in genres or not genre
        ok_min = min_rating > rating or not min_rating
        ok_max = max_rating < rating or not max_rating
        if ok_year and ok_genre and ok_min and ok_max:
            # All criterias ok, print the movie and break the loop
            print(title)
            break
