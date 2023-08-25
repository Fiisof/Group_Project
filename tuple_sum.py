# Task 1: Tuple Sum: Write a python script called ' ' that takes a tuple of integers as input ans returns the sum of all the
#         elements in the tuple. For example, if the input is (1,2,3,4,5), the function should return 15.


def tupleSum(t):
    return sum(t)

print('Enter integers separated by a comma ",":')
user_input = input()
split_input = user_input.split(',')

tup1 = []
for i in split_input:
    try:
        intcheck = int(i.strip())
        tup1.append(intcheck)
    except ValueError:
        pass
# Converts strings into tuples(integers) internally

print('Your valid tuple is:')
print(tup1)
# Prints tuple

# Calculates the sum of the tuple
tuplesum = tupleSum(tup1)
print('The sum of your tuple is:')
print(tuplesum)