"""  High order function  """


l1=["Virat","Sachin","Rohit"]
print(len(l1))   # length of the list

for i in l1:
    print(len(i))  # length of the characters (virat, sachin, rohit)


m=map(len,l1) # high order function,  hume type cast krna pdega pehle list tuple kisi mai bhi  
print(list(m))

print(list(map(len,l1))) # high order function (used for reducing the code)    


print(max(l1)) # print virat (bcoz value of v is greater)	

print(list(map(max,l1)))  # hr character mai sbse bdi value print krega (t, n, t)

print(list(map(str.upper,l1)))  # capital the whole value (upper func is for string not for list)

print(list(map(str.capitalize,l1)))  # first letter capital
