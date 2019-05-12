#!/usr/bin/python                                                                                        
# Import modules for CGI handling
import cgi, cgitb
import mysql.connector
# Create instance of FieldStorage                                                                        
form = cgi.FieldStorage()
Delete_Name = form.getvalue('deleteName')

cnx = mysql.connector.connect(user = 'aciment1', database = 'aciment11', password = 'aciment1', host = 'localhost')
cursor = cnx.cursor(buffered = True)

query =("DELETE FROM Employee WHERE Employee_Name=%s")

cursor.execute(query, (Delete_Name,))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
print" <h1> EMPLOYEE INFORMATION"
print "</h1>"

print "<h1> YOU HAVE DELETED THE EMPLOYEE %s" % (Delete_Name)
print '</h1>'

for name in cursor:
    #print name
    print "<br> Employee Name", name[0], "<br>Manager ID", name[1], "<br>Total Hours", name[2], "<br>Meeting Hours", name[3], "<br>Client Hours", name[4], "<br>Email Hours", name[5],"<br>Other Hours", name[6], "<br"

print "</body>"
print "</html>"

cnx.commit()
cursor.close()
cnx.close()


