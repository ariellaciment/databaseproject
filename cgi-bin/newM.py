#!/usr/bin/python                                                                       
import sys
import traceback
print "Content-Type: text/html"
print
import cgi, cgitb

import mysql.connector
# Create instance of FieldStorage                                                       
form = cgi.FieldStorage()

Manager_ID = str(form.getvalue('MID'))
Manager_FirstName = form.getvalue('first')
Manager_LastName = form.getvalue('last')
Employee_Count = form.getvalue('count')
Team_ID = str(form.getvalue('client'))
cnx = mysql.connector.connect(user='aciment1',database= 'aciment11', password= 'aciment1', host = 'localhost')
cursor = cnx.cursor(buffered = True)

query = "INSERT INTO Manager(Manager_ID,Manager_FirstName,Manager_LastName,Employee_Count,Team_ID) VALUES(%s,%s,%s,%s,%s)"

values = (Manager_ID,Manager_FirstName,Manager_LastName,Employee_Count,Team_ID)

try:
    cursor.execute(query,(values))

    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<body>"
    print "<h1> YOU HAVE INSERTED THE MANAGER'S INFORMATION</h1>"
    print "<br> Manager ID:", Manager_ID, "<br>Manager First Name:", Manager_FirstName, "<br>Manager Last Name:",Manager_LastName, "<br>Employee Count:", Employee_Count, "<br>Team ID:", Team_ID, "<br>"
    print "</body>"
    print "</html>"

    cnx.commit()
    cursor.close()
    cnx.close()
except:
    print "\n\n<PRE>"
    traceback.print_exc()
