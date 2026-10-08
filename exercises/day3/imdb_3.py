"""Question 3: write top 10 movies for a genre to CSV/TSV output file.

Usage:
    python exercises/day3/imdb_3.py GENRE OUTPUT_FILE [IMDB_FILE]
"""

from sys import argv


def parse_movie_line(line):
    columns = line.strip().split("|")
    genres = [genre.strip().lower() for genre in columns[5].split(",") if genre.strip()]
    return {
        "title": columns[6].strip(),
        "rating": float(columns[1].strip()),
        "genres": genres,
    }


def get_top_movies_for_genre(imdb_path, requested_genre, limit=10):
    requested_genre = requested_genre.strip().lower()
    matches = []

    with open(imdb_path, "r", encoding="utf-8") as imdb_file:
        for line in imdb_file:
            if line.startswith("#"):
                continue
            movie = parse_movie_line(line)
            if requested_genre in movie["genres"]:
                matches.append(movie)

    top_movies = []

    for movie in matches:
        inserted = False

        for index in range(len(top_movies)):
            if movie["rating"] > top_movies[index]["rating"]:
                top_movies.insert(index, movie)
                inserted = True
                break

        if not inserted:
            top_movies.append(movie)

        if len(top_movies) > limit:
            top_movies.pop()

    return top_movies


def infer_separator(output_path):
    separator = "\t"
    lowered = output_path.lower()
    if lowered.endswith(".tsv"):
        separator = "\t"
    elif lowered.endswith(".csv"):
        separator = ","
    return separator


def write_movies(output_path, movies):
    separator = infer_separator(output_path)
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(f"title{separator}rating\n")
        for movie in movies:
            out_file.write(f"{movie['title']}{separator}{movie['rating']:.1f}\n")


def main():
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
