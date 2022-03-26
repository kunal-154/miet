d1={"Name":"Kunal","Age":21,"Course":"Python"}
print("\t\t\tStudents Details")
for k,v in d1.items():    # print both keys and values
    print(k,":",v)

print("\t\t\tOnly print keys")
for k in d1.keys():     # print keys only
    print(k)

print("\t\t\tOnly print values")
for v in d1.values():    #print values only
    print(v)



employee={"Name":"Kunal","Age":21,"Salary":25000,"Comapny":"Google"}
print()  #next line
print(type(employee))    #class<dict>
print("\t\t\tEmploye Details")
for k,v in employee.items():
    print(k,"=",v)



d1=dict(((1,2),(2,3),(4,5)))
print()
print(d1)

