
# Take 6 numbers from the user.
# Store even numbers in one list and odd numbers in another.
# Finally, print both lists.

print("------------------Question 1--------------")
e=[]
o=[]
for i in range(6):
    x=int(input("Enter a number : "))
    if x%2==0:
        e.append(x)
    else:
        o.append(x)
print("lis of even number =",e)
print("list for odd number =",o)
print("-----------------------------------------")

# Ask the user for a list of numbers and find the second largest number 
print("---------------------Question 2------------------")
number=[]
for i in range(5):
    x=int(input("Enter a number : "))
    number.append(x)
print("given list ",number)
number.sort()
print("sorted list or increaseing list = ", number )
number.sort(reverse=True)
print("reverse shorded list or Descending list ", number )
print("second largest number = ",number[1])
print("----------------------------------------")

# Take 5 numbers from the user (some may be repeated).
# Print a list of unique elements only (no duplicates).

print("------------------Question 3--------------------")
numbers = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)
print("given list = ",numbers)
u=[]
for i in numbers:
    if i not in u:
        u.append(i)
print("unique list = ",u)
print("--------------------------------------------")

# Ask the user for a sentence.
# Create a dictionary where each word is a key and its length is the value.

print("-----------------------Question 4 ---------------------")
sentence=input("Enter the sentene = ")
print("The sentence is = ",sentence)
sen =sentence.split()#list of split sentence 
print(sen)
siz={}
for i in sen: 
    siz[i]=len(i) 
print(siz)
print("---------------------------------------------")

# Create a tuple of 5 numbers. Print:
# The sum of all numbers
# The maximum and minimum number
# The average of the numbers

print("-----------------Question 5 ----------------")
x=(1,2,3,4,5)
s=sum(x)
m=max(x)
mi=min(x)
av=s/5
print("Sum of all numbers ",s,""," \nMaximum number ",m," \nMinimum number ",mi
      ,"\nThe average of the numbers",av)
print("--------------------------------------------")

# Create two dictionaries from user input and merge them into one
print("----------------Question 6 ---------------------")
x={
    "omansh": 92,
    "anshu": 95,
    'deepika': 98
}
print("first dictionary = ", x)
y={
     "gagan": 65,
     'mahi': 56,
     "arpit": 85
}
print("second dictionary = ",y )
x.update(y)
print("Merge Two Dictionaries",x)
marge=x|y
print("Merge Two Dictionaries",marge)
print("-------------------------------------------")

# Product of List Elements
# Take 5 numbers from the user and find the product (multiplication) of all numbers in the list.
print("---------------------Question 7 ---------------------")
number=[]
for i in range (5):
    x=int(input(f"Enter the {1+i} number : "))
    number.append(x)
print("Given list is = ", number )
pr=1
for i in number :
    pr*=i
    print(pr ) 
print("product of element = " , pr)
print("----------------------------------------------")

# Create a dictionary with 3–5 words and their meanings.
# Ask the user to enter a word, and print its meaning if it exists, otherwise print
print("---------------------Question 8---------------------")
d={
    "classmate": 'notebook',
    "lenovo" : "laptop and computer ",
    "anshu" : "pagal ",
    "doms": "pan",
    "titan": 'watch'   
}
k=d.keys()
# print(k)
x=input("Enter the word find a meaning = ").lower()
if x in d:
    print(f"meaning of {x} is {d[x]}")
else:
    print(" not found ",k)
print("---------------------------------------")

# Create a dictionary with 3 students’ names as keys and their marks as values.
# Find and print the average marks of all students
print("----------------------Question 9-----------------")
d={
    'omansh': 56,
    'gagan':58,
    "dapanshu":52
}
print(d)
k=d.keys()
print(" Name of student = ",list(k))
v=d.values()
print(" Number of student =",list(v))
sum=sum(v)
print("sum of number = ",sum)
a=sum/3
print("avarage of marks = ",float(a))
print("-------------------------------------")

# Take two lists from the user (each with 5 numbers).
# Find and print only the numbers that are common in both lists.
print("-----------------Question 10-----------------")
f=[] 
for i in range(5):  
    x=int(input(f"Enter the {1+i} number = "))
    f.append(x)
print("first list =",f)
s=[]
for i in range(5):
    x=int(input(f"Enter the {1+i} number = "))
    s.append(x)
print("second list =",s)
co=[]
for i in f:
    # print(i)
    # print("for")
    if i in s and i not in co:
        # print(i)
        # print("in")
    # if i not in s:
    #     print(i)
        # print("not")
        # if i not in co:
        #  print(i)
        co.append(i)
print("comman element are = ",co)

# Ask the user for a sentence.
# Count how many times each word appears.
print("---------------Question 11------------")
sen=input('Enter the sentence = ').lower()
los=sen.split()
print(los)
count={}
for i in los:
    # print(i)
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("Count how many times each word appears = ",count)

