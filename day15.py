# # Input a year and find whether it is a leap year or not

print("-----------Question 1-------------")
y=int(input("Enter tha year = "))
if y%400==0 or (y%4==0 and y%100!=0):
    print("YES, it's a leap year ")
else:
     print("NO, it's a leap year ")
print("------------------------------------")

# # Take two numbers and print the sum of both.

print("-----------Question 2---------------")
x=float(input("Enter a number = "))
y=float(input("Enter a number = "))
print("The sun of two number is =",x+y)
print("------------------------------------")

# Take a number as input and print the multiplication table for it.

print("-----------Question 3 -------------")
a=int(input('Enter the number when for print a  multiplication. \n Number is = '))
for i in range(11):
    print(a,"X",i,"=",a*i)
print("------------------------------------")

# Take 2 numbers as inputs and find their HCF and LCM.

print("-------------Question 4 ------------")
x=int(input("Enter the x number = ")) 
y=int(input("Enter the y number = ")) 
print("     Calculate HCF... ")
if x<y:
    print("The smallest number x =", x)
    s=x
    # print(s)
elif y<x:
    print("The smallest number is y =",y)
    s=y
    # print(s)
print("Common factor are =", end=" ")
H=1
for i in range(1,s+1):
    # print(i)
    if x%i==0 and y%i==0:
        print(i,end=" ")
        H=i
print("\nHCF of x and y =",H)
print("     Calculate LCM... ")
L=x*y//H
print("LCM of x and y = ",L)
print("-----------------------------------------")

#Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all

print("-------------Question 5-------------")
total=0
while True:
    a=input("Enter a number (or 'x' to stop)= ")
    if a.lower()=='x':
        break
    else:
        total+=int(a)
print("Sum of all number to given by user",total)
print("-----------------------------------------")


# Write a program to print whether a number is even or odd,
# also take input from the user.

print("-------------Question 6------------")
x=int(input("Enter the number to chack a whether is Even or Odd = "))
if x%2==0:
    print("The number is Even :")
else:
    print("The number is Odd  :")
print("-----------------------------------------")

# Take name as input and print a greeting message for that particular name

print("-------------Question 7------------")
x=(input("\nPLzese Enter your Name Sir..\n"))
print("\nGood Morning ... ",x.upper(),"\n🌟Welcome ...!🌟\nto the world of " \
"Python🚀\n Have a nice Day",x.upper(),"\nThankyou 😃")
print("-----------------------------------------")


# Write a program to input principal, 
# time, and rate (P, T, R) from the user and find Simple Interest.

print("-------------Question 8------------")
P=int(input("Enter the Principal Amount = "))
T=int(input("Enter the Time in months = "))
R=int(input("Enter the  Rate in Percentag = "))
F=(P*R*T)/(100)
total=P
total+=F
print("Amount of rate is = ",F)
print("Total amount = ",total)
print("-----------------------------------------")


# Take in two numbers and an operator (+, -, *, /) 
# and calculate the value. (Use if conditions)

print('''THERE ARE TWO OR MORE METHODS TO SOLVE ANY PROBLEM.  
 METHOD 1 IS VERY BASIC  
AND METHOD 2 IS A LEVEL UP OF PYTHON.''') 
print(" METHOD 1") 
print("-------------Question 9-------------")
x=int(input("Enter the number = 'x' = "))
y=int(input("Enter the number = 'y' = "))
z=0
if x+y:
    z+=x+y
    print(z)
a=0
if x-y:
    a+=x-y
    print(a)
b=0
if x*y:
    b+=x*y
    print(b)
c=0
if x/y:
    c+=x/y
    print(c)
print("-----------------------------------------")
print(" METHOD 2") 
print("-------------Question 9-------------")
x=int(input("Enter the number = 'x' = "))
y=int(input("Enter the number = 'y' = "))
for i in range(5):
     a=input("Enter operator[/*-+]= ")
     if a=="+":
      print(x+y)
     elif a=="-":
      print(x-y)
     elif a=="*":
      print(x*y)
     elif a=="/":
      print(x/y)
     else:
      print("not define ")
print("-----------------------------------------")


# # Take 2 numbers as input and print the largest number.

print("-------------Question 10-------------")
x=int(input("Enter the number = "))
y=int(input("Enter the number = "))
if x>y:
    print("largest number = ",x)
else:
    print("largest number = ",y)
print("-----------------------------------------")


# Input currency in rupees and output in USD

