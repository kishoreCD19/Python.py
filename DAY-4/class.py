#creating a class for using the student base list with rollno and grades
class stud :
    'base class for all students'
    def __init__(self,roll_no,grade):
        self.roll_no=roll_no
        self.grade=grade
    def display (self):
        print("roll no: ",self.roll_no  , "grade:",self.grade)
print(stud.__doc__)


// output = base class for all students //
