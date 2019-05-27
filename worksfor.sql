create table works_for(
Employee_Name varchar(20),
Manager_ID varchar(20),
PRIMARY KEY(Employee_Name),
FOREIGN KEY (Employee_Name) REFERENCES Employee(Employee_Name),
FOREIGN KEY(Manager_ID) REFERENCES Manager(Manager_ID));
