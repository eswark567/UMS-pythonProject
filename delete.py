import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='$Eswar@567'
)

cur=conn.cursor()

class deleted:

    def deptdelete(x,deptidd):
        cur.execute(f"delete from department where departmentid={deptidd} ")
        conn.commit()
        print("Data deleted in Deaprtment_Table successfully")

    def coursedelete(x,cid):
        cur.execute(f"delete from course where courseid={cid} ")
        conn.commit()
        print("Data deleted in Course_Table successfully")

    def facultydelete(x,fid):
        cur.execute(f"delete from faculty where facultyid={fid} ")
        conn.commit()
        print("Data deleted in Faculty_Table successfully")
    
    def studentdelete(x,sid):
        cur.execute(f"delete from student where sid={sid} ")
        conn.commit()
        print("Data deleted in Student_Table successfully")

    