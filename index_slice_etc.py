#Q.1) Write a python program to concatenate two strings with a space (in between).

#Q.2) Write a python program to display a character according to the given index. Also display a character according to the given reverse indexing.

#Q.3) Write a python program to display a set of characters of a string according to the given range. Also display a set of characters of that string starting from any index to last index.

# Q.4) Write a python program to display a set of characters of a string according to the given reverse indexing.
#Q.5) Write a python program to find and display the reverse of a string.



#1
print(str(input())+" "+str(input()))

#2
x=str(input())
print(x[int(input())])
print(x[int(input())])

#3
x=str(input())
print(x[int(input()):int(input())])
print(x[int(input()):])
#4
x=str(input())
print(x[int(input("-ve indx")):int(input("-ve indx"))])
#5
x=str(input())
print(x[::-1])
