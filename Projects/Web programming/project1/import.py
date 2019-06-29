#import requests
#res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "LTAXckbZ8m5lCI6vU3vWg", "isbns": "9781632168146"})
#print(res.json())

#psql DBNAME USERNAME command line create,insert,delete

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#engine = create_engine(os.getenv("DATABASE_URL"))
try:
    engine = create_engine(os.getenv("DATABASE_URL"))
except:
    raise Exception('invalid env variable')

db = scoped_session(sessionmaker(bind=engine))

#raw sql
sql ='DROP TABLE IF EXISTS books'
result = engine.execute(sql)

engine.execute('''CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR UNIQUE NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year SMALLINT NOT NULL

);CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    users VARCHAR UNIQUE NOT NULL,
    passwords VARCHAR NOT NULL
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES accounts,
    book_id INTEGER REFERENCES books,
    rating SMALLINT NOT NULL CONSTRAINT Invalid_Rating CHECK (rating <=5 AND rating>=1),
    comment VARCHAR
)''')



import csv
f=open('books.csv')
reader=csv.reader(f)
next(reader, None)

for isbn, title, author, year in reader:
    db.execute("INSERT INTO books(isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": year})

    print(f"Added {isbn} with {title} written by {author} on {year} .")
# transactions are assumed, so close the transaction finished
