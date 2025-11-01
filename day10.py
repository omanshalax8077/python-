# Question 1
# Positive, Negative, or Zero
# Ask the user for a number and check if it is positive, negative, or zero.

print("-------Question 1 ----------")
for i in range(3):
     x=float(input("Enter the number = "))
     if x<0:
      print("The numver is nagative number  ")
     elif x>0:
      print("The number is positive number  ")
     else:
      print("The number is zero ")
print("------------------------------------------------")

# Question 2
# Factorial Using While Loop
# Ask the user for a number and find its factorial using a while loop.

print("--------------Question 2 ----------------")
n = int(input("Enter the number to find factorial = "))
fact=1
while n>0:
    fact=fact*n
    n=n-1
    # print(fact)
    # print(n)
print("The factorial is given number is = " ,fact)
print("------------------------------------")

#Question 3
# Reverse a Number
# Ask the user for a number (example: 1234) and print it in reverse (4321).


print("-------- Question 3--------")
a=int(input("Enter the integer number  = "))
x=0
while a>0:
    b=a%10
    x=x*10+b
    a=a//10
    # print(b)
    # print(x)
    # print(a)
print("The reverse of the number is = ",x)
print("------------------------------------")


#Question 4
# Even or Odd Numbers in a Range
# Ask the user for a number n and print all even and odd numbers from 1 to n

print("-----------Question 4-----------")
n=int(input("Enter the number = "))
print('All Even number is ')
for i in range(1, n+1):
 if i %2==0:
  print(i, end=" ")
print("\n All Odd number is ")
for i in range(1, n+1):
 if i %2!=0:
  print(i, end=" ")
print("------------------------------------")

#Question 5
# Number Guessing (Basic)
# Ask the user to guess a number 
# (you set a number in a variable, example 7). 
# If the guess is correct → print "You guessed it!", otherwise print "Try again!"

print("-----------Question 5-----------")
for i in range(2):
     g=int(input("Enter the guess a number = "))
     if g==21:
        print("You guessed it!")
     else:
           print(" Something is wrong....  Try again... !")
print("------------------------------------")

    
   