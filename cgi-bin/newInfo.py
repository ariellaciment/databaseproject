#!/usr/bin/python
import sys
import traceback
print "Content-Type: text/html"
print
import cgi, cgitb

import mysql.connector
# Create instance of FieldStorage                                                         
form = cgi.FieldStorage()

Employee_Name = form.getvalue('Ename')
Manager_ID = form.getvalue('MID')
Hours_Totals = form.getvalue('Hours')
Meeting_Hours = form.getvalue('meeting')
Client_Hours = form.getvalue('client')
Email_Hours = form.getvalue('email')
Other_Hours = form.getvalue('other')
cnx = mysql.connector.connect(user='aciment1',database= 'aciment11', password= 'aciment1', host = 'localhost')
cursor = cnx.cursor(buffered = True)

query = "INSERT INTO Employee(Employee_Name,Manager_ID,Hours_Total,Meeting_Hours,Client_Hours,Email_Hours,Other_Hours) VALUES(%s,%s,%s,%s,%s,%s,%s)"

values = (Employee_Name,Manager_ID,Hours_Totals,Meeting_Hours,Client_Hours,Email_Hours,Other_Hours)
try:
    cursor.execute(query,(values))               
#value = (Employee_Name, M_ID,Hours_Totals,Meeting_Hours,Client_Hours,Email_Hours,Other_Hours)

    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<body>"
    print "<h1> YOU HAVE INSERTED THE EMPLOYEE'S INFORMATION</h1>"
                                                             
    print "<br> Employee Name:", Employee_Name, "<br>Manager ID:", Manager_ID, "<br>Total Hours:",Hours_Totals, "<br>Meeting Hours:", Meeting_Hours, "<br>Client Hours:", Client_Hours, "<br>Email Hours:", Email_Hours,"<br>Other Hours:", Other_Hours, "<br>"
    print "</body>"
    print "</html>"

    cnx.commit()
    cursor.close()
    cnx.close()
except:
    print "\n\n<PRE>"
    traceback.print_exc()
