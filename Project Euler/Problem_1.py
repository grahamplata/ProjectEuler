#set variables
total_sum = 0

#Run loop 1000 times with index
for i in range(1000):
    #Check to see if it is evenly divisible by 3 or 5
    if (i % 3 == 0 or i % 5 == 0):
        #sum totals
        total_sum = total_sum + i
#print answer
print total_sum  