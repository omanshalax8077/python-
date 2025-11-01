#Question1 
# Reverse a Number
# Ask the user for a number (e.g., 1234) and print its reverse (4321)

print("         question 1")
x=int(input("Enter the number = "))
x=str(x)
x=x[::-1]
print("The reverse of the number is = ",x)

# Question 2
# Fibonacci Series
# Ask the user for a number n and print the first n terms of the Fibonacci series.
# (Example for n=5 → 0 1 1 2 3

print("         question 2")
n=int(input("Enter the number = "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a , b = b, a + b
print("\n")

# Question 3
# Count Digits
# Ask the user for a number and count how many digits it has

print("         question 3")
a=int(input("Enter a number to count digits = "))
a=str(a)
print(len(a))

# Question 4
# Character Frequency
# Ask the user for a word and print how many times each character occurs.
# (Example: "banana" → b:1, a:3, n:2)

print("         question 4")
a=input("Enter a word to count a character occure = ")
x={}
for i in a:
    x[i]=x.get(i,0)+1
print(x)

# Question 5
# Prime Number Check
# Ask the user for a number and check if it’s prime or not

print("         question 5")
n = int(input("Enter a number to check if it's prime: "))
if n <= 1:
    print(n, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):   
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

