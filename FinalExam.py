# Question 1. 

a = (['A','B'],['F','G','H'])
b = (['C','D','E'],['I','J'])

# # Answer: 
for i,j in zip(a[::-1],b[::-1]):
    for k in j[::-1]:
        print(k)
    for l in i[::-1]:
        print(l)

# output:

# J
# I
# H
# G
# F
# E
# D
# C
# B
# A


# Question 2

array = []
for i in range(5):
    array.append(int(input("Enter a number: ")))


print("Highest number is: ", max(array))
print("Lowest number is: ", min(array))

print('Initial Array - ', array)
for i in array:
    if i==max(array):
        array.remove(i)
    elif i==min(array):
        array.remove(i)
print('After Deleting - ', array)

# output:

# Enter a number: 321
# Enter a number: 43
# Enter a number: 5
# Enter a number: 15
# Enter a number: 34
# Highest number is:  321
# Lowest number is:  5
# Initial Array -  [321, 43, 5, 15, 34]
# After Deleting -  [43, 15, 34]

# Question 3:

class Emp:
    def __init__(self,name,sal,comm, *args,**kwargs):
        super(Emp,self).__init__(*args,**kwargs)
        Total_Sal = sal + comm
        print(name)
        print(Total_Sal)
        
    def message(self):
        print("Welcome")

class Designation:
    def __init__(self,des, *args,**kwargs):
        super(Designation,self).__init__(*args,**kwargs)
        print(des)

class final(Designation,Emp):
    def __init__(self,*args,**kwargs):
        message()
        super(final,self).__init__(*args,**kwargs)
        print('Child Class')

x = final(name='AA',sal = 3000,comm=40,des= 'US')

# Answer:

# 1. The line 1 which is message method declared outside the class is now put in the Emp class
# 2. The line 4 which calls the method message is now shifted under the class final
# 3. The Line 8 has been edited such that Destination class comes before Emp.
# 4. The calling message method has been edited to remove 'self' from it.





# Question 4:
import datetime
# Print that today’s date in mm/dd/yy format
print(datetime.date.today().strftime('%m/%d/%y'))

# A print small version of a day (based on today’s date)
print(datetime.date.today().strftime('%a'))

# Ask the user to enter a number and Print square root the number
num = int(input("Enter a number: "))
print('Square root -',num**0.5)

# Ask the user to enter a number and Print power of the number (Power of 3)
num = int(input("Enter a number: "))
print('Power of 3 -',num**3)

# Ask the user to enter a number Print exponential  of that number
num = int(input("Enter a number: "))
print('Exponential -',num**2.71828)

base = int(input("Enter a base: "))
exponent = int(input("Enter a exponent: "))
print("Exponential Value is: ", base ** exponent)


# Ouput:

# 12/06/22
# Tue
# Enter a number: 4
# Square root - 2.0
# Enter a number: 3
# Power of 3 - 27
# Enter a number: 3
# Exponential - 19.81295094562122
# Enter a base: 2
# Enter a exponent: 3
# Exponential Value is:  8


# Question 5:
a = (['A','B'],['E','F','G'])
b = (['C','D'],['H','I','K'])

for i,j in zip(a,b):
    for h,k in zip(i,j):
        print(h)
        print(k)

# Output

# A
# C
# B
# D
# E
# H
# F
# I
# G
# K