print("-------------Question 11-------------")
x=int(input("Input currency in rupees = "))
D=0.0118
print("output in USD = ",x*D)
print("-----------------------------------------")


# To calculate Fibonacci Series up to n numbers.
print("-------------Question 12-------------")
x=int(input("Enter the number = "))
a=0
b=1
print("Fibonacci Series = ")
for i in range(x):
    print(a,end=" ")
    a,b=b,a+b
print("\n-----------------------------------------")


# To find out whether the given String is Palindrome or not

print("-------------Question 13-------------")
a=input("Enter a string = ")
if a==a[::-1]:
    print("The given string is Palindrome")
else:
    print("The given string is not Palindrome")
print("-----------------------------------------")


# Area Of Circle 
print("-------------Question 14-------------")
r=float(input("Enter the radius of circle = "))
pi=22/7
A=pi*r*r
print("Area of circle = ",A)
print("-----------------------------------------")
  

# Area Of Triangle
print("-------------Question 15-------------")
b=float(input("Enter the base of triangle = "))
h=float(input("Enter the height of triangle = "))
A=1/2*b*h
print("Area of triangle = ",A)
print("-----------------------------------------")


# Area Of Rectangle Program
print("-------------Question 16-------------")
l=float(input("Enter the Length of rectangle = "))
b=float(input("Enter the Breadth of rectangle = "))
A=l*b
print("Area of rectangle = ",A)
print("-----------------------------------------")


# Area Of Isosceles Triangle
print("-------------Question 17-------------")
h=float(input("Enter the height of isosceles triangle = "))
b=float(input("Enter tha base of isosceles triangle = "))
A=(b*h)/2
print("Area of isosceles triangle = ",A)
print("-----------------------------------------")


# Area Of Parallelogram
print("-------------Question 18-------------")
b=float(input("Enter the base of parallelogram = "))
h=float(input("Enter the height of parallelogram = "))
A=b*h
print("Area of parallelogram = ",A)
print("-----------------------------------------")


# Area Of Rhombus
print("-------------Question 19-------------")
d1=float(input("Enter the first diagonal of rhombus = "))
d2=float(input("Enter the second diagonal of rhombus = "))
A=(d1*d2)/2
print("Area of rhombus = ",A)
print("-----------------------------------------")


# Area Of Equilateral Triangle
print("-------------Question 20-------------")
a=float(input("Enter the side of equilateral triangle = "))
A=(1.73/4)*a**2
print("Area of equilateral triangle = ",A)
print("-----------------------------------------")


# Perimeter Of Circle
print("-------------Question 21-------------")
pi=21/7
r=float(input("Enter the radius of circle = "))
P=2*pi*r
print("Perimeter of circle = ",P)
print("-----------------------------------------")


# Perimeter Of Equilateral Triangle
print("-------------Question 22-------------")
a=float(input("Enter the side of equilateral triangle = "))
P=3*a
print("Perimeter of equilateral triangle = ",P)
print("-----------------------------------------")


# Perimeter Of Parallelogram
print("-------------Question 23-------------")
b=float(input("Enter the base of parallelogram = "))
a=float(input("Enter the side of parallelogram = "))
P=2*(a+b)
print("Perimeter of parallelogram = ",P)
print("-----------------------------------------")


# Perimeter Of Rectangle
print("-------------Question 24-------------")
l=float(input("Enter the Length of rectangle = "))
b=float(input("Enter the Breadth of rectangle = "))
P=2*(l+b)
print("Perimeter of rectangle = ",P)
print("-----------------------------------------")


# Perimeter Of Square
print("-------------Question 25-------------")
a=float(input("Enter the side of square = "))
P=4*a
print("Perimeter of square = ",P)
print("-----------------------------------------")

# Perimeter Of Rhombus
print("-------------Question 26-------------")
a=float(input("Enter the side of rhombus = "))
P=4*a
print("Perimeter of rhombus = ",P)
print("-----------------------------------------")


# Volume Of Cone 
print("-------------Question 27-------------")
r=float(input("Enter the radius of cone = "))
h=float(input("Enter the height of cone = "))
pi=22/7
V=pi*r**2*h/3
print("Volume of cone = ",V)
print("-----------------------------------------")


# Volume Of Prism
print("-------------Question 28-------------")
h=float(input("Enter the Height of prism = "))
A=float(input("Enter the Area of base of prism = "))
V=A*h
print("Volume of prism = ",V)
print("-----------------------------------------")


