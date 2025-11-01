# Question 1
# Sum of Even Numbers
# Ask the user for a number n and print the sum of all even numbers from 1 to n

print("-------- Question 1 --------")
n=int(input(" Enter a n number to find the sum of all even number =  "))
sum=0
for i in range(1,n+1):
    if i%2==0:
       print(i)
       sum=sum+i
print("The sum of all even number up to n = " ,sum)
print("------------------------------------------------")

# Question 2
# Float to Integer
# Take a floating-point number from the user, type cast it to integer, and print the result.

print("-------- Question 2 --------")
a=float(input("Enter a  number =  "))
print("The type of a variable a is = ",type(a))
b=int(a)
print("The type of b variable is = ",type(b))
print(b)
print("------------------------------------------------")

# Question 3
# Digit Counter
# Take a number from the user and count how many digits it has

print("-------- Question 3 --------")
n= int(input("Enter a number to count the digits = "))
sum=0
for i in range(n):
    while n>0:
     n=n//10
     sum=sum+1
print("The number of digits in the number is = ",sum )
# print("------------------------------------------------")

# Question 4
# Swap Numbers
# Take two numbers from the user and swap them without using a third variable

print("-------- Question 4 --------")
a=int(input("Enter a first number = "))
b=int(input("Enter a second number = "))
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
print("------------------------------------------------")

# Question 5
# Palindrome Check
# Ask the user for a string and check if it is a palindrome (same forwards and backwards).

print("-------- Question 5 --------")
for i in range(2):
  s=(input("Enter the string to check palindrome = "))
  if s==s[::-1]:
   print("The string is palindrome")
  else:
   print("The string is not palindrome")

print("------------------------------------------------")

# Question 6
# Palindrome Check
# Ask the user for a integer number and print its reverse.

print("-------- Question 6 --------")
a=int(input("Enter the integer number  = "))
x=0
while a>0:
    b=a%10
    x=x*10+b
    a=a//10
    print(b)
    print(x)
    print(a)
print("The reverse of the number is = ",x)

