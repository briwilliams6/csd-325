#Work by Brieanna Williams for CIS 245-T303
class student:
    def __init__(self, firstName, lastName):
        self.firstName= firstName
        self.lastName= lastName
        self.grade_points= 0
        self.credits= 0
        self.gpa= 0

    def calculateGPA(self, grade, credits):
        self.credits= self.credits + credits
        if grade== 'A':
            self.grade_points= self.grade_points + (int(credits)*4)
        if grade== 'B':
            self.grade_points= self.grade_points + (int(credits)*3)
        if grade== 'C':
            self.grade_points= self.grade_points + (int(credits)*2)
        if grade== 'D':
            self.grade_points= self.grade_points + (int(credits)*1)
        else:
            self.grade_points= self.grade_points + (int(credits)*0)
        self.gpa= (self.grade_points)/(self.credits)
    
    def getGPA(self):
        print(f'The GPA for {self.firstName} is {round(self.gpa,1)}')
        print(f'The GPa for {other.firstName} is {round(self.gpa,1)}')
        
breakpoint()

class declared_student(student):
    def __init__ (self, firstName, lastName, concentration):
        student.__init__(self, firstName, lastName)
        self.concentration=concentration.upper()
        
    def getConcentration(self):
        return self.concentration
    
    def getYear(self):
        
        
        if self.concentration== 'NA':
            return f"{self.firstName} {self.lastName} has not selected a concentration"
        if self.credits <= 33:
            return f"{self.firstName} {self.lastName} Year One student"
        elif self.credits <= 66:
            return f"{self.firstName} {self.lastName} Year Two student"
        elif self.credits <= 96:
            return f"{self.firstName} {self.lastName} Year Three student"
        elif self.credits <130:
            return f"{self.firstName} {self.lastName} Year Four student"
        else:
            return 'Multiyear student'
        
        
#get first and last names
student_firstName= input('Please enter the student first name: ')
student_lastName= input('Please enter the student last name: ')
student_concentration= input('Please enter the student concentration area.If the student is undeclared, enter NA: ')

student_1= declared_student(student_firstName, student_lastName, student_concentration)

quit= '1'
while quit=='1':
    grade=input('please enter student grade: ')
    credits= input('please enter credits: ')
    
    student_1.calculateGPA(grade, int(credits))
    quit= input('Press 1 to continue entering grades or 2 to quit: ')
    
student_1.getGPA()

student_year=student_1.getYear()
print(student_year)