"""
    Python data types
"""

"""
    DataTypes           classes                         Description
    
    Numeric             int, float, complex             hold the numeric value
    string              str                             hold sequence of character
    sequence            list, tuple, range              hold the collection of items
    Mapping             dict                            holds data in key-value pair form
    Boolean             bool                            hold either true or false
    set                 set, frozenset                  hold collection of unique items 
    
"""


num1 = 5  # -- int 
# print(num1, 'is of type', type(num1))

num2 = 2.0 # -- float
# print(num2, 'is of type', type(num2))

num3 = 1+2j # -- complex
# print(num3, 'is of type', type(num3))


#   ------------------------ LIST-------------------------------------------
"""
    Definition: A list is a collection of items, ordered and mutable. It allows you to store multiple items in a single variable.

    Ordered: Lists maintain the order of elements as they are inserted. The order of items in a list is preserved unless explicitly changed.

    Mutable: Lists are mutable, meaning you can modify them after creation. You can add, remove, or change elements in a list.

    Heterogeneous Elements: Lists can contain elements of different data types - integers, floats, strings, or even other lists.
"""

languages = ["Swift", "Java", "Python"]  # -- list 
# print(languages)

# iteration throught the list 
for language in languages :
    # print(language)
    pass
    
for i in range(len(languages)):
    # print(languages[i])
    pass
    
languages = ["Swift", "Java", "Python"]
languages_copy = languages.copy()

"""
    access the list items 
"""
# print(languages[-1])  # access the item from the end if the python list

# access element at index 0
# print(languages[0])   # Swift

# access element at index 2
# print(languages[2])   # Python

languages.append("german") # append the item
languages.insert(1,"English") # append the item at the specific index 
# print(f"before pop : {languages}")

languages.pop() # remove the item 
# print(f"after pop : {languages}")

languages = languages_copy

del languages_copy # deleting the copy of the language 

# remove specific item from the list, remove java 

languages.remove("Java") # remove the java item by name of the item .
languages.append("Java") # append the java
languages.pop(1) # remove the the java item with the index . 

# print(languages) # printing the list of the languages 

# list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for fruit in fruits :
    if "a" in fruit :
        # adding the fruits in which a appear's 
        newlist.append(fruit)
        
# print(newlist) # list of all the fruits consist alphbet a 

# sorting of the array

thislist = [100, 50, 65, 82, 23]
thislist.sort()
# print(thislist) # sorting asc to desc

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
# print(thislist) # sorting desc to asc

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
# print(thislist) # sorting aphabet vise i.e a-z

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
# print(thislist) # sorting aphabet vise in reverse i.e z-a 

# appending the two list 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
# print(list3)

#---------------------------- TUPLE ----------------------------------

"""
    Tuples are used to store multiple items in a single variable.
    Tuple is one of 4 built-in data types in Python used to store 
    collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
    A tuple is a collection which is ordered and unchangeable.
"""

mytuple = ("apple", "banana", "cherry","cabbage")
# print(mytuple)  # printing the tuple
# print(type(mytuple)) # printing the type of tuple 

"""
    accessing the tuple 
"""
# print(mytuple[-1]) # accessing the last tuple
# print(mytuple[2]) # accessing the 3 tuple 
# print(mytuple[:2]) # acessing the 0 to 2nd tuple
# print(mytuple[1:3]) # accessing 1 to 3rd tuple

"""
    update tuple .
"""

# change tuple value .

x = ("apple", "banana", "cherry")
y = list(x) # getting all the value of the tuple into the list
y.append("grape") # append the "grape" into the list 
x = tuple(y) # updating the x by transforming the list into the tuple 
# print(x) # printing the updated tuple 

# ---------------------------- sets --------------------------------------
"""
    Sets are used to store multiple items in a single variable.
    Set is one of 4 built-in data types in Python used to store collections of data,
    the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
    A set is a collection which is unordered, unchangeable*, and unindexed.
"""
thisset1 = {"apple", "banana", "cherry"} # set always written in curly braces

# duplicate in sets are not allowed 
thisset2 = {"apple", "banana", "cherry", "apple"}

# print(thisset2) # printing the set output : {'cherry', 'apple', 'banana'}

# true and 1 considered as the same valuee 
thisset3 = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset3) # printing , output : {'banana', True, 2, 'cherry', 'apple'}

# false and 0 considered as the same value 
thisset4 = {"apple", "banana", "cherry", False, True, 0}
# print(thisset4) # printing , output : {False, True, 'banana', 'apple', 'cherry'}

# set with integer integer string and boolean 
set1 = {"abc", 34, True, 40, "male"}

# set constructor 
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(type(thisset)) # checking weather tuple type is changed to type set

"""
    access the item in the set 
"""
for i in thisset4:
    # print(i) # iterate the items of the set one by one 
    pass

"""
    adding the set items . 
"""
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") # add the item into the set
# print(thisset) # printing the set

# updating the set with the another set . 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
# print(thisset)

# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
# print(thisset)

"""
    remove the items from the sets 
"""

# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
# print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
# print(thisset)

# remove the random itme using the pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
# print(x)
# print(thisset)

# make the empty set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
# print(thisset)

"""
    set operation on the set .
"""

#       union

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
# print(set3)


#       update

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
# print(set1)


#       intesection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)

# print(x)


#       not duplicate
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
# print(x)

# return the set with the symettric difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

# print(z)

# ------------------------------------- Dictionary ------------------------------

"""
    Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:

"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color" : "yellow"
}

# print(thisdict)
# print(thisdict["brand"])

"""
    accessing the dictinary .
"""
x = thisdict.get("model") # getting the item
# print(x)

x = thisdict.keys()
# print(list(x))

thisdict["color"] = "white" # changing the value

"""
    updating dictionary
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
# print(thisdict)

"""
    removing item from dictionary
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
# print(thisdict)


"""
    nested dictionary .
"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# print(myfamily)