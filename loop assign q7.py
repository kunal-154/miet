n=int(input("Enter a number:"))
sum=0
i=1
while i<=n:
    if i%2!=0:
        print(i)
    sum=sum+i
    i=i+1
print(sum)
