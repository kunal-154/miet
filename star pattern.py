""" Star pattern:    'i' represent rows and 'j' represent columns
         j
     1 2 3 4 5
   1 *                i=1  j=1            j<=1
   2 * *              i=2  j=1,2          j<=2     j<=i #condition(if)
i  3 * * *            i=3  j=1,2,3        j<=3
   4 * * * *          i=4  j=1,2,3,4      j<=4
   5 * * * * *        i=5  j=1,2,3,4,5    j<=5
"""

i=1
while i<=5:  #for row
    j=1
    while j<=5:  # for coloumn
        if j<=i:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1    
    print()
    i=i+1
