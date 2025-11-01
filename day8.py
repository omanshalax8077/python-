#Question 1 
# Largest of Two Numbers
# Ask the user for two numbers and print which one is larger

print("------Question 1-------")
x=float(input("Enter the first number = ")) 
y=float(input("Enter the second number = "))
if x>y:
    print("The Largest Number is = ",x)
else:
    print("The Largest Number is = ",y) 
print("---------------------------------------")

#Question 2
# String Length Without len()
# Take a string from the user and find its length without using len() function.

print("------Question 2-------")
s=input("Enter the string = ")
count=0
for i in s:
    if i==" ":
        count-=1
    count+=1
print("The Length of the strinh is = ", count ) 
print("---------------------------------------")

#Question 3
# Sum of First N Numbers
# Ask the user for a number n and calculate the sum of numbers from 1 to n.

print("------Question 3-------")
n=int(input("Enter the number = "))
sum=0
for i in range(1,n+1):
    print(i)
    sum+=i
print("Sum of the n number is =  ",sum)
print("---------------------------------------")

#question 4
# Count Uppercase and Lowercase Letters
# Take a string input and count how many uppercase and lowercase letters it has.

print("------Question 4-------")
x=input("Enter the string = ")
upper=0
lower=0
for i in x:
    if i.isupper():
        upper+=1
    elif i.islower():
      lower+=1
print("lower case letter is = ",lower )
print("upper case letter is = ",upper )
print("---------------------------------------")

# #Question 5
# # FizzBuzz
# # Print numbers from 1 to 20, but:
# # If the number is divisible by 3 → print "Fizz"
# # If divisible by 5 → print "Buzz"
# # If divisible by both → print "FizzBuzz


print("------Question 5-------")
for i in range(1, 21):
    if i % 3 == 0 :
        print("Fizz", i)
    elif i % 5 == 0 :
        print("Buzz", i)
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
    else:
        print(i)
print("---------------------------------------")