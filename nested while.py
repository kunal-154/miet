#Nested while loop with while statement

i=1
while i<=3:
    j=1
    while j<=3:
        if(i==2 and j==2):
                break
        print(i," ",j)
        j=j+1
    i=i+1    
