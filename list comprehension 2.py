""" Nested condition in list comprehensions """

print([i for i in range(100) if(i%2==0) if(i%5==0)])  # for ke aage vala variable h or pehle vala expression (dono same hote h)

print([ x+1 if (x%2==0) else x**2 for x in [1,2,3,4,5,6,7,8]])

list=[[1,2,3],[4,5,6],[3,4]]
print([res**2 for x in list for res in x])  # for list


