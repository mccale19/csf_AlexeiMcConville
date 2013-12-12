# -*- coding: utf-8 -*-

#Problem 3 (How to create and call a function)
"""
Functions are great tools for cutting down repetition. Make a function that 
    performs the multiplication of three variables. Make the variables:
        a=1
        b=2
        c=3
Call the function multi. Print multi(a,b,c) should print the value 6.
"""

a = 1
b = 2
c = 3
multi = (a * b * c)
print multi

#Problem 4 (Creating Dictionaries, Lists, and lists of dictionaries)
"""
An empty dictionary is d={}, an empty list is l=[]
Say you have multiple dictionaries:
    a = {“a”: 1}
    b = {“b”: 2}
    c = {“c”: 3}
Put these dictionaries into a list called list. But… here’s the catch you can’t
    just type list1=[{“a”: 1}, {“b”: 2}, {“c”: 3}], you have to use the command 
    append!
"append" adds something to the end of a list. So, if you have an empty list 
    (list1=[])
list1.append(2) will now make list1=[2], if you say a=7 list1.append(a) the list
    will now be list1=[2, 7]
"""

a = {"a": 1}
b = {"b": 2}
c = {"c": 3}

list = []
list.append(a)
list.append(b)
list.append(c)

print list

#Problem 5 (Iterate through a list of dictionaries, keys in a dictionary, and values)
"""
You have a list of dictionaries. For each item in the list print one dictionary
    per line.
So the list: a=[{“Pet”: “Cat”, “Name”: “Bob”}, {“Pet”: “Dog”, “Name”:  “Blake”},
    {“Pet”: “Bird”, “Name”: “Tweet”}] would print the first dictionary on a line,
    then the second dictionary on the next line, and so on.  The easiest way to 
    do this is to use a for loop.
You can iterate through a list with: “for i in a” (this means for every index in
    a(the list) the for loop will iterate).
Your output should be:
{“Pet”: “Cat”, “Name”: “Bob”}
{“Pet”: “Dog”, “Name”:  “Blake”}
{“Pet”: “Bird”, “Name”: “Tweet”}
Write the code that performs this task
"""

a = [{"Pet": "Cat", "Name": "Bob"}, {"Pet": "Dog", "Name": "Blake"},
    {"Pet": "Bird", "Name": "Tweet"}] 

for i in a:
    print i

#Problem 6 (Merging two dictionaries)
"""
You have two separate dictionaries now make one dictionary with all the information
    from the first dictionary and the second dictionary.
For example:
    a = {“A”: 1, “B”: 2,  “C”: 3}
    b = {“D”: 4,  “E”: 5} 
Now you need to make a new dictionary with the two combined,like:
    c = {“A”: 1,  “B”: 2,  “C”: 3, “D”: 4,  “E”: 5}
Note: the order in dictionaries doesn’t matter)
Hint: the command to do this can be done with: dictionary=dict(dictionary1.items()+dictionary2.items())
    dictionary, dictionary1, and dictionary2 are where you would put your dictionary names
    items() doesn’t take any arguments just leave it how it is.
"""

a = {"A": 1, "B": 2, "C": 3}
b = {"D": 4, "E": 5}

c = dict(a.items() + b.items())

print c


#Problem 7 (Creating a new dictionary from a list of dictionaries)
"""
You have a list of dictionaries:
    a = [{“State”: “WA”,  “Bird”: “American Goldfinch”,“Nickname”: “The Evergreen State”},
    {“State”: “OR”, “Bird”: “Western Meadowlark”, “Nickname”: “Beaver State”},
    {“State”: “CA”, “Bird”: “California Quail”, “Nickname”: “The Golden State”}]
Now convert this dictionary into a new dictionary with just the value of the 
    state and the value of the nickname. So, the new dictionary would look like:
    thisdictionary={“WA”: “The Evergreen State”, “OR”: “Beaver State”,  “CA”: 
    “The Golden State”}
Hint: create an empty: “dictionary={}” then use a for loop for iteration 
    like you did in Problem 5.
"""

a = [{"State": "WA",  "Bird": "American Goldfinch","Nickname": "The Evergreen State"},
    {"State": "OR", "Bird": "Western Meadowlark", "Nickname": "Beaver State"},
    {"State": "CA", "Bird": "California Quail", "Nickname": "The Golden State"}]
    
for x in a:
    print x["State"]
    print x["Nickname"]

b = x["State"], x["Nickname"]
print b