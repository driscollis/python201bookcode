import pyodbc

driver = 'DRIVER={SQL Server}'
server = 'SERVER=localhost'
port = 'PORT=1433'
db = 'DATABASE=testdb'
user = 'UID=me'
pw = 'PWD=pass'
conn_str = ';'.join([driver, server, port, db, user, pw])

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute('select * from table_name')
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()