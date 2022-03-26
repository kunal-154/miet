"""
              scope of variables:

      1) Global variable   2) Local variable
"""
x=10    # Global scope
def func():
    print(x)
func()    


def fun():
    x=20    #local scope
    print(x)
fun()


def func1():
    x=30
    print(x)
func1()
print(x)  # error becoz it is locally declared not globally




def calculate(*num):   #variable function
    sum=0
    for num1 in num:
        sum=sum+num1
    print("sum is:",sum)
sum=0
calculate(10,20,30)
print("value of the sum outside the function:",sum)

