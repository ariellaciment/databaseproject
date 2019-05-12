#!/usr/bin/python                                                                                                       
import cgi, cgitb

import mysql.connector
# Create instance of FieldStorage                                                                                       
form = cgi.FieldStorage()

Manager = form.getvalue('manager')
cnx = mysql.connector.connect(user = 'aciment1', database = 'aciment11', password = 'aciment1', host = 'localhost')
cursor = cnx.cursor(buffered = True)

query =("SELECT * FROM Manager WHERE Manager_FirstName=%s")

cursor.execute(query, (Manager,))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"

print" <h1> %s 's MANAGER INFORMATION" %(Manager)
print "</h1>"
print "<h1>"
for name in cursor:
    print "<br> Manager ID:", name[0], "<br>Manager First Name:", name[1], "<br>Manager Last Name:", name[2], "<br>Employee Count:", name[3], "<br>Team ID:", name[4], "<br>"
print"</h1>"
print "</body>"
print "</html>"

cnx.commit()
cursor.close()
cnx.close()
