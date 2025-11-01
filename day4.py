# question 1
# Print Numbers 1 to 10
# Use a for loop to print numbers from 1 to 10

print("         question 1")
for i in range (1,11):#first method
# for i in range(1,1,11) second method
# for i in range(11): third method
    print(i)

# Question 2
# Sum of First 10 Natural Numbers
# Use a loop to calculate and print the sum of numbers from 1 to 10

print("         question 2")
sum=0
for i in range (11):
    print(i,end=" ")
    sum+=i
print("\nThe sum of 1 to 10 ",sum)

# Question 3
# Multiplication Table
# Ask the user for a number and print its multiplication table from 1 to 10

print("         question 3")
number=int(input("Enter the number for multiplication table = "))
for i in range(11):
    print(number,"x",i,"=",number*i)      

# Question 4 
# Count Vowels
# Ask the user for a word and count how many vowels (a, e, i, o, u) it contains

print("         question 4")
a=input("Enter a word to count vowels : ")
vowels="aeiouAEIOU"
count=0
for i in a:
    if i in vowels:
     count+=1 
print(count)

# Question 5
# Factorial
# Ask the user for a number and find its factorial using a loop

print("         question 5")
a=int(input("Enter a number to find factorial ="))
fact = 1
for i in range(1,a +1):
    print(i)
    fact *= i
print("Factorial of", a, "is:", fact)
