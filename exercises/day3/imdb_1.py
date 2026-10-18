"""Question 1: print number of movies per genre in 250.imdb."""

from sys import argv


def parse_movie_line(line):
	"""Parse one IMDb row into title and normalized genres.

	Args:
		line (str): A pipe-separated movie row from the IMDb file.

	Returns:
		dict[str, str | list[str]]: Dictionary with:
		- title (str): Movie title.
		- genres (list[str]): Lowercased genre names for the movie.
	"""
	columns = line.strip().split("|")
	genres = [genre.strip().lower() for genre in columns[5].split(",") if genre.strip()]
	return {
		"title": columns[6].strip(),
		"genres": genres,
	}

def count_genres(genres, counts):
	"""Update genre counters using one movie's list of genres.

	Args:
		genres (list[str]): Genre names for a single movie.
		counts (dict[str, int]): Running count per genre.

	Returns:
		dict[str, int]: Updated genre count dictionary.
	"""
	for genre in genres:
		if genre not in counts:
			counts[genre] = 0
		counts[genre] += 1
	return counts

def parse_imdb_file(imdb_filehandle):
	"""Read an IMDb file handle and count how many movies each genre has.

	Args:
		imdb_filehandle (TextIO): Open text file handle for IMDb data.

	Returns:
		dict[str, int]: Genre names mapped to number of movies.
	"""
	counts = {}
	for line in imdb_filehandle:
		if line.startswith("#"):
			continue

		movie = parse_movie_line(line)
		genres = movie["genres"]

		counts = count_genres(genres, counts)

	return counts


def count_movies_per_genre(imdb_path):
	"""Load an IMDb file path and return movie counts per genre.

	Args:
		imdb_path (str): Path to the IMDb-style input file.

	Returns:
		dict[str, int]: Genre names mapped to number of movies.
	"""
	counts = {}

	with open(imdb_path, "r", encoding="utf-8") as imdb_file:
		return parse_imdb_file(imdb_file)


def main():
	"""Read CLI input path and print movie counts by genre.

	Args:
		None.

	Returns:
		None.
	"""
	imdb_path = argv[1] if len(argv) > 1 else "downloads/250.imdb"
	counts = count_movies_per_genre(imdb_path)
	for genre in sorted(counts):
		print(f"{genre}\t{counts[genre]}")


if __name__ == "__main__":
	main()