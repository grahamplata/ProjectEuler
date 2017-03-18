#!C:\Python33\python.exe

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from math import floor

def factor(value):
    #create list of values
    numbers = []

    #check if the input is prime
    if value != 2 and value % 2 == 0:
        numbers.append(2)

    for i in xrange(3, int(floor(value ** 0.5)), 2):
        if value % i == 0:
            if len(factor(i)) == 0:
                numbers.append(i)
    return numbers

print factor(600851475143)
