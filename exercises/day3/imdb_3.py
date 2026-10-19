"""Question 3: write top 10 movies for a genre to CSV/TSV output file.

Usage:
    python exercises/day3/imdb_3.py GENRE OUTPUT_FILE [IMDB_FILE]
"""

from sys import argv


def parse_movie_line(line):
    """Parse one IMDb line into title, rating, and normalized genres.

    Args:
        line (str): A pipe-separated movie row from the IMDb file.

    Returns:
        dict[str, str | float | list[str]]: A dictionary with keys:
        - title (str): Movie title.
        - rating (float): Movie rating.
        - genres (list[str]): Lowercased genre names for the movie.
    """
    columns = line.strip().split("|")
    genres = [genre.strip().lower() for genre in columns[5].split(",") if genre.strip()]
    return {
        "title": columns[6].strip(),
        "rating": float(columns[1].strip()),
        "genres": genres,
    }


def parse_genre_matches(imdb_file, requested_genre):
    """Collect all movies from the file that match a requested genre.

    Args:
        imdb_file (TextIO): Open text file handle for pipe-separated IMDb data.
        requested_genre (str): Lowercased genre name to filter by.

    Returns:
        list[dict[str, str | float | list[str]]]: Matching movie dictionaries.
    """
    matches = []

    for line in imdb_file:
        if line.startswith("#"):
            continue

        movie = parse_movie_line(line)
        if requested_genre in movie["genres"]:
            matches.append(movie)

    return matches


def insert_movie_by_rating(top_movies, movie):
    """Insert one movie into a list sorted descending by rating.

    Args:
        top_movies (list[dict[str, str | float | list[str]]]): Movies sorted by rating.
        movie (dict[str, str | float | list[str]]): Movie dictionary to insert.

    Returns:
        None: The list is updated in place.
    """
    for index in range(len(top_movies)):
        if movie["rating"] > top_movies[index]["rating"]:
            top_movies.insert(index, movie)
            return

    top_movies.append(movie)


def trim_to_limit(top_movies, limit):
    """Trim a sorted movie list so it contains at most limit entries.

    Args:
        top_movies (list[dict[str, str | float | list[str]]]): Movies sorted by rating.
        limit (int): Maximum number of movies to keep.

    Returns:
        None: The list is updated in place.
    """
    if len(top_movies) > limit:
        top_movies.pop()


def get_top_movies(matches, limit):
    """Build a top-N list from matching movies using rating order.

    Args:
        matches (list[dict[str, str | float | list[str]]]): Movie dictionaries to rank.
        limit (int): Number of top-rated movies to keep.

    Returns:
        list[dict[str, str | float | list[str]]]: Up to limit movies sorted by rating.
    """
    top_movies = []

    for movie in matches:
        insert_movie_by_rating(top_movies, movie)
        trim_to_limit(top_movies, limit)

    return top_movies


def get_top_movies_for_genre(imdb_path, requested_genre, limit=10):
    """Read an IMDb file and return top-rated movies for one genre.

    Args:
        imdb_path (str): Path to the IMDb-style input file.
        requested_genre (str): Genre name from user input.
        limit (int): Maximum number of movies to return.

    Returns:
        list[dict[str, str | float | list[str]]]: Top movies sorted by rating.
    """
    requested_genre = requested_genre.strip().lower()

    with open(imdb_path, "r", encoding="utf-8") as imdb_file:
        matches = parse_genre_matches(imdb_file, requested_genre)

    return get_top_movies(matches, limit)


def infer_separator(output_path):
    """Infer output delimiter from file extension.

    Args:
        output_path (str): Path for the output file.

    Returns:
        str: "\t" for .tsv, "," for .csv, and "\t" by default.
    """
    separator = "\t"
    lowered = output_path.lower()
    if lowered.endswith(".tsv"):
        separator = "\t"
    elif lowered.endswith(".csv"):
        separator = ","
    return separator


def write_movies(output_path, movies):
    """Write movie titles and ratings to CSV/TSV file.

    Args:
        output_path (str): Path to the output file.
        movies (list[dict[str, str | float | list[str]]]): Movies with title and rating.

    Returns:
        None: Writes formatted text to disk.
    """
    separator = infer_separator(output_path)
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(f"title{separator}rating\n")
        for movie in movies:
            out_file.write(f"{movie['title']}{separator}{movie['rating']:.1f}\n")


def main():
    """Read CLI arguments, compute top movies, and write output file.

    Args:
        None.

    Returns:
        None.
    """
    if len(argv) < 3:
        raise SystemExit(
            "Usage: python exercises/day3/imdb_3.py GENRE OUTPUT_FILE [IMDB_FILE]"
        )

    requested_genre = argv[1]
    output_path = argv[2]
    imdb_path = argv[3] if len(argv) > 3 else "downloads/250.imdb"

    top_movies = get_top_movies_for_genre(imdb_path, requested_genre)
    write_movies(output_path, top_movies)
    print(f"Wrote {len(top_movies)} movies to {output_path}")


if __name__ == "__main__":
    main()
