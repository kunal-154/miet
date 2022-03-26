# Call by refrence in python
# passing mutable object (list)
# agr inside change krenge toh outside bhi effect pdega

def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("List inside function: ",list1)

#defining the list
list1=[10,30,40,50]

#calling the func.
change_list(list1)
print("List outside function: ",list1)





