try:
    fileptr=open("abc.txt","r")
    try:
        fileptr.write("Hi, I am good")
    finally:  # error ho program mai ya na ho finally hamehsa chlega
        fileptr.close()
        print("File Closed")
except:
    print("Error")
        

""" Raise exception """

try:
    age=int(input("Enter your age: "))
    if (age>18):
        raise ValueError
    else:
        print("The age is valid")
except ValueError:
    print("The age is not valid")
