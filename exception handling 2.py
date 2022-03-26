try:
    fileptr=open("today.txt","r")
except IOError:
    print("File not found")
else:  #  agr koi error ni h toh else case chlega
    print("The file opened successfully")
    fileptr.close()
  

try:
    a=10/0
except(ArithmeticError,IOError):
    print("Arithmetic Exception")
else:
    print(a)


try:
    a=10/2
    file=open("abc.txt","r")
    print(file.read())
except(ArithmeticError,IOError) as e:
    print(e)
else:
    print("Successfully Done")
s
