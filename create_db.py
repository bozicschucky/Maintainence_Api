import sqlite3
# import psycopg2

# conn = psycopg2.connect(host="localhost",database="posttest", user="postgres", password="sudo")
# cursor = conn.cursor()

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
# cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100,"abc'def"))
# cursor.execute("SELECT * FROM test;")
# cursor.fetchone()

cursor.execute("CREATE TABLE users (id serial PRIMARY KEY, username varchar , password varchar);")
# cursor.execute("CREATE TABLE items (name text PRIMARY KEY, price real);")




# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)
#
# create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
# cursor.execute(create_table)

connection.commit() #save changes

connection.close()
connection.close()
