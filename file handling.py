#file=open('abc.txt','r')
#print(file.read())

file=open("Today.txt","w")   # agr pehle se koi file hogi today naam ki toh vo open kr dega or agr ni hogi toh apne aap nyi create kr dega
a=file.write("Hello Welcome to ducat")  # yeh today file mai write kia h humne
print(a)   # 22
c=file.write("Monty python's flying circus")
print(c)
b=file.flush()
print(b)
#file.close()
file.tell()



file=open("Today.txt","r")  # by default bhi r hi hota h (read mode)
print(file.read())   # file mai kya likha h vo dikha dega  (default value -1 hoti h read ki)
print(file.tell())   # tells the current position of the pointer
file.seek(0)         # change the position of the cursor and take it to position 0
print(file.read(20)) # ab yeh 20 tk bhi print krega, pehle ni kr rha tha seek lgane se, qki pointer 50 pr tha or ab 0 pr h
file.close()




file=open("Today.txt","r")
text=file.read()
print("Characters in the text : ",len(text))

s="India is a country"
words=s.split()  #returns list of sub string (return total no. of words)
print(len(words))


file=open("Today.txt","r")
text=file.read()
words=text.split()
lines=text.split("\n")
print("Total no. of character : ",len(text))
print("Total no. of words : ",len(words))
print("Total no. of lines : ",len(lines))

file=open(input("Enter the path of the file : "),"r")
text=file.read()
words=text.split()
lines=text.split("\n")
print("Total no. of character : ",len(text))
print("Total no. of words : ",len(words))
print("Total no. of lines : ",len(lines))
file.close()
