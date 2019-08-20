#use mysql for demo
#create these scripts before 
"""
create database py_learnings;
use py_learnings;
create table student(name varchar(40), college varchar(20));
insert into student values('bob','vsit'), ('micheal','CMD')
select * from student
"""
# install mysql-connector using pip3 install mysql-connector from your python installation folder

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="mysql", passwd="mysql",database="py_learnings")
mycursor = mydb.cursor()
mycursor.execute('select * from student') #you need mention database in the connection

result = mycursor.fetchall()
for i in result:
    print(i)
#to get only one data from fetch
#result = mycursor.fetchone()
#print(result)