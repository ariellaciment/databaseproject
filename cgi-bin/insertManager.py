#!/usr/bin/python
# Import modules for CGI handling                                                       
import cgi, cgitb
# Create instance of FieldStorage                                                       
form = cgi.FieldStorage()
Manager_Name = form.getvalue('name')
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"

print "<h1> WELCOME THE NEW MANAGER, %s" % (Manager_Name)
print '</h1>'

print '<h2>Please insert all of the new Managers Information</h2>'

print '<form action="newM.py">Manager ID: <br>'
print '<input type="text" name="MID"><br>'

print '<form action="newM.py">Manager First Name: <br>'
print '<input type="text" name="first"><br>'

print '<form action="newM.py"> Manager Last Name:<br>'
print '<input type="text" name="last"><br>'

print '<form action="newM.py"> Employee Count:<br>'
print '<input type="text" name="count"><br>'

print '<form action="newM.py"> Team ID:<br>'
print '<input type="text" name="client"><br>'
print '<input type="submit" value="Submit"></form>'

print "</body>"
print "</html>"
