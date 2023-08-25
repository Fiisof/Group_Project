#!/usr/bin/env python
# coding: utf-8

# In[1]:


# list comprehension write a python function called '' that takes list of integers as input and returns a new list
# containing the squares of only even numbers from the original list. For example, if the input is [1,2,3,4,5,6],
# the function should return [4,16,36]


# In[24]:


list_int = [1,2,3,4,5,6]
list_sqr = []

for i in range(len(list_int)):
    if list_int[i]%2==0:
        list_sqr = list_sqr + [list_int[i]*list_int[i]]
        
print(list_sqr)


# In[25]:


# Dictionary merge write a python function called '' that takes two dictionaries as input and prints a new dictionary
# containing all the key-value pairs from both dictionaries. If there are common keys, the value from the second dictionary
# should overwrite the value from the first dictionary


# In[33]:


def Merge(dict1, dict2):
    return(dict1.update(dict2))

dict1 = {"a":1, "b":2}
dict2 = {"b":3, "c":4}

Merge(dict1,dict2)

print(dict1)


# In[ ]:


# Tuple Sum: Write a python script called ' ' that takes a tuple of integers as input ans returns the sum of all the
# elements in the tuple. For example, if the input is (1,2,3,4,5), the function should return 15.


# In[ ]:


def tupleSum(t):
    return sum(t) 

print('Enter integers separated by a comma ",".')
user_input = input()
tup1 = eval(user_input)

print('Your tuple is:')
print(tup1)

tuplesum = tupleSum(tup1)
print('The sum of your tuple is:')
print(tuplesum)

