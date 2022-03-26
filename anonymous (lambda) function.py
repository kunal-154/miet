"""
    Anonymous Function: (function without name)
    defined by lambda keyword  (use only one time)
    generally we use lambda function with high order function or in event handling

"""

def sqr(a):
    return a*a
l=[1,2,3,4,5,6,7]
print(list(map(sqr,l)))  # using map function


# Using lambda keyword or anonymous function
print(list(map(lambda x:x*x*x,l)))   # lambda (without using any function and reduce code in one line)  (known as inline function in c++)


x=lambda a:a+a
print(x(5))  # print 10


x=lambda a,b:a+b
print(x(100,200))

