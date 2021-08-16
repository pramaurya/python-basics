# **LAB 4**

# Q.1) Write a python program to count the total no. of characters of a given string without space.

# Q.2) Write a python program to check whether a sentence ends with a specific word or not?

# Q.3) Write a python program to check the frequency of a specific character and a specific word within a string.
# Q.4) Write a python program to find the position of a specific word in the given string.

# Q.5) Write a python program to replace an existing sub-string of a string with a new string.

# Q.6) Write a python program to display a sub-string of a string with single quote (‘). Also specify the tab space and new line.
# Write a python program to capitalize the 1st letter of each and every word of a string.

#  Hello cruel world you are really great filled with cruel people.


#s=str(input())
s="Hello cruel world you are really great filled with cruel people."
#1
print(len(s) - s.count(" "))
#2
print(s.endswith("people."))
#3
print(s.count("l"))
print(s.count("cruel"))
#4
print(s.index(("great")))
#5
print(s.replace("cruel","worst"))
#6
print('Hello cruel world \'you are really \t\tgreat filled \nwith cruel people.')
#7
print(str.title(s))
