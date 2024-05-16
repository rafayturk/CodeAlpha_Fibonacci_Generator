x=0     # set x equals 0
y=1     # set y equals 1
limit=int(input('enter limit :'))   # user will enter the limit of numbers in fibonacci series
fib_seq=[]      # initially fibonacci series list is empty
for i in range(limit): # loop according to limit entered by user
    fib_seq.append(x)   # put the value of x in the list    
    temp=x+y        # sum of x & y stored in temp variable
    x=y     # assign the value of y in x
    y=temp     # store temp value in y

print(fib_seq) 