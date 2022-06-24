import sqlite3
from tkinter import *

con=sqlite3.connect("assignment_db1.db")


def addInstructorToDataBase(instructor):
    query="insert into Instructor values(?,?,?,?,?)"
    cursor=con.cursor()
    ls=(instructor.name,instructor.gender,instructor.style,instructor.number,instructor.hrRate)
    cursor.execute(query,ls)
    con.commit()
    for days in instructor.availability:
        query = "insert into Instructor_Availability values(?,?)"
        cursor = con.cursor()
        ls = (instructor.name, days)
        cursor.execute(query, ls)
        con.commit()
    print("Completed")


def addStudentToDataBase(student):
    query = "insert into Student values(?,?,?,?,?,?,?,?,?,?,?)"
    cursor = con.cursor()
    ls = (student.stid,student.firstName, student.lastName, student.email, student.gender, student.DOB,student.phone,student.address,student.danceStyle,student.maxHrRate,"")
    cursor.execute(query, ls)
    con.commit()
    print("Completed")


def changeInstructorInDataBase(instructor):
    query = "update Instructor set Gender=?,Style=?,Tp_No=?,HrRate=? where Name=?"
    cursor = con.cursor()
    ls = (instructor.gender, instructor.style, instructor.number, instructor.hrRate,instructor.name)
    cursor.execute(query, ls)
    con.commit()
    print("Completed")

def deleteInstructorInDataBase(instructor):
    query = "delete from Instructor where Name=?"
    cursor = con.cursor()
    ls = (instructor,)
    cursor.execute(query, ls)
    con.commit()
    print("Completed")

def viewAllInstructors():
    query = "select * from Instructor"
    cursor = con.cursor()

    cursor.execute(query)
    rows=cursor.fetchall()
    root=Tk()
    rowCount=len(rows)
    colCount=len(rows[0])
    for i in range(rowCount):
        for j in range(colCount):
            enty=Label(root,width=20)
            enty.grid(row=i, column=j)
            enty['text'] = rows[i][j]


    print("Completed")

def setInstructorToStudents(name):#get student ids of students and set instructor to them

    query1="select Student_Id,Dance_Style,MaxHrRate from Student"
    cursor = con.cursor()

    cursor.execute(query1)
    stuRows = cursor.fetchall()
    query2 = "select Style,HrRate from Instructor where Name='"+name+"'"
    cursor = con.cursor()

    cursor.execute(query2)
    instructor = cursor.fetchall() #assume that we cannot have multiple instructor with same name
    #get students for an instructor
    setStudents=list()
    if(len(instructor)==0):
        print("No such Instructor in database")
    else:
        print("Completed")
        for student in stuRows:
            #check instructors dancing style equals to student dancind method and students hr rate >= instructor hr rate
            if student[1]==instructor[0][0] and student[2]>=instructor[0][1]: #assume that we cannot have multiple instructor with same name
                setStudents.append(student[0])

        for stID in setStudents:

            query3="update Student set Instructor_Name=? where Student_Id=?"
            cursor = con.cursor()
            ls = (name,stID)
            cursor.execute(query3, ls)
            con.commit()
            print("Completed")




def isInsinDB(insNm):
    query = "select * from Instructor where Name='"+insNm+"'"
    cursor = con.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return False
    return rows


def addAbooking(insNme,bookingNo):
    query="select Student_Id from Student where Instructor_Name='"+insNme+"'"
    cursor = con.cursor()

    cursor.execute(query)
    stuRows = cursor.fetchall()
    for stNo in stuRows:
        query1 = "insert into booking values(?,?,?)"
        cursor = con.cursor()
        stNo=stNo[0]
        ls = (stNo,insNme,bookingNo)
        cursor.execute(query1, ls)
        con.commit()
    print("Completed")



