print("Empty Dictionary")
d1={}
print(d1)

d1[0]="Ajay"
d1[1]="Amit"
d1[2]="Sachin"
d1[3]="Vijay"
d1[4]="Arman"

print(d1)  #apne aap dictionary bna dega

d1["Emp Ages"]=34,45,54,22,31

print(d1)
for k,v in d1.items():
    print(k,"=",v)


d1={1:"Kunal"}
print(d1)

d1[1]="Utkarsh"

print(d1)

employee={"Name":"Kunal","Age":21,"Salary":25000,"Comapny":"Google"}
for i in employee:   # keys and values dono print kr dega bina (.items) lgaye
    print(i,":",employee[i])

print()
print(employee.clear())  #none  (puri dictionary clear kr dega)

e1=employee.copy()
print(e1)
