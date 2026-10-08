"""Question 2: print average movie runtime per genre (in minutes)."""

from collections import defaultdict
from sys import argv


def parse_movie_line(line):
    columns = line.strip().split("|")
    runtime_seconds = int(columns[3].strip())
    genres = [genre.strip().lower() for genre in columns[5].split(",") if genre.strip()]
    return {
        "runtime_seconds": runtime_seconds,
        "genres": genres,
    }


def average_runtime_per_genre(imdb_path):
    runtime_totals = defaultdict(int)
    genre_counts = defaultdict(int)

    with open(imdb_path, "r", encoding="utf-8") as imdb_file:
        for line in imdb_file:
            if line.startswith("#"):
                continue
            movie = parse_movie_line(line)
            for genre in movie["genres"]:
                runtime_totals[genre] += movie["runtime_seconds"]
                genre_counts[genre] += 1

    averages = {}
    for genre in runtime_totals:
        avg_seconds = runtime_totals[genre] / genre_counts[genre]
        averages[genre] = avg_seconds / 60
    return averages


def main():
    imdb_path = argv[1] if len(argv) > 1 else "downloads/250.imdb"
    averages = average_runtime_per_genre(imdb_path)
    for genre in sorted(averages):
        print(f"{genre}\t{averages[genre]:.1f} min")


if __name__ == "__main__":
    main()
