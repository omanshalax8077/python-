# Question 1: Square of Each Number
# Take 5 numbers from the user, store them in a list, and print a new list containing the square of each number.

# print("----------------------Question 1------------------")
# l=[]
# x=(int(input("Enter the number of element of list you take square - ")))
# for i in range(x):
#     y=int(input(f"Enter the {i+1} number "))
#     l.append(y)
# print("List of whoes number will be square - ",l)
# p=[]
# for i in l:
#     p.append(i**2)
# print("Square list are - ",p)
# print("------------------------------------------------------")

# Question 2: Count Occurrences
# Ask the user for a sentence and count how many times each word appears.

# print("----------------------Question 2------------------")
# sen=input("Enter the senternce - ")
# wo=sen.split()
# print(wo)

# wc={}

# for i in wo:
#     i = i.lower()
#     if i in wc :
#         wc[i]+=1
#     else:
#         wc[i]=1
# print(wc)

# for key,value in wc.items():
#     print(key,"-",value)  
# print("------------------------------------------------")

# Question 3: Tuple Slicing
# Create a tuple with 6 numbers and print:
# The first three elements
# The last two elements
# The tuple in reverse orde

# print("----------------------Question 3------------------")
# l=[]
# x=(int(input("Enter the number of element of list you take Tuple Slicing - ")))
# for i in range(x):
#     y=int(input(f"Enter the {i+1} number "))
#     l.append(y) 
# print(type(l))
# print(l)
# t=tuple(l)
# print(type(t))
# print(t)
# print("The first three elements")
# print(t[0:3])
# print("The last two elements")
# print(t[4:6])
# print("The tuple in reverse orde")
# print(t[::-1])
# print("-------------------------------------------")

# Question 4: Merge Two Lists
# Take two lists from the user and merge them into a single list without using the + operator

# print("----------------------Question 4------------------")
# print("Enter the first list element ")
# f=[]
# for i in range(3):
#     y=int(input(f"Enter {i+1} element  = "))
#     f.append(y)
# print("Enter the second list element ")
# s=[]
# for i in range(3):
#     x=int(input(f"Enter {i+1} element  = "))
#     s.append(x)
# print(f)
# print(s)
# print("merge them into a single list with using the + operator")
# print(f+s)
# print("merge them into a single list witout using the + operator")
# m=[]
# for i in (f):
#     m.append(i)
# for i in (s):
#     m.append(i)
# print(m)
# print("--------------------------------------------")

# Question 5: Student Marks Dictionary
# Create a dictionary that stores 3 students’ names as keys and their marks as values.
# Then print:
# All student names
# All marks
# The student with the highest marks
print("---------------------Question 5 -----------------")
sudent={
    "gagan": 80,
    'omansh':50,
    "deepanshu":90  
}
print(list(sudent.keys()))
print(list(sudent.values()))
max_number=max(sudent,key=sudent.get)
print(max_number)
print("------------------------------------------------")

