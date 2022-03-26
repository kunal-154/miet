l1=[]  #Empty list
n=int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    l1.append(input("Enter the item:"))
print("Printing list item: ")
for i in l1:                                # add the value at the end
    print(i,end=" ")     



list1=[1,2,3,4,5]
list2=[2,3,4,5,6,7]
print(max(list1))   # max value: 5
print(min(list2))   # min value: 2



l3=[1,2,3,4,5,6,7]
print(l3.count(7))   # 1
l3.extend([45,34,655,34,76])    # add all the items at the end of the list
l3.append([23,45,67])   # add single element at the end (consider all the elements as a single element)
print(l3)



l4=[1,2,3,4,5,6]
print(l4.index(5))   #tells the index of the item(5=4)
l4.insert(2,"Ducat")     #contains 2 arguments:- 1) index at which you want to insert    2)value you want to insert
print(l4)

print(l4.pop())    # remove last value and return that value again and print that value (6)


l5=[23,86,45,67,34,25,86,55]     # sorted hamara list ka method ni h yeh toh alg func. h jo hum list pr bhi use kr skte h  
print(sorted(l5))                # sort the list
print(l5.sort())      #none (because sort function is deplicated)
print(l5.reverse())   #none (" " " ")

l5.sort()     # uppr ni chla tha ab chl gya qki pehle sort hoga fir print hoga
print(l5)     # ek sth sort or print ni ho skta

l5.reverse()   # same as sort function
print(l5)

 
