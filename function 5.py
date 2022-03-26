# Default arguments

def printme(name,age=20):
    print("My name is",name, "And my age is",age)
printme("Kunal")  #age ki default value le lega(20)
printme("Kunal",21)   # age ki default valu ni lega qki humne yha dedi(21)


def hello(name="Kunal",age=20):
    print("My name is",name, "And my age is",age)
hello()  # by default le lega dono ki value



# Variable length arguments

def printme(*names):    #many names can be passed using abstrick*
    print("Type of passed argument is",type(names))
    print("printing the passed arguments....")
    for name in names:
        print(name)
printme("Kunal","Adi","Chirag","Utkarsh","Srthk","Hello","Bye")        


#keyword arguments(**Kwargs)   (isme baad mai keyword defines kr dete h)
