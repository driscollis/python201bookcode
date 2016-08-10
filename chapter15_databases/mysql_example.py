import MySQLdb

conn = MySQLdb.connect('localhost', 'username', 'password', 'table_name')
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")

# get a single row
row = cursor.fetchone()
print(row)

# disconnect from the database
conn.close()