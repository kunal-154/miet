""" Pattern:

  1 2 3 4 5
1         *
2       * *
3     * * *
4   * * * *
5 * * * * *
6   * * * *
7     * * *
8       * *
9         *

"""

i=1
def func():
    for i in range(1,5):
        j=1
        for j in range(1,6):
            if (j>=6-i):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
func()        

def func1():
    for i in range(1,6):
        j=1
        for j in range(1,6):
            if (j>=i):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
func1()    
