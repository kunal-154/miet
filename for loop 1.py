# For loop using range() function
""" range(start,stop,step size)
    range() expected atleast one argument
"""

for i in range(0):  #"""no output"""
    print("Hello")


for i in range(10):  #print 10 times hello
    print("Hello")


for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
    print(i)

for i in range(3,10): # 3 4 5 6 7 8 9   (3,10-1)
    print(i)

for i in range(1,10,2):  # 1 3 5 7 9 (skip by 2)
    print(i)


for i in range(1,10):   # 1 2 3 4 5 6 7 8 9
    print(i)
    i = i+1  # no effect on iteration


for i in range(10,1,-1): # 10 9 8 7 6 5 4 3 2 (reverse the string) 
    print(i)


for i in range("Kunal","Gupta"):  # string is not allowed in range()
    print(i) 
