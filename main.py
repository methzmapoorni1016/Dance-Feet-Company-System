from tkinter import *
from Administrator import Administrator
from DanceInstructor import *
from Controller import isInsinDB
from tkinter import messagebox
from tkinter import *


def showAdminFunc():

    print("1 : Add an Dance Instructor")
    print("2 : Delete an Dance Instructor")
    print("3 : Edit an Dance Instructor")
    print("4 : View all Dance Instructors")
    print("5 : Schedule an Dance Instructor")
    print("6 : Register a Student ") 
    choice=int(input("Enter your choice : "))
    if(choice==1):
        Administrator.addInstructor()
    elif(choice==2):
        Administrator.deleteInstructor()

    elif(choice==3):
        Administrator.editInstructor()
    elif(choice==4):
        Administrator.viewInstructors()
    elif(choice==5):
        Administrator.scheduleInstructor()
    elif (choice == 6):
        Administrator.registerStudent()
    else:
        print("Wrong Number Selected!!")



def instructorFunc():

    name=input("Enter Your Name Instructor : ")
    res=isInsinDB(name)
    if(res==False):
        print("You are not registered!!")

    else:
        ins = DanceInstructor(res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], "")
        ins.addLessonBooking()




#once you done with an operation  you must go back to the gui and select the role to do another operation
def administrator_login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Administrator")
    screen2.geometry("300x250")

    global username_admin
    global password_admin
    
    username_admin = StringVar()
    password_admin = StringVar()

    global username_admin1
    global password_admin1
    Label(screen2, text = "Username *").pack()
    username_admin1 = Entry(screen2, textvariable = username_admin)
    username_admin1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password *").pack()
    password_admin1 = Entry(screen2, textvariable = password_admin)
    password_admin1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = "10", height = "1", command = cmd_admin).pack()
    

#Command
def cmd_admin():
    if username_admin1.get()=='admin' and password_admin1.get()=='admin':
        messagebox.showinfo("LOGIN SUCCESSFULLY", "  WELCOME")
        showAdminFunc()
        
    else:
        messagebox.showwarning("LOGIN FAILED"," PLEASE TRY AGAIN")
    
def main_screen ():
    global screen
    screen=Tk()
    screen.geometry("500x250")
    screen.title("DanceFeet Academy")
    Label(text = "DanceFeet Academy", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text = "Administrators", height = "2", width = "20", command=administrator_login).pack() 
    Label(text = "").pack()
    Button(text = "Dance instructors", height = "2", width = "20", command=instructorFunc).pack() #command = instructors
    
    screen.mainloop() 
    
main_screen()







