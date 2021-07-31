print("Q.1) Write a python program to find the area and circumference of a circle according to the given radius value.\n\n")
r = int(input())
print("area of circle ", r*r*3.14)
print("circumference ", 2*3.14*r)

print("Q.2) Write a python program to calculate the simple interest of the given P,T,R.\n")
print("SI ", int(input())*int(input())*int(input())*0.01)


print("Q.3) Write a python program to input a 3-digits number and display its 1st and last digit.\n")
x=int(input())
print("frst dg ",(x%10))
print("Last dg ",(x//100))


print("Q.4) Write a python program to input a value as seconds and convert it into hour, minute and seconds (using operators).\n")
x= int(input())
s=x%60
m=(x//60)%60
h=(x//60)//60
print(h, m, s)

print("Q.5) Write a python program to input a 3-digits number, then find and display its reverse (using operators).\n")
n=int(input())
a=n%10
z=n//10
b=z%10
y=n//100
c=y%10
print(str(a)+str(b)+str(c))

print("Q.6) Write a python program to input two numbers, and check both are equal or not using comparison operator.\n")

print (int(input())==int(input()))


print("Q.7) Write a python program to input two numbers and find the biggest one (using operators).\n")

x=int(input())
y=int(input())
print(int(x>y)*x or int(x<y)*y)

print("Q.8) Write a python program to input three numbers as a,b,c, then display 1 if those are sides of a triangle otherwise display 0 on the screen (using operators).\n")
a=int(input())
b=int(input())
c=int(input())
print(int((a + b > c) or (a + c > b) or (b + c > a)))

