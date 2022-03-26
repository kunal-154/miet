print("Enter a string:")
text=input()
print("Enter a character")
char=input()
textlen=len(text)
sum=0
for i in range(textlen):
    if char==text[i]:
        sum=sum+1
print("\nOccurance of the given character is:")
print(sum)
