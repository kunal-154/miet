""" String can be represented by three types : >single quotes  (Single line stirng) 
                                               >Double quotes  (Single line string)
                                               >triple quotes  (Multi line string)
"""

print("Hello Python")

print('Hello python')

print("""Hello python
                                welcome to noida""")





print(type('A'))



#String Slicing/Indexing

"""Forward Indexing   (here colon will be used)"""

name="Python"   #indexing start with 0 1 2 3 
print(name[1])   # y
print(name[1:4])    #last number exclusive(4)
print(name[:])    #will show full string
print(name[1:7:2])   #gap of 2    (By default gap of 1)
print(name[::-1])    #Reverse the string


"""Backward Indexing
   indexing starts with -1 from right to left   (-4 -3 -2 -1)
"""


print("Python")
print(name[-1])  # n
print(name[-2])   # o
print(name[-1:-4])   #no output because deafult gap is 1
print(name[-1:-4:-1])    #now it will print (noh)
print(name[-4:-1])   #output(tho)


