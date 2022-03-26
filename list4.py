l1=[1,2,3,4,5,6,["amit","ajay"]]
l2=l1    # Refrence copy
print(l2)
l2[5]="Sudhanshu"    # isme change ho jayga (original mai)
print(l1) 
print(id(l1))   # Address same honge dono ke
print(id(l2))

#Copy method

l3=[1,2,3,4,5,6,["Kunal","Utkarsh"]]

l4=l3.copy()   # Shallow copy
print(l4)
l3[4]="Aditya"    # isme koi change ni hoga(original mai)
print(id(l3))     # address alg honge dono ke
print(id(l4)) 

l4[4]="Aditya"   # ab change ho jayga 
print(l4)        # original mai change ni hoga, copy vali list mai ho jayga

