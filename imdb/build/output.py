#!/usr/bin/env python3
# -*- coding: utf-8 -*-


dbfile = '250-shuffled.imdb'

def to_html(line):
    blocks = line.split('|')
    # Votes Rating Year Runtime URL Genres Title
    return u'<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td><img src="{4}" alt=""/></td><td>{5}</td><td>{6}</td>'.format(
        blocks[0],
        blocks[1],
        blocks[2],
        blocks[3],
        blocks[4],
        blocks[5],
        blocks[6]
    )


with open('db.html','w',encoding="utf-8") as html:
    html.write('''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
	<title>Movie DB</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        table {cell-spacing:2px; } 
        th { background: black; color: white; }
        tbody tr:nth-child(even) { background: #eee; }
        tbody tr:nth-child(odd)  { background: white; }
        img { height: 100px; }
        </style>
    </head>
    <body>
    <table>
    <thead><tr>
    <th>Votes</th><th>Rating</th><th>Year</th><th>Runtime (in seconds)</th><th>Poster</th><th>Genres</th><th>Title</th>
    <tr></thead>
    <tbody><tr>''')


    with open(dbfile,'r',encoding="utf-8") as db:

        html.write('</tr><tr>'.join( to_html(line) for line in db if not line.startswith('#') ))


    html.write('</tr></tbody></table></body></html>')

