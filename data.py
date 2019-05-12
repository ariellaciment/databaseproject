#!/usr/bin/python3

import mysql.connector

cnx = mysql.connector.connect(user='aciment1', database='aciment11', password='aciment1', host='localhost')
cursor = cnx.cursor()

cursor.execute("LOAD DATA LOCAL INFILE './employee.txt' INTO TABLE Employee FIELDS TERMINATED BY '|'")

cursor.execute("LOAD DATA LOCAL INFILE './manager.txt' INTO TABLE Manager FIELDS TERMINATED BY '|'" )


cursor.execute("LOAD DATA LOCAL INFILE './team.txt' INTO TABLE Team FIELDS TERMINATED BY '|'")

cnx.commit()
cursor.close()
cnx.close()
