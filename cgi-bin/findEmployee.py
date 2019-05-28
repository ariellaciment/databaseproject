#!/usr/bin/python
import cgi, cgitb

import mysql.connector
# Create instance of FieldStorage                      
form = cgi.FieldStorage()

checkName = form.getvalue('Ename')
cnx = mysql.connector.connect(user = 'aciment1', database = 'aciment11', password = 'aciment1', host = 'localhost')
cursor = cnx.cursor(buffered = True)
#query to match up the employee name to the employee in the database
query =("SELECT * FROM Employee WHERE Employee_Name=%s")

cursor.execute(query, (checkName,))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"

print" <h1> %s 's EMPLOYEE INFORMATION" %(checkName)
print "</h1>"
print "<h1>"
#to print out all of the employees information
for name in cursor:
    print "<br> Employee Name:", name[0], "<br>Manager ID:", name[1], "<br>Total Hours:", name[2], "<br>Meeting Hours:", name[3], "<br>Client Hours:", name[4], "<br>Email Hours:", name[5],"<br>Other Hours:", name[6], "<br>"
print"</h1>"
print "</body>"
print "</html>"

cnx.commit()
cursor.close()
cnx.close()
