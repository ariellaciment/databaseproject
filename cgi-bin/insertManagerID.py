#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 


FirstName = form.getvalue('firstname')
LastName = form.getvalue('lastname')

print "Content-type:text/html\r\n\r\n"
print "<html>"

print "<h1> Hello, %s %s" % (FirstName,LastName)
print "</h1>"

print '<body>To insert a new Employee:</body>'
print '<form action="insertEmployeeName.py">Enter the new Employees name:<br>'
print '<input type="text" name="newname"><br>'
print '<input type="submit" value="Submit"></form>'

print '<body>To find an Employee:</body>'
print '<form action="findEmployee.py">Enter Employee Name:<br>'
print '<input type="text" name="Ename"><br>'
print '<input type="submit" value="Submit"></form'

print '<body>To find a Manager:</body>'
print '<form action="findManager.py">Enter the Manager name:<br>'
print '<input type="text" name="manager"><br>'
print '<input type="submit" value="Submit"></form>'

print '<body>To update an Employees information:</body>'
print '<form action="updateEmployee.py"> Enter Employee Name:<br>'
print '<input type="text" name="updateName"><br>'
print '<input type="submit" value="Submit"></form'


print '<h1>To delete an Employee:</h1>'
print '<form action="deleteEmployee.py">Enter Employee Name:<br>'
print '<input type="text" name="deleteName"><br>'
print '<input type="submit" value="Submit"></form'


print '<h1>To find a Team:</h1>'
print '<form action="searchTeam.py">Enter Team Name:<br>'
print '<input type="text" name="team"><br>'
print '<input type="submit" value="Submit"></form'

print '</html>'
