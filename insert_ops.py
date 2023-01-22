import mysql.connector as conn

mydb = conn.connect(host='localhost',user='root',passwd = '******')

cursor = mydb.cursor()
s = "insert into sudhanshu.ineuron values(1, 'Abhinav', 'abhinav.mysql@gmail.com', 1900000,30)"
cursor.execute(s);
mydb.commit()
# cursor.execute("SELECT * FROM sudhanshu.ineuron;")
cursor.execute("Select emp_id,emp_name from sudhanshu.ineuron;")
# mydb.commit()

for i in cursor.fetchall():
    print(i)