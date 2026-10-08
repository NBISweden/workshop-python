"""Question 1: print number of movies per genre in 250.imdb."""

from collections import defaultdict
from sys import argv


def parse_movie_line(line):
	columns = line.strip().split("|")
	genres = [genre.strip().lower() for genre in columns[5].split(",") if genre.strip()]
	return {
		"title": columns[6].strip(),
		"genres": genres,
	}


def count_movies_per_genre(imdb_path):
	counts = defaultdict(int)
	with open(imdb_path, "r", encoding="utf-8") as imdb_file:
		for line in imdb_file:
			if line.startswith("#"):
				continue
			movie = parse_movie_line(line)
			for genre in movie["genres"]:
				counts[genre] += 1
	return counts


def main():
	imdb_path = argv[1] if len(argv) > 1 else "downloads/250.imdb"
	counts = count_movies_per_genre(imdb_path)
	for genre in sorted(counts):
		print(f"{genre}\t{counts[genre]}")


if __name__ == "__main__":
	main()