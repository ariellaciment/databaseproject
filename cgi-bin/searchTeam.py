#!/usr/bin/python                                                                         
import cgi, cgitb

import mysql.connector
# Create instance of FieldStorage                                                         
form = cgi.FieldStorage()

Team = form.getvalue('team')
cnx = mysql.connector.connect(user = 'aciment1', database = 'aciment11', password = 'acim\
ent1', host = 'localhost')
cursor = cnx.cursor(buffered = True)
#to match up the team that the user inputed to the team in the database
query =("SELECT * FROM Team WHERE Team_Name=%s")

cursor.execute(query, (Team,))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
print" <h1> TEAM INFORMATION"
print "</h1>"
print "<h1>"
for team in cursor:
    print "<br> Team Name:", team[0], "<br>Team ID:", team[1], "<br>Department:", team[2], "<br>Team Count:", team[3], "<br>Manager ID:", team[4], "<br"
print "</h1>"

print "</body>"
print "</html>"

cnx.commit()
cursor.close()
cnx.close()
