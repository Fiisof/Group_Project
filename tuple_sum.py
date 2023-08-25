# Task 1: Tuple Sum: Write a python script called ' ' that takes a tuple of integers as input ans returns the sum of all the
#         elements in the tuple. For example, if the input is (1,2,3,4,5), the function should return 15.

def tupleSum(t):
    return sum(t)

print('Enter integers separated by a comma ",":')
user_input = input()

# Splits the string into a list; specified separator is a comma
split_input = user_input.split(',')

tup_list = []                           # Stores the new list
for i in split_input:
    try:
        intcheck = int(i.strip())       # Accepts integers only
        tup_list.append(intcheck)       # Adds each valid input into the list 'tup1'
    except ValueError:                  # Overlooks invalid inputs
        pass

# Converts list into a tuple
tuple1 = tuple(tup_list)

# Prints the valid inputs from user as a tuple as well as an error message for cases of overlooked inputs
print('Your valid tuple is:', tuple1)
print('If there are any missing values, ensure that you input integers only.')

# Calculates and prints the sum of the tuple
tuplesum = tupleSum(tuple1)
print('The sum of your valid tuple is:', tuplesum)