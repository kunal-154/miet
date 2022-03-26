"""Nested for loop
    for i in range()
        for j in range()
"""

for i in range(1,4):      # 11 12 13 21 22 23 31 32 33
    for j in range(1,4):
        print(i," ",j,end="")





for i in range(1,4):       # 11 12 13 21 31 32 33
    for j in range(1,4):
        if i==2 and j==2:
            break
        print(i,"",j, end=" ")
       

        
