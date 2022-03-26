list=["kunal","adi","23","453","34.5","ducat","kunal","453","hello","adi"]
print("The original list with duplicate irems is: "+ str(list))
list2=[]
for i in list:  
    if i not in list2:
        list2.append(i)
        print("The list after removing duplicate items is: "+ str(list2))
print(list2)        
