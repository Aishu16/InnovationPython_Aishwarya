#Task Three
'''
1. Create a list of the 10 elements of four different types of
Data Type like int, string, complex and float.
'''
List = [1, 1.0, 3+8j, 'consutadd', 5, 'abc', 0.2, 15, 4+8j, 'string']

'''
2. Create a list of size 5 and execute the slicing structure 
'''
x = [1, 2.0, 3+4j, 'consultadd', 20]
print(x[2:])
print(x[:4])
print(x[1:5:2])
print(x[::1])
print(x[::-1])

''' 
3. Write  a program to get the 
sum and multiply of all the items in a given list.
'''
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

def sum(list):
    x = 1
    for x in list:
        x += x
    return x

def mult(list):
    # Multiplying elements one by one
    x = 1
    for x in list:
        x *= x
    return x

print("Sum of number in list is: ", sum(lst))
print("Multiplication of number in list is: ", mult(lst))

''' 
4. Find the largest and smallest number from a given list.
'''
lst = []
num = int(input('How many numbers: '))

for i in range(num):
    numbers = int(input('Enter number: '))
    lst.append(numbers)

print(lst)
print("Smallest number in lst: ", min(lst))
print("Largest number in lst: ", max(lst))

''' 
5. Create a new list which contains the specified numbers 
after removing the even numbers from a predefined list. 
'''
lst = [10, 21, 4, 45, 66, 93]

for num in lst:
    if num % 2 != 0:
        print(num, end=" ")

''' 
6. Create a list of first and last 5 elements where the 
values are square of numbers between 1 and30 (both included).
'''
def square_val():
    a = list()
    for i in range(1, 31):
        a.append(i**2)
    print(a)

square_val()

'''
7.	Write a program to replace the last element
in a list with another list.
Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
Expected output: [1,3,5,7,9,2,4,6,8]

'''
x = [[1, 3, 5, 7, 9, 10],[2, 4, 6, 8]]
y = x[0][:-1] + x[1]
print(y)

'''
8. Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
Expected Result: {1:10,2:20,3:30,4:40}
'''
def Merge(d1, d2):
    return(d1.update(d2))

a={1:10,2:20}
b={3:30,4:40}
Merge(a, b)
print(a)

''' 
9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
Sample data (n=5)
Expected Output: {1:1,2:4,3:9,4:16,5:25}
'''
x = int(input("Input number: "))
a = dict()

for x in range(1, x+1):
    a[x] = x*x
print(a)

''' 
10. Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which contains
every number. Suppose the following input is supplied to the program:
34,67,55,33,12,98
The output should be:
[‘34’,’67’,’55’,’33’,’12’,’98’]
(‘34’,’67’,’55’,’33’,’12’,’98’]
'''

x = input("Enter number with comma: ")
list = x.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)

''' 
11.	Create a list of the 10 elements of four different types of 
Data Type like int, string, complex and float.
'''
List = [1, 1.0, 3+8j, 'consutadd', 5, 'abc', 0.2, 15, 4+8j, 'string']

''' 
12. Create a list of size 5 and execute the slicing structure 
'''

x = [1, 2.0, 3+4j, 'consultadd', 20]
print(x[2:])
print(x[:4])
print(x[1:5:2])
print(x[::1])
print(x[::-1])

''' 
13. Create a list of given structure and run 
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
●	Access list [1, 2, 3, 4]
●	Access list [600,  700]
●	Access list [100, 300, 500, 600, 800]
●	Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
●	Access list [10]
●	Access list [ ]

'''
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print(x[5][:4])
print(x[6:8])
print(x[::2])
print(x[::-1])
print(x[5][5][0:-4])
print(x[0:-10])

'''
14. 	Create a list of thousand number using range and xrange and 
see the difference between each other.
ans: Python 3, there is no xrange, but the range function 
behaves like xrange in Python 2
'''
a = range(1, 10000)

print("The return type of range() is : ")
print(type(a))

''' 
15. How Tuple is beneficial as compare to the list?
answer: Tuple can also be used as key in dictionary due to their hashable 
and immutable nature whereas Lists are not used as key in a dictionary 
because list can't handle __hash__() and have mutable nature.
'''

''' 
16. Write a program in Python to iterate through the list of numbers 
in the range of 1,100 and print the number which is divisible by 3 and 
a multiple of 2.
'''
x = []
for i in range(1101):
    if i % 3 == 0 and i % 2 == 0:
        x.append(i)
print(x)

'''
17. Write a program in Python to reverse a string and print 
only the vowel alphabet if exist in the string with their index.
'''
a = 'abcdef'
def reverse(x):
    x = x[::-1]
    return x
print(reverse(a))

for i, c in enumerate(reverse(a)):
    if (c == 'a' or c == 'A' or
        c == 'e' or c == 'E' or
        c == 'i' or c == 'I' or
        c == 'o' or c == 'O' or
        c == 'u' or c == 'U'):
        print("Index", i, 'Vowels', c)

''' 
18. Write a program in Python to iterate through the 
string “hello my name is abcde” 
and print the string which has even length of word.
'''
a = "hello my name is abcde"

def evenwords(a):
    a = a.split(' ')
    for word in a:
        if len(word) % 2 == 0:
            print(word)
evenwords(a)

''' 
19. Write a program in python to print the pair of numbers 
whose sum is equal to result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
'''

def printPairs(a, n, sum):
    for i in range(0, n):
        for j in range(i + 1, n):
            y = a[i] + a[j]
            if (y == sum):
                print(a[i], ", ", a[j], sep="")

a = [1,2,3,4,5,6,7,8,9,-1]
n = len(a)
sum = 8
printPairs(a, n, sum)

''' 
20. Write a program in Python to complete the following task:
●	Create two different list as in even_list and odd_list
●	Ask user to enter the number in the range of 1,50 and 
make sure if the entered number is even append it to the even_list and 
if the entered number is odd append it to the odd list.
●	Keep that in mind you can only add 5 items in each list
●	Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

'''
def addition(list):
    return sum(list)

def maximum(list):
   return max(list)

b = int(input("Enter size of list: "))
x = []
print("Enter the number between 1 to 50: ")

for a in range(b):
    y = int(input(""))
    x.append(y)

even_list = []
odd_list = []
def even_odd(x):
    for i in x:
        if i > 0 and i < 51:
            if i % 2 == 0 and len(even_list) < 5:
                even_list.append(i)

            elif i % 2 != 0 and len(odd_list) < 5:
                odd_list.append(i)
        else:
            print("Only number between 1 to 50 are acceptable")

    print("Even list: \n", even_list,"\n",
          "Addition of even list: ", addition(even_list),"\n",
          "Max number in even_list: ", maximum(even_list))
    print("Odd list: \n", odd_list, "\n",
          "Addition of odd list", addition(odd_list), "\n",
          "Max number in odd_list", maximum(odd_list))

even_odd(x)



'''
21. Write a program to find out the occurrence of a specific word 
from an alphanumeric statement. Example: 12abcbacbaba344ab  
Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
'''
def wordcount():
    x = input("Enter the string: ")
    y = input("Enter the words: ")
    a = x.split(" ")


    count = 0
    for i in a:
        if i in y:
            count += 1
    print("Words frequency is: ", count)

wordcount()

'''
22. Generate and print another tuple whose values are even numbers 
in the given tuple (1,2,3,4,5,6,7,8,9,10).

'''

def even_num_tuple(t):
    x = []
    for i in t:
        if i % 2 == 0:
            x.append(i)
    return tuple(x)

tp = (1,2,3,4,5,6,7,8,9,10)

print(even_num_tuple(tp))