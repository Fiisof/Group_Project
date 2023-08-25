# Task 2: List Comprehension Write a Python function called even_square_list.py that takes a list of integers as input and
#         returns a new list containing the squares of only the even numbers from the original list. For example, 
#         if the input is [1, 2, 3, 4, 5, 6], the function should return [4, 16, 36].

# User input with error handling for non-integer inputs
while (True):
    print("Enter a list of numbers:")
    user_input = input()

    try:
        list1 = eval(user_input)
        break
    except NameError:
        print("Your list is contains non-integer values. Please try again")
        print()

# making a new list to store all the even squares
list2 = []
for i in list1:
    if (i%2) == 0:
        list2.append(i*i)

print("Even square list: ", list2)
        