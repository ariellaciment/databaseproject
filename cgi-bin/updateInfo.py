#!/usr/bin/python                                                                                              
import cgi, cgitb
import mysql.connector
# Create instance of FieldStorage
form = cgi.FieldStorage()

Employee_Name = form.getvalue('Ename')
Manager_ID = form.getvalue('MID')
Hours_Total = form.getvalue('Hours')
Meeting_Hours = form.getvalue('meeting')
Client_Hours = form.getvalue('client')
Email_Hours = form.getvalue('email')
Other_Hours = form.getvalue('other')
cnx = mysql.connector.connect(user = 'aciment1', database = 'aciment11', password = 'aciment1', host = 'localhost')

cursor = cnx.cursor(buffered = True)

query =("UPDATE Employee SET Employee_Name="+Employee_Name+",Manager_ID="+Manager_ID+",Hours_Total="+Hours_Total+",Meeting_Hours="+Meeting_Hours+",Client_Hours="+Client_Hours+",Email_Hours="+Email_Hours+", Other_Hours="+Other_Hours+")\
VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')")

vals = (Employee_Name,Manager_ID,Hours_Total,Meeting_Hours,Client_Hours,Email_Hours, Other_Hours)

cursor.execute(query, (vals,))
#(Employee_Name, Manager_ID, Hours_Total, Meeting_Hours, Client_Hours, Email_Hours, Other_Hours)\
#VALUES(%s, %s, %s, %s, %s, %s, %s)"

#% (Employee_Name, Manager_ID,Hours_Totals,Meeting_Hours,Client_Hours,Email_Hours,Other_Hours))
#cursor.execute('%s', '%s', '%s', '%s', '%s', '%s', '%s')%\
#(Employee_Name,Manager_ID,Hours_Totals,Meeting_Hours,Client_Hours,Email_Hours,Other_Hours,)
#cursor.execute(query,(Employee_Name,Manager_ID,Hours_Totals,Meeting_Hours,Client_Hours,Email_Hours, Other_Hours,))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"                                                                                                          
print" <h1> UPDATED EMPLOYEE INFORMATION"
print "</h1>"
#name = cursor.fetchall()
for name in cursor:
    print name                                                                                                      
    #print "<br> Employee Name:", name[0], "<br>Manager ID:", name[1], "<br>Total Hours:", name[2], "<br>Meeting Hours:", name[3], "<br>Client Hours:", name[4], "<br>Email Hours:", name[5],"<br>Other Hours:", name[6], "<br>"

print "</body>"
print "</html>"

cnx.commit()
cursor.close()
cnx.close()
