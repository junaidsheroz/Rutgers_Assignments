# Q1. Get the following output.
# Create a 2D Array

# a = (['A','B'],['F','G','H'])
# b = (['C','D','E'],['I','J'])

# # Answer: 
# for i,j in zip(a[::-1],b[::-1]):
#     for k in j[::-1]:
#         print(k)
#     for l in i[::-1]:
#         print(l)

# Question 2

# array = []
# for i in range(5):
#     array.append(int(input("Enter a number: ")))


# print("Highest number is: ", max(array))
# print("Lowest number is: ", min(array))

# print('Initial Array - ', array)
# for i in array:
#     if i==max(array):
#         array.remove(i)
#     elif i==min(array):
#         array.remove(i)
# print('After Deleting - ', array)

# Question 3:

def message():
    print("Welcome")

class Emp:
    def __init__(self,name,sal,comm, *args,**kwargs):
        super(Emp,self).__init__(*args,**kwargs)
        message(self)
        Total_Sal = sal + comm
        print(name)
        print(Total_Sal)
    
class Designation:
    def __init__(self,des, *args,**kwargs):
        super(Designation,self).__init__(*args,**kwargs)
        print(des)

class final(Emp,Designation):
    def __init__(self,*args,**kwargs):
        super(final,self).__init__(*args,**kwargs)
        print('Child Class')
