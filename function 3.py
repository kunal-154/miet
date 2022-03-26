""" Arguments in Function
"""
def user(name):
    print("Hello",name)   #hello kunal
user("Kunal")    




def details(name,password):
    print("My name is ",name)
    print("Your password is",password)
details("Kunal","12345")    



def sum(a,b):
    return a+b
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(sum(num1,num2))


def sum():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    return num1+num2
print(sum())
