def func():
    i=1
    while i<=8:
        j=1
        while j<=8:
            if (j<=9-i):
                print("*",end="")
            else:
                print(" ",end="")
            j=j+1
        print()
        i=i+1
func()

def func1():
    i=1
    while i<=9:
        j=1
        while j<=8:
            if (j>=i):
                print("*",end="")
            else:
                print(" ",end="")
            j=j+1
        print()
        i=i+1
func1()

