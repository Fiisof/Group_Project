#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Dictionary merge write a python function called '' that takes two dictionaries as input and prints a new dictionary
# containing all the key-value pairs from both dictionaries. If there are common keys, the value from the second dictionary
# should overwrite the value from the first dictionary


# ## Hardcoded Version

# In[14]:


def Merge(dict1, dict2):
    return(dict1.update(dict2))

dict1 = {"a":1, "b":2}
dict2 = {"b":3, "c":4}

Merge(dict1,dict2)

print(dict1)


# ## Accepts User Inputs

# In[12]:


def Merge(dictA, dictB):
    return(dictA.update(dictB))

print('Please enter the number of values for the first dictionary')
n = input()
m = input()
n = int(n)
m = int(m)

dictA = {}
dictB = {}
def inputDictA(n,m):
    dictA = {}
    dictB = {}
    for i in range(n):
        key = input("Key for the dictionary: ")
        value = input("Value binded to the key: ")
        dictA[key] = value
        
    for i in range(m):
        key = input("Key for the dictionary: ")
        value = input("Value binded to the key: ")
        dictB[key] = value
        
#     print("DictA:", dictA)
#     print("DictB:", dictB)

    Merge(dictA,dictB)
    print("Merged dictionaries:",dictA)

inputDictA(n,m)