# Volume Of Cylinder
print("-------------Question 29-------------")
r=float(input("Enter the radius of cylinder = "))
h=float(input("Enter the height of cylinder = "))
pi=22/7
V=pi*r**2*h
print("Volume of cylinder = ",V)
print("-----------------------------------------")


# Volume Of Pyramid
print("-------------Question 30-------------")
l=float(input("Enter the Length of pyramid = "))
w=float(input("Enter the Width of pyramid = "))
h=float(input("Enter the Height of pyramid = "))
V=l*w*h/3
print("Volume of pyramid = ",V)
print("-----------------------------------------")


# Curved Surface Area Of Cylinder
print("-------------Question 30-------------")
r=float(input("Enter the radius of cylinder = "))
h=float(input("Enter the height of cylinder = "))
pi=22/7
CSA = 2*pi*r*h
print("Curved Surface Area of cylinder = ",CSA)
print("-----------------------------------------")


# Total Surface Area Of Cube
print("-------------Question 32-------------")
a=float(input("Enter the side of cube = "))
TSA=6*a**2
print("Total Surface Area of cube = ",TSA)
print("-----------------------------------------")


# Fibonacci Series
print("-------------Question 33-------------")
n=int(input("Enter the number of terms = "))
a,b=0,1
print("Fibonacci Series = ")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print("\n------------------------------------------")


# Subtract the Product and Sum of Digits of an Integer
print("-------------Question 34------------")
n=int(input("Enter the number = "))
pro=1
sum=0
while n>0:
    digite=n%10
    sum+=digite
    pro*=digite
    n=n//10
result=pro-sum
print("The sum of the number is =",sum)
print("The product of the number is =",pro )
print("Subtract the Product and Sum of Digits = ",result)
print("-----------------------------------------")


# Input a number and print all the factors of that number (use loops).
print("-------------Question 35-------------")
n=int(input("Enter the number = "))
print("Factors of ",n,"is = ",end=" ")
for i in range(1,n+1):
 if n%i==0:
  print(i,end=" ")
print("\n------------------------------------------")


# Take integer inputs till the user enters 0 and print the sum of all numbers
print("-------------Question 36-------------")
sum=0
while True:
    a=int(input("Enter the number {stop to enter 0} = "))
    if a==0:
        break
    else:
        sum+=a
print("sum of all number to given by ueser = ",sum)
print("------------------------------------------")


# Take integer inputs till the user enters 0 and print the largest number from all.
print("-------------Question 37-------------")
big=0
while True:
    a=int(input("Enter the number {stop to enter 0} = "))
    if a==0:
        break
    elif a>big:
        big=a
print("the largest number from all = ",big)
print("------------------------------------------")


# Addition Of Two Numbers
print("-------------Question 38-------------")
x=float(input("Enter the number = "))
y=float(input("Enter the number = "))
print("sum of two number is = ",x+y)
print("------------------------------------------")


# Factorial Program
print("-------------Question 39-------------")
x=int(input("Enter the number = "))
for i in range(1,x+1):
    if x%i==0:
        print(i)
print("----------------------------------------")


# Calculate Electricity Bill
import datetime
print("-------------Question 40-------------")
a='Electricity Bill'
now= datetime.datetime.now() 
print(a.upper())
print("Data - ",now.date())
print("Time - ",now.time())
print("Bill No - 33102145472 \n Name - Python ")
u=float(input("Enter the unit of a electricity bill = "))
x=6.8
if u<=69:
    print("No Bill ....")
elif u<=149:
    print("Only pay Electricity charges = Rs.250/-")
elif u>=150:
    print("Total Amount = ",x*u)
print("Thnakyou")
print("----------------------------------------")


# Calculate Average Of N Number  
print("-------------Question 41-------------")
X=int(input("Enter the N number = "))
sum=0
for i in range(1,X+1):
    sum+=i
print("Sum of tha N number = ",sum)
R=sum/X
print("Avrage of tha N number = ",R)
print("----------------------------------------")


# Calculate Discount Of Product
print("-------------Question 42-------------")
A = input("Enter the name of a product : ")
print('''Product price above 1000 then discount 2%
Product price above 5000 then discount 5%
Product price above 10000 then discount 10%''')
P = float(input("Enter the price of the product = "))
if P>10000:
    D=10
elif P>5000:
    D=5
elif P>1000:
    D=2
else:
    D=0 
dis=(P*D)/100
total=P-dis
print("Discount % = ",D)
print("Discount Amount = ",dis)
print("You pay the amount = ",total)
print("--------------------------------------")


