#Question 1
# Addition from User Input
# Ask the user for two numbers, convert them to integers, and print their sum

print("         question 1")
a=int(input("Enter first number = "))         
b=int(input("Enter second number = "))
print("The sum of two numbers is:",a+b)

# Question 2
# Even or Odd
# Ask the user for a number and check if it’s even or odd. Print the result.

print("         question 2")    
for i in range(2):
 a=int(input("Enter a number = "))
 if a%2==0:
    print("The number is even.")
 else:
    print("The number is odd.")

# Question 3
# First and Last Character
# Take the string "Python" and print its first and last character

print("         question 3")
x="Python"
print("The string is:",x)
print("The first character of string is:",x[0] )
print("The last character of string is:",x[5])

# Question 4
# Area of a Rectangle
# Ask the user for the rectangle’s length and width, calculate the area, and print it

print("         question 4")
a=float(input("Enter the length of rectangle = "))
b=float(input("Enter the width of rectangle = "))
c=a*b
print("The area of rectangle is:",c)

# Question 5
# Reverse a String
# Ask the user for a word and print it in reverse

print("         question 5")
a=input("Enter a word = ")
print("The reverse of the word is :",a[: : -1])