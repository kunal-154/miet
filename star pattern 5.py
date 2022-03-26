""" Pattern:
  1 2 3 4 5
1 * * * * *
2 * * * * *
3 * * * * *
4 * * * * *
5 * * * * *
"""
i=1
while(i<=5):
    j=1
    while(j<=5):
        if(j<=5):
            print(" *",end="")
        else:
            print(" ",end="")
        j=j+1
    print()
    i=i+1



a=int(input("Enter the number of rows: "))
b=int(input("Enter the number of columns: "))
i=1
for i in range(1,a):
    j=1
    for j in range(1,b):
        if j<=a:
            print(" * ",end="")
        else:
            print(" ",end="")
        j=j+1
    print()
    i=i+1
    
