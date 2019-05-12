#!/usr/bin/python
#Import modules for CGI handling                                                    
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

Update_Name = form.getvalue('updateName')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"

print "<h1> LETS UPDATE, %s, 's INFORMATION" % (Update_Name)
print '</h1>'

print '<h2>Please insert all of the updated Employee Information</h2>'


print '<form action="updateInfo.py">Employee Name: <br>'
print '<input type="text" name="Ename"><br>'
print '<form action="updateInfo.py">Manager ID: <br>'
print '<input type="text" name="MID"><br>'
print '<form action="updateInfo.py"> Total Hours:<br>'
print '<input type="text" name="Hours"><br>'
print '<form action="updateInfo.py"> Meeting Hours:<br>'
print '<input type="text" name="meeting"><br>'
print '<form action="updateInfo.py"> Client Hours:<br>'
print '<input type="text" name="client"><br>'
print '<form action="updateInfo.py"> Email Hours:<br>'
print '<input type="text" name="email"><br>'
print '<form action="updateInfo.py"> Other Hours:<br>'
print '<input type="text" name="other"><br>'
print '<input type="submit" value="Submit"></form>'

print "</body>"
print "</html>"
