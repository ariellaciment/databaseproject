#!/usr/bin/python                                                                                        
# Import modules for CGI handling
import sys
import traceback
print "Content-Type: text/html"
print
sys.stderr = sys.stdout
import cgi, cgitb
import mysql.connector
# Create instance of FieldStorage                                                                        
form = cgi.FieldStorage()
#get the value that the user inputed in the URL
Delete_Name = form.getvalue('deleteName')
#connecting to the database
cnx = mysql.connector.connect(user='aciment1', password='aciment1', host='localhost',database='aciment11')

cursor = cnx.cursor(buffered = True)

query3 = ("DELETE FROM Employee WHERE Employee_Name = %s")

try:
    cursor.execute(query3, (Delete_Name,))

    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<body>"
    print" <h1> YOU HAVE DELETED THE EMPLOYEE %s's  INFORMATION" % (Delete_Name)
    print "</h1>"
    print "<h1>"

    print '</h1>'
    print "</body>"
    print "</html>"

    cnx.commit()
    cursor.close()
    cnx.close()
except:
    print "\n\n<PRE>"
    traceback.print_exc()
