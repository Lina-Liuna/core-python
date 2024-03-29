# SQLite is a C library that provides a lightweight disk-based database that doesn't require a separate
# server process.

# SQLite allows accessing the database using a nonstandard variant of the SQL query language.

# Some applications can use SQLite for internal data storage.
# Can prototype an application using SQLite and then port the code to a larger database such as PostgreS@QL or Oracle.

# 1. create a new database and open a database connection to allow sqlite3 to work with it.

# call sqlite3.connect() to create a connection to the database tutorial.db in the current working directory
# Implicitly creating it if it does not exist.

# the returned connection object con represents the connection to the on-disk database.
import sqlite3

con = sqlite3.connect('tutorial.db')

# 2. to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor.
# call con.cursor() to create the cursor.

cur = con.cursor()

# 3. after the database connection and a cursor, create a database table movie with columns for title, release year,
# and review score.
cur.execute("CREATE TABLE if not exists movie(title, year, score)")

# 4. verify that the new table has been created by querying the sqlite_master built-in to SQLite, which should new
# contain an entry for the movie table definition.

# Execute the query by calling cur.execute(), assign the result to res

res = cur.execute("SELECT name from sqlite_master")

# 5. call res.fetchone() to fetch the resulting row

print(res.fetchall())

# 6. query sqlite_master for table named 'movie'
res = cur.execute("SELECT name FROM sqlite_master WHERE name='movie'")
print(res.fetchone())

# 7. Insert data

cur.execute("""
    INSERT INTO movie VALUES
        ('He is Just Not That Into You', 1990, 6.4),
        ('Silver Linings Playbook', 2012, 7.7)
""")

# con.commit() to commit the transaction
con.commit()

# 8. Verify:
res = cur.execute('SELECT score FROM movie')
print(res.fetchall())


# insert more rows by calling cur.executemany(...)

data = [
    ('The Menu', 2022, 7.3),
    ('Avatar:The Way of Water', 2022, 7.9),
    ('Everything Everywhere All at Once', 2022, 8.0),
    ('A Man Called Otto', 2022, 7.5)
]

cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

# verify new rows by executing a SELECT query
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

# verify that the database has been written to disk by calling con.close() to close the existing connection
con.close()

# Opening a new one, creating a new cursor, then query the database:
new_con = sqlite3.connect('tutorial.db')
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring movie is {title!r}, released in {year}')

# use :memory: to create a shared memory connection,
# the :memory: database will be erased when the last connection is deleted from memory.
# Super-useful: encrypt your database by using con.create_function(md5)
import hashlib


def md5sum(t):
    return hashlib.md5(t).hexdigest()


con = sqlite3.connect(":memory:")

con.create_function("md5", 1, md5sum)
for row in con.execute("SELECT md5(?)", (b"foo",)):
    print(row)
con.close()

# Create or remove a user-defined SQL aggregate function
class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.execute("CREATE TABLE test(i)")
cur.execute("INSERT INTO test(i) VALUES(1)")
cur.execute("INSERT INTO test(i) VALUES(2)")
cur.execute("INSERT INTO test(i) VALUES(3)")
cur.execute("SELECT mysum(i) FROM test")
print(cur.fetchall())
#print(cur.fetchone()[0])
res = cur.execute("SELECT name from sqlite_master")
print(res.fetchall())

con.close()

# example: shows a reverse sorting collation
def collate_reverse(string1, string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1

con = sqlite3.connect(":memory:")
con.create_collation("reverse", collate_reverse)

cur = con.execute("CREATE TABLE test(x)")
cur.executemany("INSERT INTO test(x) VALUES(?)", [("a",), ("b",)])
cur.execute("SELECT x FROM test ORDER BY x COLLATE reverse")
for row in cur:
    print(row)

con.close()

# Convert :memory: db to SQL dump file dump.sql
con = sqlite3.connect(':memory:')
with open('temp.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)
con.close()


# con.backup: Create a backup of an SQLite database.
# Works even if the database is being accessed by other clients or concurrently by the same connection.

def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

src = sqlite3.connect('tutorial.db')
dst = sqlite3.connect('backup.db')
with dst:
    src.backup(dst, pages=1, progress=progress)
dst.close()
src.close()


# sent ISO dates/ ISO timestamps to SQLite.
import datetime

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("create table test(d date, ts timestamp)")

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
cur.execute("select d, ts from test")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))

con.close()


# How to use placeholders to bind values in SQL queries

# SQL operations usually need to use value from python variables, however, beware of using python's string operations
# to assemble queries, as they are vulnerable to SQL injection attacks.

# to insert a variable into a query string, use a placeholder in the string, and substitute that actual values into
# the query by providing them as a tuple of values to the second argument of the cursors' execute() method.

# An SQL statement may use  one of two kinds of placeholders: question marks or named placeholders.
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

# This is the qmark style:
cur.execute("INSERT INTO lang VALUES(?, ?)", ("C", 1972))

# The qmark style used with executemany():
lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
cur.executemany("INSERT INTO lang VALUES(?, ?)", lang_list)

# And this is the named style:
cur.execute("SELECT * FROM lang WHERE first_appeared = :year", {"year": 1972})
print(cur.fetchall())
