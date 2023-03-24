import sqlite3
import csv

conn = sqlite3.connect('proj_0.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS movie_lens;
    DROP TABLE IF EXISTS top_1_in_20c;

    CREATE TABLE movie_lens(
    movie_id   INTEGER,
    title      TEXT,
    year       INTEGER,
    genres     TEXT,
    user_id    INTEGER,
    rating     REAL,
    time_stamp INTEGER,
    PRIMARY KEY (movie_id, user_id)
    );

    CREATE TABLE top_1_in_20c(
    title TEXT,
    year  INTEGER,
    top_1 REAL
    )
''')

with open('movielens.csv', 'r') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    for row in data:
        row = row[1:]
        #print(row)
        cur.execute('''INSERT INTO movie_lens (movie_id, title, year, genres, user_id, rating, time_stamp)
            values(?, ?, ?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

cur.execute('''WITH avg AS(
    SELECT title, year, ROUND(AVG(rating),2) AS avg_rating FROM movie_lens GROUP BY title
    )
SELECT title, year, MAX(avg_rating) FROM avg WHERE year BETWEEN 1900 AND 1999 GROUP BY year ORDER BY year
''')
results = cur.fetchall()
#print(results)
for top_1s in results:
    cur.execute('''INSERT INTO top_1_in_20c (title, year, top_1)
        VALUES(?, ?, ?)''', (top_1s[0], top_1s[1], top_1s[2]))

conn.commit()
conn.close()

print('database created')