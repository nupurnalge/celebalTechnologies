'''Q1)The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
''' You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character '(X,c)' with  in the string.'''
# importing the required module
from itertools import groupby

# using if __name__ variable
if __name__ == "__main__":
    
    # using for loop to iterate through the string
    for k, c in groupby(input()):

        #printing the output
        print("(%d, %d)" % (len(list(c)), int(k)), end=' ')

''' Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.'''    

def minion_game(string):
    # your code goes here
    n = len(string)
    comb = ((n)*(n+1))/2
    count_k = 0
    count_s = 0
    count_k = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_s = comb - count_k
    
    if count_s == count_k:
        print("Draw")
    elif count_s > count_k:
        print("Stuart", int(count_s) )
    else:
        print("Kevin", int(count_k))

if __name__ == '__main__':
    s = input()
    minion_game(s)
''' An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.'''

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:            #Here we are checking if the year is normal year
        leap = True
        if year%100 == 0:        #Here we are checking if the year is a century year      
            if year%400 == 0:
                leap = True
            else:
                leap = False
        
                
    

                
    

    return leap

year = int(input())
print(is_leap(year))

'''Iterables and iterators problem'''
from itertools import combinations, groupby

# Read the input
count, letters, to_select = int(input()), input().split(), int(input())

# sort the letters so all a's are on left side
letters = sorted(letters)

# Find all possible combinations of to_select
combinations_of_letters = list(combinations(letters, to_select))

# find all which contain
contain = len([c for c in combinations_of_letters if 'a' in c])

# Print Results
print(contain / len(combinations_of_letters))

''' Python Tuples problem'''
if __name__ == '__main__':

    n = int(input())

    Tuple1 = map(int, input().split())

    t = tuple(Tuple1)

    print(hash(t))

''' The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal '''
if __name__ == '__main__':

    n = int(input())

    student_marks = {}

    for _ in range(n):

        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores

    query_name = input()

    l1 = list(student_marks[query_name]) 

    addition = sum(l1)

    result = addition/len(l1)

    print('%.2f'% result)


''' Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary '''

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    

