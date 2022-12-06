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

#  Ask total of 5 numbers from the user and store them in the array.

array = []
for i in range(5):
    array.append(int(input("Enter a number: ")))


print("Highest number is: ", max(array))
print("Lowest number is: ", min(array))

print('Initial Array - ', array)
for i in array:
    if i==max(array) or i==min(array):
        array.remove(i)

print('After Deleting - ', array)