# Calculate Distance Between Two Points
print("-------------Question 43-------------")
a=float(input("Enter the first point distance = "))
b=float(input("Enter the second point distance = "))
print("distance between two point = ",abs(a-b))
print("--------------------------------------")


# Calculate Commission Percentage
print("-------------Question 44-------------")
Commission_Amount=int(input("Enter tha Commission Amount = "))
Sales_Revenue=int(input("Enter tha Sales or Revenue amount = "))
Commission_Rate=(Commission_Amount / Sales_Revenue)*100
print("Commission Percentage ",Commission_Rate,"%")
print("--------------------------------------")


#Power In python
print("-------------Question 45-------------")
a=int(input("Enter the number = "))
p=int(input("Enter the power = "))
R=a**p
print("result",R)
print("-------------------------------------------")


#Calculate Depreciation of Value
print("-------------Question 46-------------")
Asset_Cost=float(input("Enter the Asset Cost = "))
Salvage_Value=float(input("Enter the Salvage Value = "))
Useful_Life= int(input("Enter the Useful Life in years = "))
Annual_Depreciation=(Asset_Cost-Salvage_Value)/Useful_Life
print("Depreciation of Value =",Annual_Depreciation)
print("-------------------------------------------")


# Calculate Batting Average
print("-------------Question 47-------------")
Scored=int(input("Enter the Scored of batsman = "))
Dismissal=int(input("Enter tha Dismissal of batsman = "))
P=Scored/Dismissal
print("Batting Average =",P)
print("-------------------------------------------")


# # Calculate GPA and CGPA 
print("-------------Question 48-------------")
print("Calculate CGPA..\nFist of all calculate tha GPA")
print("Calculate GPA ")
e=int(input("Enter the total numbers of subject ="))
sum=0
aad=0
ad=0
for i in range(1,e+1):
    s=(input("Enter the name of subject = "))
    ga=input("Enter the grade = ")
    g=int(input("Enter the Grade point of a subjet = "))
    c=int(input("Enter the credit hours of a subject = "))
    t=g*c 
    print("multiplication of grade point and credit hours = ",t)
    sum+=t
    print("addation of grade point and credit hours =",sum)
    aad+=c
    ad+=g
print("total addation of Grade point ",ad)
print("total addation of credit hours ",aad)
print("total addation of grade point and credit hours ",sum)
GAP=sum/aad
print("GPA is = ",GAP)
print("\nCalculate CGPA..")
s=int(input("Enter the number of semesters = "))
gpa=float(input("Enter the total GPA of all semesters = "))
CGPA=gpa/s
print("CGPA is = ",CGPA)
print("---------------------------------------------")


# # Compound Interest
print("-------------Question 49-------------")
P = int(input("Enter the principal amount = "))
R = int(input("Enter the rate(per year, in %) = "))
T = int(input("Enter the time in year = "))
A = P*(1+R/100)**T
CI= A-P
print("final amount after interest =",A)
print("compound interset =",CI)
print("----------------------------------------")


# # Calculate Average Marks
print("------------Question 50------------")
e=int(input('Enter the total number of a subject = '))
add=0
for i in range(1,e+1):    
    s=input("Enter the Name of a Subject : ")
    m=float(input("Enter the number of a subject ="))
    add+=m
print("Total number of all subject = ",add) 
A=add/e
print("avrage of the mark = ",A)
print("------------------------------------")


#Sum Of N Numbers
print("------------------- Question  51-----------------")
sum=0
N=int(input("Enter the N number = "))
for i in range(1,N+1):
    sum+=i
print("sum of N number are = ",sum)
print("-------------------------------------------------")


# Armstrong Number
print("--------------Question 52--------------")
x=int(input("Enter the number ="))
y=x
sum=0
while x>0:
    d=x%10
    # print(d)
    sum+=d**3
    # print(sum)
    x=x//10
    # print(x)
if sum==y:
    print("number is ast")
else:
    print('no')
    


# Reverse A String
print("------------------Qustion 53-----------------")
x=input("Entr the string = ")
rev=x[::-1]
print(x)
print(rev)
print("---------------------------------------------")

# Future Investment Value
print("------------------Question 54----------------- ")
P=int(input("enter the Principal value = "))
r=int(input("enter the rate in year  = "))
n=int(input("enter the compound fequency = "))
t=int(input("Enter the rate of intrest = "))
FV=P*(1+r/n)**n*t
print("future investment",FV)