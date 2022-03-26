l1=[1,2,3,4,5,6,7,8]
for i in l1:
    print(i)


l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5,6]
print(l1==l2)    #True


list1=[1,8,7,98,45,26]
list1.remove(98)     # remove(list to be removed, not index)
print(list1)


l2=[34,56,78]
print(l1+l2)
print(l2*3)
print(9 in l1)

list2=["Kunal","Adi",23,34.5]
for i in list2:          # print the list without brackets and commas (iteartion)
    print(i,end=" ")
print(len(list2))
