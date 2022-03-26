"""String assignment  (we cannot edit in the existing string)
        Stirngs are immutable
"""



name="Ducat"
#name[1]='M'   #TypeError: 'str' does not support item assignment
print(name)

#del name[1]  #TypeError: 'str' does not support item assignment
print(name)

print(id(name))
name='Java'
print(name)
print(id(name))



""" String Operators"""

print("Hello"+"Python")  #Concatinate the string
print("Hello \n"*4)

name="Python"
print('P' in name)
print('P' not in name)

print("C:\\Users\\kunal\\OneDrive\\Documents\\dbms")     #double slash lgake single slash show krega
print(r"C:\Users\kunal\OneDrive\Documents\dbms")         #(raw string) double slash lgane ki need ni h
print(R"C:\Users\kunal\OneDrive\Documents\dbms")
