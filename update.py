import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='$Eswar@567'
)

cur=conn.cursor()

class updated:
    def deptupdate(x,colname,newval,refColname,oldvalue):
        cur.execute(f"update department set {colname}='{newval}' where {refColname}='{oldvalue}'")
        conn.commit()
        print("Data Updated in Department_Table Successfully---")

    def courseupdate(x,colname,newval,refColname,oldval):
        cur.execute(f"update course set {colname}='{newval}' where {refColname}='{oldval}'")
        conn.commit()
        print("Data Updated in Course_Table Successfully---")

    def facultyupdate(x,colname,newval,refColname,oldval):
        cur.execute(f"update faculty set {colname}='{newval}' where {refColname}='{oldval}'")
        conn.commit()
        print("Data Updated in Faculty_Table Successfully---")

    def Studentupdate(x,colname,newval,refColname,oldval):
        cur.execute(f"update student set {colname}='{newval}' where {refColname}='{oldval}'")
        conn.commit()
        print("Data Updated in Student_Table Successfully---")


