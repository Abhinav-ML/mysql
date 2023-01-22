import mysql.connector as connection

mydb = connection.connect(host='localhost',user='root',passwd='******')
# print(mydb)

cursor = mydb.cursor()

# cursor.execute(" create table sudhanshu.ineuron(emp_id int(10), emp_name varchar(20), emp_mailid varchar(30), emp_salary int(7), emp_attendence int(3)) ")
cursor.execute("select * from sudhanshu.ineuron")
print(cursor.fetchall())