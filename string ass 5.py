a=input("Enter first string: ")
b=input("Enter second string: ")

print(a,b,sep=" ")
x=a[0:2]
a=a.replace(a[0:2],b[0:2])
b=b.replace(b[0:2],x)
print("Your first string has become: ",a)
print("your second string has become: ",b)
