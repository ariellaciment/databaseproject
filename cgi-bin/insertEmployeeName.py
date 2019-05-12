#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

Employee_Name = form.getvalue('newname')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"

print "<h1> WELCOME THE NEW EMPLOYEE, %s" % (Employee_Name)
print '</h1>'

print '<h2>Please insert all of the new Employees Information</h2>'

print '<form action="newInfo.py">Employee Name: <br>'
print '<input type="text" name="Ename"><br>'
print '<form action="newInfo.py">Manager ID: <br>'
print '<input type="text" name="MID"><br>'
print '<form action="newInfo.py"> Total Hours:<br>'
print '<input type="text" name="Hours"><br>'
print '<form action="newInfo.py"> Meeting Hours:<br>'
print '<input type="text" name="meeting"><br>'
print '<form action="newInfo.py"> Client Hours:<br>'
print '<input type="text" name="client"><br>'
print '<form action="newInfo.py"> Email Hours:<br>'
print '<input type="text" name="email"><br>'
print '<form action="newInfo.py"> Other Hours:<br>'
print '<input type="text" name="other"><br>'
print '<input type="submit" value="Submit"></form>'





print "</body>"
print "</html>"
