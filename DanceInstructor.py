from Student import *
from Controller import *
class DanceInstructor:
    def __init__(self,name,gender,style,number,hrRate,availability):
        self.name=name
        self.gender=gender
        self.style=style
        self.number=number
        self.hrRate=hrRate
        self.availability=availability





    def addLessonBooking(self):

        if(isInsinDB(self.name)):
            bookingNo=input("Enter Booking Number : ")
            print("Compleyed")
            addAbooking(self.name,bookingNo)
        else:
            print("You are not registered!!")




