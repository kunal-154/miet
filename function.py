""" Function: are of two types  -) Built-in functions    -) User defined
     Defind as organized block of reusable code, which can be called whenever required
     denoted by round braces()
     def keyword is used to create a function
     #syntax to create function:-
     def <function_value>():
         code to be executed
         return value
"""     

def func(): 
    print("Hello my name is kunal")    #no output

func()    # hello my name is kunal (bcoz humne func call kia)
func()    # jitni br likhenge utni br print hoga



def sum(x,y):
    print(x+y)
#sum()   #error
sum(5,6) #11  (jaisa func define kia h vaise hi return krega 2 parameter ke sth)


def sub(x,y):
    return x-y
sub(12,2)  # no output (bcoz we haven't print sub() func)
print(sub(12,2))  # 10 qki humne print kra diya

result=sub(13,2)    # 11 (ese bhi kr skte h kisi value mai store krke)
print(result)




def div():
    return 6.5
print(div())   # 6.5
