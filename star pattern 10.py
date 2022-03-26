i=1
def func():
    for i in range(1,6):
        j=1
        for j in range(1,6):
            if j<=i:
                print(" *",end="")
            else:
                print(" ",end=" ")
        print()
func()               
