""" This is called high order function   """  #(Map and Filter)


def sqr(x):
    return x*x

def cube(a):
    return a*a*a

l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(sqr,l)))  # sbka square krke dedega ek line mai (reduce the code in single line)

print(list(map(cube,l)))  # sbka cube kr dega (reduce the code)


print(list(map(sqr,range(1,100))))  # 1 se 100 tk sbke square bta dega



def check(x):   # filter function
    if(x%2==0):
        return True
    else:
        return False

print(check(10))    
print(check(9))

print(list(filter(check,l)))  # Filter func. returns the value which is true only  (print even numbers)

print(list(map(check,l)))  # map function print false and true (all values)
