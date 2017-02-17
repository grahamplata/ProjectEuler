#Set upper total limit
limit = 4000000
#Even Fibonacci number sum
total = 0
#Tuple containing current and next value
a, b = 1, 1

#Current is checked against the limit
while a <= limit:
    #Add even values to total
    if a % 2 == 0:
        total += a
    #Fibonacci sequence formula
    a, b = b, a + b
print total

