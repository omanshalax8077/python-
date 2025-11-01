
#Question 1
# Squares of Numbers
# Use a loop to print the squares of numbers from 1 to 10.

print("         question 1")
for i in range (11):
    print(i, "suuare is ",i**2)

# Question 2
# Palindrome Check
# Ask the user for a word and check if it is a palindrome (same forward and backward). Print "Yes" or "No".

print("         question 2")
for i in range(2):
 a=(input("Enter a word to check palindrome = "))
 if a==a[::-1]:
  print("YES it is a palindrome")
 else:
  print("NO it is not a palindrome")

# Question 3
# Sum of Digits
# Ask the user for a number (example: 1234) and print the sum of its digits (1+2+3+4 = 10)

print("         question 3")
a=int(input("Enter a number to find sum of digits = "))
sum=0
total = 0 
while a>0:
    sum= a % 10    
    total += sum
    a //= 10 
print("Sum of digits is:", sum)

# Question 4
# Largest of Three Numbers
# Ask the user for three numbers and print the largest one

print("         question 4")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("The largest number is =", a)
elif b >= a and b >= c:
    print("The largest number is =", b)
else:
    print("The largest number is =", c)

# Question 5
# Count Consonants
# Ask the user for a word and count how many consonants it has (letters other than vowels)


print("         question 5")
a=input("Enter a word to count consonants = ")
c ="aeiouAEIOU"
count = 0
for i  in a:
    if i not in c:
        count +=1
print("The number of consonants in the word is:",count)