# question 1
# String Length
# Store "Python programming" in a variable and print its length using len()

print("         question 1")
a=" python programming"
print(a)
print("The length of the string is:",len(a))

# question 2
# String Slicing
# Take the string "Python" and print only "Pyt".

x="python"
print("         question 2")
print(x)
print("After sliced the string is:", x[0:3])

# question 3
# Multiplication
# Create two variables a = 6 and b = 7, and print their multiplication result

a,b=6,7
print("         question 3")
print("The value of a is =",a)
print("The value of b is =",b)
print("The multiplication of a and b is =",a*b)

# question 4
# Square of a Number
# Ask the user for a number, convert it to an integer, and print its square

print("         question 4")
a= input("Enter a number to find its square: ")#asking user for input
print(type(a),a)
a=int(a)  #converting string to integer
print(type(a),a)
print("The square of the number is:", a**2)

# question 5
# String Replace
# Take the string "I love Java" and replace "Java" with "Python", then print the result

print("         question 5")
a="I love Java"
print(a)
b=a.replace("Java","Python")
print("After replacing 'Java' with 'Python':" ,b)
