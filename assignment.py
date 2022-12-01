# Question 1: Create 2 D array and get following output
a=(['A','B'],['F','G','H'])
b=(['C','D','E'],['I','J'])
print("Length of Array-a is",len(a))
print("Length of Array-b is",len(b))
for i,j in zip(a,b):
    for k in i:
        print(k)
    for l in j:
        print(l)

# Question 2: Create 2D array and get following output
a=(['A','B'],['F','G','H'])
b=(['C','D','E'],['I','J'],['K'])
print("Length of Array-a is",len(a))
print("Length of Array-b is",len(b))
for i,j in zip(a,b):
    for k in i:
        print(k)
    for l in j:
        print(l)
    for m in b[2]:
        print(m)

# Question 3: Create your function module for the following two questions and import your library to execute functions: 
import module

module.function1()
module.function2()

# Question 4: Use Object-Oriented concepts


def welcome():
    print("Welcome to the program")

class Demographics:
    def __init__(self, Id, Age, Gender,In_state=None):
        self.Id = Id
        self.Age = Age
        self.Gender= Gender
        self.In_state = input('Are you in state? (Yes/No): ')
    
    def calculate_fee(self):
        if self.In_state == 'Yes':
            self.fees =560
            return self.fees
        else:
            self.fees = 913
            return self.fees

class Grade:
    def __init__(self, Maths, Sci, Eng):
        self.Maths = Maths
        self.Sci = Sci
        self.Eng = Eng

    def calculate_grades(self):
        self.total = self.Maths + self.Sci + self.Eng
        self.average = self.total/3
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 70:
            self.grade = 'F'
        return self.grade

class final(Demographics, Grade):
    # Use all attributes and generate the student’s transcript. (Print all values)
    welcome()
    def __init__(self, Id, Age,Gender, Maths, Sci, Eng):
        Demographics.__init__(self,Id,Age,Gender)
        Grade.__init__(self,Maths,Sci,Eng)
        self.Id = Id
        self.Age = Age
        self.Gender = Gender
        self.Maths = Maths
        self.Sci = Sci
        self.Eng = Eng
        self.fees = Demographics.calculate_fee(self)
        self.total = Grade.calculate_grades(self)
    
    def transcript(self):
        print("Student ID: ", self.Id)
        print("Student Age: ", self.Age)
        print('Student Gender', self.Gender)
        print('In state: ', self.In_state)
        print("Maths: ", self.Maths)
        print("Science: ", self.Sci)
        print("English: ", self.Eng)
        print('Fees: ',self.fees)
        print("Grades: ", self.total)
# callable function
student1 = final(1, 20,'Male', 90, 80, 70)
student1.transcript()
