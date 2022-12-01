# def function1():
#     while True:
#         n1 = int(input('Enter number 1: '))
#         n2 = int(input('Enter number 2: '))
#         if n1 == n2:
#             break    

# Ask the User to enter five numbers, store those numbers in ascending order in a single Dimensional array, and print that array
def function2():
    # Create a list to hold the numbers
    numbers = []
    # Ask the user to enter five numbers
    for i in range(5):
        # Ask the user to enter a number
        number = int(input('Enter a number: '))
        # Add the number to the list
        numbers.append(number)
    # Sort the list
    numbers.sort()
    # Print the list
    print(numbers)


