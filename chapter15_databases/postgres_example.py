import psycopg2

conn = psycopg2.connect(dbname='my_database', user='username')
cursor = conn.cursor()

# execute a query
cursor.execute("SELECT * FROM table_name")
row = cursor.fetchone()

# close your cursor and connection
cursor.close()
conn.close()