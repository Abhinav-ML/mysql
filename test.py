import mysql.connector as conn  # connection

mydb = conn.connect(host='localhost', user='root', passwd='*****')
print(mydb)
cursor = mydb.cursor()
cursor.execute('show databases')
print(cursor.fetchall())
# # cursor.execute("create database sudhanshu")
# for i in cursor.fetchall():
#     l.append(i)
# print(l)
