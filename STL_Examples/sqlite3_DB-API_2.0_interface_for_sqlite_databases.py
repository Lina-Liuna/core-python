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

# 