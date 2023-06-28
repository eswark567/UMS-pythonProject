import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='$Eswar@567'
)

cur=conn.cursor()

class read:
    def deptreading(x,deptid):
        cur.execute(f"select * from department where departmentid={deptid}")
        print(cur.fetchall())
    def deptWhreading(x):
        cur.execute(f"select * from department")
        print(cur.fetchall())

    def coursereading(x,cid):
        cur.execute(f"select * from course where courseid={cid}")
        print(cur.fetchall())
    def courseWhreading(x):
        cur.execute(f"select * from course")
        print(cur.fetchall())
    
    def facultyreading(x,fid):
        cur.execute(f"select * from faculty where facultyid={fid}")
        print(cur.fetchall())
    def facultyWhreading(x):
        cur.execute(f"select * from faculty")
        print(cur.fetchall())

    def studentreading(x,sid):
        cur.execute(f"select * from student where sid={sid}")
        print(cur.fetchall())
    def studentWhreading(x):
        cur.execute(f"select * from student")
        print(cur.fetchall())
        