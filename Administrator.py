from Student import *
from DanceInstructor import DanceInstructor
from Controller import *



class Administrator(object):

    @staticmethod
    def addInstructor():
        name=input("Enter Instructor Name : ")
        gender = input("Gender : ")
        danceStyle = input("Enter Dance Style : ")
        No = input("Enter Contact number : ")
        hrRate = input("Enter Hour Rate : ")
        availability=list()
        print("Enter Days Available : (press 1 to end)")
        while(True):
            day=input(" Enter day : ")
            if(day=='1'):
                break
            availability.append(day)
        addInstructorToDataBase(DanceInstructor(name,gender,danceStyle,No,hrRate,availability))


    @staticmethod
    def editInstructor():
        name = input("Enter Dance Instructor Name Want To Change : ")
        gender = input("Change Gender : ")
        danceStyle = input("Change Dance Style : ")
        No = input("Change Contact No : ")
        hrRate = input("Change Hour Rate : ")
        availability = list()
        # assume here you are unable to edit available dates
        changeInstructorInDataBase(DanceInstructor(name, gender, danceStyle, No, hrRate, availability))

    @staticmethod
    def deleteInstructor():
        Iname=input("Enter Name Of Dance Instructor You Want To Remove :")
        deleteInstructorInDataBase(Iname)


    @staticmethod
    def viewInstructors():
        viewAllInstructors();

    @staticmethod
    def scheduleInstructor():
        insName=input("Enter Dance Instructor Name : ")
        setInstructorToStudents(insName)

    @staticmethod
    def registerStudent():
        studentId= input("Enter A Student ID : ")
        firstName = input("Enter Student First Name : ")
        surName = input("Enter Student Last Name : ")
        email = input("Enter Student Email : ")
        gender = input("Enter Gender : ")
        dob = input("Enter Student DOB : ")
        phoneNo = input("Enter Student Contact Number : ")
        address = input("Enter Student Address : ")
        danceStyle = input("Enter Dance Style : ")
        maxHrRate = input("Enter Maximum HourRate : ")
        addStudentToDataBase(Student(studentId,firstName,surName,email,gender,dob,phoneNo,address,danceStyle,maxHrRate))

