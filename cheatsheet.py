import random
import string
from collections import defaultdict

w = 'abc'
arr = ['a', 'b', 'c']
abc = {'a': 0, 'b': 0, 'c': 0}

# ________________STRINGS____________________
# lowercase characters
lowercase = string.lowercase

# uppercase characters
uppercase = string.uppercase

# digit characters
digits = string.digits

# copy a string
# strings are immutable in python
# two variable will reference the same address if their values
# are initialized to the same string
wCopy = (w + '.')[:-1]

# list version of string
# given 'abc fgh hij'
# returns ['a', 'b', 'c', ' ', 'f', 'g', 'h', ' ', 'h', 'i', 'j']
w_list = list(w)

# split the string of delimeter, default is " "
# given 'abc fgh hij'
# returns ['abc', 'fgh', 'hij']
w_list = w.split()

# _________________ARRAYS____________________
# given and array covent to a string
''.join(arr)

# reverse a list in place O(n)
reverse_s = arr[::-1]

# get a copy of an array
arr_copy = arr[:]

# pop from an array, takes a parameter default if -1
c = arr.pop()

# add one element of the arr
arr.append(c)

# extend add the element of on arry to the end of another
arr_extend = arr.extend(['c','d','f'])

# remove the first item with specified value
arr.remove('a')

# sort an array
arr.sort()

# sort an array in reverse order
arr.sort(reverse=True)



# _______________DICTIONARY___________________
# creating a dict uses default dict will, create elements in dict upon reference
default_dict = defaultdict(int)

# Create a copy of a dictionary
abcCopy = dict(abc)

# get list of dictionary keys
abc.keys()

# get list of dictionary values
abc.values()

# get list of tuples [(key, values)] for elemtents in dict
abc.items()

# ways iterate through a dictionary
for key in abc:
    abc[key] += 1

for key, val in abc.items():
    None

# delete a key from a dictionary
del abc['a']

# sort a dictionary by key
{k: v for k, v in sorted(abc.items(), key=lambda item: item[0])}

# sort a dictionary by value
{k: v for k, v in sorted(abc.items(), key=lambda item: item[1])}


# _________________TESTING___________________
# Shuffle an array in place in O(n) time
#  Uses this algorithm https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
random.shuffle(arr)