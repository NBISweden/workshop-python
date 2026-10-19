"""Question 2: print average movie runtime per genre (in minutes)."""

from sys import argv


def parse_movie_line(line):
    """Parse one IMDb line into runtime and normalized genres.

    Args:
        line (str): A pipe-separated movie row from the IMDb file.

    Returns:
        dict[str, int | list[str]]: A dictionary with keys:
        - runtime_seconds (int): Movie runtime as number of seconds.
        - genres (list[str]): Lowercased genre names for the movie.
    """
    columns = line.strip().split("|")
    runtime_seconds = int(columns[3].strip())
    genres = [genre.strip().lower() for genre in columns[5].split(",") if genre.strip()]
    return {
        "runtime_seconds": runtime_seconds,
        "genres": genres,
    }


def add_movie_runtime_to_genres(movie, runtime_totals, genre_counts):
    """Accumulate one movie's runtime into per-genre totals and counters.

    Args:
        movie (dict[str, int | list[str]]): Parsed movie data with runtime and genres.
        runtime_totals (dict[str, int]): Maps genre to total runtime in seconds.
        genre_counts (dict[str, int]): Maps genre to number of movies seen.

    Returns:
        None: The provided dictionaries are updated in place.
    """
    for genre in movie["genres"]:
        if genre not in runtime_totals:
            runtime_totals[genre] = 0
        if genre not in genre_counts:
            genre_counts[genre] = 0

        runtime_totals[genre] += movie["runtime_seconds"]
        genre_counts[genre] += 1


def parse_imdb_runtime_totals(imdb_file):
    """Read an IMDb file handle and collect per-genre runtime totals.

    Args:
        imdb_file (TextIO): Open text file handle for pipe-separated IMDb data.

    Returns:
        tuple[dict[str, int], dict[str, int]]: (runtime_totals, genre_counts).
    """
    runtime_totals = {}
    genre_counts = {}

    for line in imdb_file:
        if line.startswith("#"):
            continue

        movie = parse_movie_line(line)
        add_movie_runtime_to_genres(movie, runtime_totals, genre_counts)

    return runtime_totals, genre_counts


def convert_runtime_totals_to_minutes(runtime_totals, genre_counts):
    """Convert per-genre total runtimes and counts into average minutes.

    Args:
        runtime_totals (dict[str, int]): Maps genre to total runtime in seconds.
        genre_counts (dict[str, int]): Maps genre to movie count.

    Returns:
        dict[str, float]: Maps genre to average runtime in minutes.
    """
    averages = {}
    for genre in runtime_totals:
        avg_seconds = runtime_totals[genre] / genre_counts[genre]
        averages[genre] = avg_seconds / 60
    return averages


def average_runtime_per_genre(imdb_path):
    """Compute average runtime (minutes) for each genre from an IMDb file.

    Args:
        imdb_path (str): Path to the IMDb-style input file.

    Returns:
        dict[str, float]: Genre names mapped to average runtime in minutes.
    """
    with open(imdb_path, "r", encoding="utf-8") as imdb_file:
        runtime_totals, genre_counts = parse_imdb_runtime_totals(imdb_file)

    return convert_runtime_totals_to_minutes(runtime_totals, genre_counts)


def main():
    """Read input path from CLI arguments and print genre averages.

    Args:
        None.

    Returns:
        None.
    """
    imdb_path = argv[1] if len(argv) > 1 else "downloads/250.imdb"
    averages = average_runtime_per_genre(imdb_path)
    for genre in sorted(averages):
        print(f"{genre}\t{averages[genre]:.1f} min")


if __name__ == "__main__":
    main()
