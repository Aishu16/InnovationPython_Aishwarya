#Task Four: FUNCTIONS

'''
1. Write a program to reverse a string.
Sample data: “1234abcd”
Expected Output: “dcba4321”
'''

def reverse():
    x = input("Enter a string: ")
    y = list(x)
    print("Reverse string is: ", x[::-1])

reverse()

''' 
2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12

'''
def counts():
    x = input("Enter a String: ")
    Upper = 0
    Lower = 0
    for i in x:
        if i.isupper():
            Upper += 1
        elif i.islower():
            Lower += 1
        else:
            pass
    print("Sting: ", x)
    print("No. of Upper case characters : ", Upper)
    print("No. of Upper case characters : ", Lower)

counts()

'''
3. Create a function that takes a list and returns a new list
with unique elements of the first list.
'''
def unique(x):
    y = []

    for i in x:
        if i not in y:
            y.append(i)
    print("Unique elements in list: ", y)

x = [1,2,3,3,4,5,6,7,7,8,9,9]
unique(x)

'''
4. Write a program that accepts a hyphen-separated sequence of words
as input and prints the words in a hyphen-separated sequence after
sorting them alphabetically.
'''

def sperate_sort():
    x = input("Enter a hyphen-separated sequence of words: ")
    y = x.split('-')
    y.sort()
    print("The hyphen-separated sequence after sorting: ", '-'.join(y))

sperate_sort()

