""" calculator via function"""

def calculate():
    print("\t\t\tSimple Claculator Via Function.")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    num1=int(input("Enter first numnber:"))
    num2=int(input("Enter second number:"))

    choice=int(input("Enter your choice: "))
    if (choice==1):
        print("Sum is: ",(num1+num2))
    elif (choice==2):
        print("Subtraction is:",(num1-num2))
    elif (choice==3):
        print("Multiplication is:",(num1*num2))
    elif (choice==4):
        print("Division is:",(num1/num2))
    elif (choice==5):
        exit()

    chr1=input("Do you want to continue y/n : ")
    if (chr1=='y'):
        calculate()
    else:
        print("Thankyou")        
calculate()

