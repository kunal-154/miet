"""    LISTS: Denoted by square brackets[]
        can be store any type of datatypes
        In python lists are mutable
"""

name="Kunal"
age= "21"
course="Python"

list=["Kunal",21,"Python",68.5,True,False,None]
print(name,age,course)
print(list)



list1=[1,2,3,4,5]
list2=["kunal","aditya",21,21]
print(list1)
print(list2)
print(type(list1))
print(type(list2))

print(list1[1])
print(list2[3])
print(list1[-2])



list1[2]="Ducat"
list2[3]=34
print(list1)
print(list2)
list1[1:4]="My","Name"
print(list1)
