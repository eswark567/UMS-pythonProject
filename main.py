from insert import inserted
from update import updated
from delete import deleted
from read import read

obj=inserted()
obj2=updated()
obj3=deleted()
obj4=read()
print("Welcome to the University Management System!")
print("Database Information:")
print("- Number of tables: 4")
print("- Table names: Student, Department, Faculty, Course")

# Displaying student table information
print("\nStudent Table Information:")
print("- Number of records: 4")
print("- Columns: sid, sname, courseid, dptid")

# Displaying department table information
print("\nDepartment Table Information:")
print("- Number of records: 2")
print("- Columns: departmentid, departmentname")

# Displaying faculty table information
print("\nFaculty Table Information:")
print("- Number of records: 5")
print("- Columns: facultyid, facultyname, departmentid, salary, courseid")

# Displaying course table information
print("\nCourse Table Information:")
print("- Number of records: 4")
print("- Columns: courseid, coursename, coursefees, duration")

tab=int(input("Select Table number from \n1.Department\n2.Course\n3.Faculty\n4.Student\n Enter Table Number:"))
opr=int(input("select Operation from \n1.INSERT\n2.UPDATE\n3.DELETE\n4.READ\n5.Read_Whole_Table\n Enter operator:"))

# DATA OPERATIONS FOR DEPARTMENT TABLE
if tab==1 and opr==1:
    deptid=int(input("Enter DepartmentID:"))
    deptname=input("Enter Department Name:")
    obj.deptinsert(deptid,deptname)

if tab==1 and opr==2:
    colname=input("Enter columnName:")
    newval=input("Enter New value:")
    refcolname=input("Enter Referemce_column_name:")
    oldvalue=input("Enter Oldvalue:")
    obj2.deptupdate(colname,newval,refcolname,oldvalue)

if tab==1 and opr==3:
    deptidd=int(input("Enter deptid:"))
    obj3.deptdelete(deptidd)

if tab==1 and opr==4:
    deptid=int(input("Enter DepartmentID:"))
    obj4.deptreading(deptid)
if tab==1 and opr==5:
    obj4.deptWhreading()
    
# DATA OPERATIONS FOR COURSE TABLE

if tab==2 and opr==1:
    cid=int(input("Enter Course_ID:"))
    cname=input("Enter Course_Name:")
    cfee=float(input("Enter Course_Fee:"))
    cduration=int(input("Enter Duration_of_Course:"))
    obj.courseinsert(cid,cname,cfee,cduration)
if tab==2 and opr==2:
    colname=input("Enter columnName:")
    newval=input("Enter New value:")
    refcolname=input("Enter Referemce_column_name:")
    oldvalue=input("Enter Oldvalue:")
    obj2.courseupdate(colname,newval,refcolname,oldvalue)
if tab==2 and opr==3:
    cid=int(input("Enter Course_id:"))
    obj3.coursedelete(cid)
if tab==2 and opr==4:
    cid=int(input("Enter Course_ID:"))
    obj4.coursereading(cid)
if tab==2 and opr==5:
    obj4.courseWhreading()

#DATA OPERATIONS FOR FACULTY TABLE
if tab==3 and opr==1:
    fid=int(input("Enter Faculty_ID:"))
    fname=input("Enter Faculty_Name:")
    deptid=float(input("Enter Department_ID:"))
    sal=int(input("Enter Salary :"))
    cid=int(input("Emter COurse_id:")) 
    obj.facultyinsert(fid,fname,deptid,sal,cid)
if tab==3 and opr==2:
    colname=input("Enter columnName:")
    newval=input("Enter New value:")
    refcolname=input("Enter Referemce_column_name:")
    oldvalue=input("Enter Oldvalue:")
    obj2.facultyupdate(colname,newval,refcolname,oldvalue)
if tab==3 and opr==3:
    fid=int(input("Enter Faculty_id:"))
    obj3.facultydelete(fid)
if tab==3 and opr==4:
    fid=int(input("Enter Faculty_ID:"))
    obj4.facultyreading(fid)
if tab==3 and opr==5:
    obj4.facultyWhreading()

#DATA OPERATIONS FOR FACULTY TABLE
if tab==4 and opr==1:
    sid=int(input("Enter Student_ID:"))
    sname=input("Enter Student_Name:")
    cid=int(input("Emter COurse_id:"))
    deptid=int(input("Enter Department_ID:"))
    obj.studentinsert(sid,sname,cid,deptid)
if tab==4 and opr==2:
    colname=input("Enter columnName:")
    newval=input("Enter New value:")
    refcolname=input("Enter Referemce_column_name:")
    oldvalue=input("Enter Oldvalue:")
    obj2.Studentupdate(colname,newval,refcolname,oldvalue)
if tab==4 and opr==3:
    sid=int(input("Enter Student_id:"))
    obj3.studentdelete(sid)
if tab==4 and opr==4:
    sid=int(input("Enter Student_ID:"))
    obj4.studentreading(sid)
if tab==4 and opr==5:
    obj4.studentWhreading()