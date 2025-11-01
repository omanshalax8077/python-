# Question 1
# Print Even Numbers
# Print all even numbers from 1 to 20 using a loop.

print("         question 1")
for i in range(1,21):
    if i%2==0:
     print(i,end=" ")
print("\nAll even numbers from 1 to 20")

# Question 2
# Count Words
# Ask the user for a sentence and count how many words it has

print("         question 2")
sen=input("Enter a sentence = ")
count=1
for i in sen:
   if i==" ":
     count+=1
print("The number of words in the sentence is = ",count)

# Question 3
# Multiplication Table (Range)
# Ask the user for a number and print its multiplication table up to 20.

print("         question 3")
n= int(input("Enter a number to print multiplication table = "))
for i in range(1,21):
    print(n,"X",i,"=",n*i)

# Question 4
# Sum of Even Digits
# Ask the user for a number (example: 123456) and print
#  the sum of its even digits (2+4+6 = 12)
   
print("         question 4")
a = input("Enter the number to find sum of even digits = ")
sum = 0
for i in a:
    b = int(i)          # har digit ko integer banao
    if b % 2 == 0:      # check karo even hai ya nahi
        sum += b
print("The sum of even digits is =", sum)


#Quection 5
# Reverse Each Word
# Ask the user for a sentence and print each word reversed.

print("         question 5")
a=input("Enter a sentence to reverse each word = ")
b=a.split()
c=[w[::-1] for w in b]
print("  ".join(c))

