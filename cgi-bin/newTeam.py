#!/usr/bin/python                                                            
import sys
import traceback                                                             
print "Content-Type: text/html"
print                                                                        
import cgi, cgitb

import mysql.connector
# Create instance of FieldStorage                                           
form = cgi.FieldStorage()                                                    
 
Team_Name = str(form.getvalue('name'))
Team_ID = str(form.getvalue('TID'))
Department = form.getvalue('dept')
Team_Count = form.getvalue('count')
Manager_ID = str(form.getvalue('MID'))
cnx = mysql.connector.connect(user='aciment1',database= 'aciment11', password
= 'aciment1', host = 'localhost')
cursor = cnx.cursor(buffered = True)

query = "INSERT INTO Team(Team_Name,Team_ID,Department,Team_Count,Manager_ID) VALUES(%s,%s,%s,%s,%s)"

v = (Team_Name, Team_ID, Department, Team_Count, Manager_ID)

try:
    cursor.execute(query,(v))
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<body>"
    print "<h1> YOU HAVE INSERTED THE TEAM'S INFORMATION</h1>"

    print "<br> Team Name:", Team_Name, "<br>Team ID:", Team_ID, "<br>Department:",Department, "<br>Team Count:",Team_Count,"<br>Manager ID:", Manager_ID, "<br>"
    print "</body>"
    print "</html>"

    cnx.commit()
    cursor.close()
    cnx.close()
except:
    print "\n\n<PRE>"
    traceback.print_exc()
