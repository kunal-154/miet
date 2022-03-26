""" Pattern:

  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

1 * * * * * * * * * * * * * * *  
2 * * * * * * *   * * * * * * * 
3 * * * * * *       * * * * * * 
4 * * * * *           * * * * * 
5 * * * *               * * * *
6 * * *                   * * *
7 * *                       * *
8 *                           *

"""

def func():
    i=1
    for i in range(1,8):
        j=1
        for j in range(1,9):
            if (j<=9-i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
func()

def func1():
    
    i=1
    for i in range(1,9):
        j=1
        for j in range(1,9):
            if (j>=i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
func1()
#print(func(),func1(),end="")
