import adodbapi

database = "db1.mdb"
constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s'  % database
tablename = "address"

# connect to the database
conn = adodbapi.connect(constr)

# create a cursor
cur = conn.cursor()

# extract all the data
sql = "select * from %s" % tablename
cur.execute(sql)

# show the result
result = cur.fetchall()
for item in result:
    print item

# close the cursor and connection
cur.close()
conn.close()