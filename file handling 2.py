file=open("abc.txt","w")
a=file.write("Some candidates are not regukar in the class\n")
b=file.write("dedication is required to get something")
print(a,b)
print(file.write("a"))
file.close()


file=open("abc.txt","r+")
print(file.read())   # r+ le baad read() zrur use krna h
file.write("Python Programming")
file.close()


file=open("abc.txt","a+")
file.write("\nHi I am good")
file.flush()
file.seek(0)
print(file.read())
file.close()


with open("aa.txt","w") as file:   # if you do not use close() then we can use with(). It will consider automatic close()
   file.write("Bye")
print("Done...")
print(file.mode())
print(file.name())
file.close()
