""" Exception Handling """

#f5print(10/0)   # zero division error
#print("Programme will continue")


try:
    print(10/0)
except ZeroDivisionError as e:  # yha error likhni h jo aaygi or agr  ni pta ki konsi error h toh """Exception""" likh do error ki jgh
    print(e)

print("Programme will continue")    

try:
    print(10/0)
except Exception as e:  
    print(e)


try:
    x=10
    print(y) # name error
except NameError as e:
    print("Please print valid variable name")


try:
    print(10/2)
    x=10
    print(y)
except ZeroDivisionError:
    print("Number is not Divide by zero")
except NameError:
    print("Please provide valid variable name")

else:
    print("My programme will continue")    

