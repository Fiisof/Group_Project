# Task 1: Tuple Sum: Write a python script called ' ' that takes a tuple of integers as input ans returns the sum of all the
#         elements in the tuple. For example, if the input is (1,2,3,4,5), the function should return 15.

def tupleSum(t):
    return sum(t) 

print('Enter integers separated by a comma ",".')
user_input = input()
tup1 = eval(user_input)
# Converts strings into tuples(integers) internally

print('Your tuple is:')
print(tup1)
# Prints tuple

# Calculates the sum of the tuple
tuplesum = tupleSum(tup1)
print('The sum of your tuple is:')
print(tuplesum)