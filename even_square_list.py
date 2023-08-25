print("Enter a list of numbers:")

user_input = input()
list1 = []
# list1 = eval(user_input)      # Simple evaluation of input

# removing all unnecessary characters that are not numbers from input
for i in user_input:
    try:
        num = int(i)
        list1.append(num)
    except ValueError:
        continue
    
# print(list1)      # test line

# making a new list to store all the even squares
list2 = []
for i in list1:
    if (i%2) == 0:
        list2.append(i*i)

print("Even square list: ", list2)
        