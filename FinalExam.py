# Q1. Get the following output.
# Create a 2D Array

a = (['A','B'],['F','G','H'])
b = (['C','D','E'],['I','J'])

# output
# J
# I
# H
# F
# E
# D
# C
# B
# A

# code to print above output
# solution

for i,j in zip(a,b):
    for k in j:
        print(k,reversed=True)
    # print(i)
    # print(j)