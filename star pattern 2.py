""" Pattern
  1 2 3 4 5
1         *       i=1   j=5
2       * *       i=2   j=4,5          j>=6-i # if condition
3     * * *       i=3   j=3,4,5
4   * * * *       i=4   j=2,3,4,5
5 * * * * *       i=5   j=1,2,3,4,5
"""

i=1
while i<=5:
    j=1
    while j<=5:
        if (j>=6-i):
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    print()
    i=i+1
