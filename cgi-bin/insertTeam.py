#!/usr/bin/python
# Import modules for CGI handling
import cgi, cgitb
# Create instance of FieldStorage
form = cgi.FieldStorage()
Team_Name = form.getvalue('team')
print "Content-type:text/html\r\n\r\n"
print "<html>"                                                                
print "<body>"                                                                
 
print "<h1> WELCOME THE NEW TEAM, %s" % (Team_Name)                   
print '</h1>'
 
print '<h2>Please insert all of the new Teams Information</h2>'
                                   
print '<form action="newTeam.py">Team Name: <br>'
print '<input type="text" name="name"><br>'

print '<form action="newTeam.py">Team ID: <br>'
print '<input type="text" name="TID"><br>'

print '<form action="newTeam.py"> Department:<br>'
print '<input type="text" name="dept"><br>'

print '<form action="newTeam.py"> Team Count:<br>'                        
print '<input type="text" name="count"><br>'                                
 
print '<form action="newTeam.py"> Manager ID:<br>'
print '<input type="text" name="MID"><br>'
print '<input type="submit" value="Submit"></form>'
print"</body>"
print"</html>"
