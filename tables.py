#!/usr/bin/python3
from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='aciment1', password='aciment1',
                              host='localhost', database = 'aciment11')
mycursor = cnx.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS Employee\
(Employee_Name varchar(15),\
Manager_ID varchar(10),\
    Hours_Total varchar(100),\
    Meeting_Hours varchar(100),\
    Client_Hours varchar(100),\
    Email_Hours varchar(100),\
    Other_Hours varchar(100),\
    PRIMARY KEY (Manager_ID))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Manager(\
    Manager_ID varchar(10),\
    Manager_FirstName varchar(20),\
    Manager_LastName varchar(20),\
    Employee_Count varchar(100),\
    Team_ID varchar(10),\
    PRIMARY KEY(Team_ID),\
    FOREIGN KEY (Manager_ID) REFERENCES Employee(Manager_ID))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Team(\
    Team_Name varchar(30),\
    Team_ID varchar(10),\
    Department varchar(20),\
    Team_Count varchar(100),\
    Manager_ID varchar(10),\
    PRIMARY KEY(Team_Name),\
    FOREIGN KEY (Team_ID) REFERENCES Manager(Team_ID),\
    FOREIGN KEY(Manager_ID) REFERENCES Employee(Manager_ID))")

mycursor.close()
cnx.close()
