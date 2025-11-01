# Question 1: 
# Palindrome Number
# Ask the user for a number and check if it is a palindrome
#  (same forward and backward, e.g., 121, 1331)

print("-----------Question 1 ---------")
x = int (input("Enter the number to check a number is palidrome = "))
p=x
a=0
for i in range (1,x+1):
 while x>0:
  b=x%10 # input =123 ,output = 3
  a=a*10+b 
  x=x//10 # input =123 ,output = 12 
  # print(b) 
  # print(x)
  print(a)
if a==p:
   print("YES The number number is palidrome")
else:
   print("NO The number number is palidrome")
print("------------------------------------")

# Question 2:
# Count Digits and Alphabets
# Take a string input and count how many digits and how many alphabets it has

print("-----------Question 2 ---------")
s=input("Enter tha santence = ")
A=0
D=0
for ch in s :
  if ch.isalpha():
    A+=1
  elif ch.isdigit():
    D+=1
print("Number of alphabets is = ",A)
print("Number of digite is = ",D)
print("------------------------------------")

# Question 3: 
# Perfect Square Check
# Take a number from the user and check if it is a perfect square or not

print("-----------Question 3---------")
x=int(input("Enter the number to chack tha prefect root = "))
root=int(x**0.5) 
if root*root==x :
  print("Perfect square of ",root )
else:
  print("its not a Perfect square ")
print("-----------------------------------")

# Question 4:
# Multiplication Table (Reverse Order)
# Take a number from the user and print its multiplication table in reverse.
# (Example: n=5 → 5×10, 5×9 … till 5×1)

print("-----------Question 4---------")
t=int(input("Enter the number of reverse oder of table \n the number is = "))
for i in range (10,0,-1):
 print(t,"X",i,"=",t*i)
print("-----------------------------------")

# Question 5: 
# Number Guessing (Simple)
# Ask the user to guess a number between 1 and 10.
# If the guess is correct, print "Correct!", else print "Try again!".

print("-----------Question 5---------")

for i in range(2):
    x=int(input("Enter tha number between 1 and 20 = "))
    if(x==12):
      print("Guess is correct... thankyou..... ")
      break
    else:
      print(" Something is worrg.... plz.. Try again!")
print("-----------------------------------")