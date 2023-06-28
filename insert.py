import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='$Eswar@567'
)

cur=conn.cursor()

class inserted:

    def deptinsert(x,deptid,deptname):
        cur.execute(f"insert into department values({deptid},'{deptname}')")
        conn.commit()
        print("Data Inserted in Department Table successfully---")
    
    def courseinsert(x,cid,cname,cfee,cduration):
        cur.execute(f"insert into course values({cid},'{cname}',{cfee},{cduration})")
        conn.commit()
        print("Data inserted in Course Table Successfully")
    
    def facultyinsert(x,fid,fname,deptid,sal,cid):
        cur.execute(f"insert into faculty values({fid},'{fname}',{deptid},{sal},{cid})")
        conn.commit()
        print("Data inserted in Faculty_Table Successfully")

    def studentinsert(x,sid,sname,cid,deptid):
        cur.execute(f"insert into student values({sid},'{sname}',{cid},{deptid})")
        conn.commit()
        print("Data inserted in Student5_Table Successfully")

