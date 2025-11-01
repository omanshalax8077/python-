# Question 1: List Sum
# Take 5 numbers from the user, store them in a list, and print the sum of all numbers.

a=[1,2,3,4,5]
print(a)
print(type(a))

print("------------------Question 1 -----------------")
x=[] # empty list 
for i in range(5): #ranga of list 
    y = int(input(f"Enter number {i+1} -  ")) # f string 
    x.append(y) # x ma y ko dal daya ha   
print("list are ",x)
print("sum of list is -",sum(x)) # sum is a function of python 
print("-------------------------------------------")

# Question 2: Find Maximum in List
# Take 7 numbers in a list and print the largest number without using max()

print("------------------Question 2 -----------------")
print("with  max() function ")
x=[]
for i in range (7):
    y=int (input(f"enter the number {i+1} - "))
    x.append(y)
print("list are", x )
print("largest number is = ", max(x))

print("without max() function ")
x=[]
for i in range (7):
    y=int (input(f"enter the number {i+1} - "))
    x.append(y)
print("list are", x )
large_number=x[0]
for p in x:
    if p>large_number :
        large_number=p
print("large number is ",large_number)
print("---------------------------------------------")

# Question 3: Reverse a List
# Ask the user for a list of numbers and print the reversed list.
print("--------------------Question 3----------------------")
n=[]
for i in range(5):
    y=int(input("Enter the number "))
    n.append(y)
print(n)
r=[]
for i in range (len(n)-1,-1,-1):
    r.append(n[i])
print(r)
print("--------------------------------------------")

# Question 4: Tuple Indexing
# Create a tuple ofprint the 2nd and 4th element
print("--------------------Question 4--------------")
a=('apple','king','python','java','forget')
print(a)
print("index : 1 ,element 2",a[1])
print("index : 3 ,element 4",a[3])
print("------------------------------------------")

# Question 5: Dictionary Word Meaning
# Create a dictionary with 3 English words and their meanings. Ask the user to enter a word and print its meaning

print("----------------Question 5-----------------")
d={
    "apple": ' is a fruit',
    "bike ":'is a transport',
    "keybord":"is a input divice "
}
w=input("Enter the word = ").lower()
if w in d :
     print ("value",d[w])
else:
    print("sorry... try again ... ")