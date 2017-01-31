# My dirty ImDB crawler

My small dirty scripts to fetch the information from ImDB.
It requires `imdbpie`

----

	python fetch.py
	
will create `250-short.imdb` and `250.imdb`. It is slow as we make a query for every movie from the top 250 chart.

> `250-org.imdb` is here to skip that step.

----

	python randomize.py

takes `250-org.imdb` and shuffles the lines (except the first). It creates `250-shuffled.imdb`

----

	python output.py

takes `250-shuffled.imdb` and outputs a (big) table in HTML format (File: `db.html`)
