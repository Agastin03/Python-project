"""
#addition
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=a+b
print("the additon of 5 and 10 is:",c)

#check the maximum value

if(a>b):
    print("a is maximum")
else:
    print("b is maximum")
    
#print prime numbers

x=int(input("enter the value:"))
if(x%2==1):
    print("the given number is prime")
else:
    print("the given number is not prime")
    
    
#factorial of 5
import math
x=5
print(math.factorial(x))

#ascii value
x=(input("enter the element:"))
y=ord(x)
print(y)

#leap year

x=int(input("enter the leap year:"))
if(x%4==0):
    print("the year is leap year")
else:
    print("the year is non leap year")

#area of circle
    
r=7
radius=(22/7)*(r**2)
print(radius)

#voting eligiblity

x=int(input("enter an age:"))
if(x>=18):
    print("you are eligible for voting:")
else:
    print("you are no eligible for voting")
    
#check even or odd    
    
x=int(input("enter the number:"))
if(x%2==0):
    print("the given number is even:")
else:
    print("the given number is even")
#even number(range)

for i in range(1,20):
    if i%2==0:
        print(i)
        """
